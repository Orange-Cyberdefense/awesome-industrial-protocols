# Turn/IP
# Claire-lex - 2023
# Interface to OpenAI for AI-generated data

from re import findall
try:
    import openai
except ModuleNotFoundError:
    pass
from openai.error import AuthenticationError, RateLimitError
# Internal
from config import ai, protocols as p
from . import SearchException

"""Generate data with OpenAI models.

You need a paid OpenAI account to use this feature.

WARNING: As you may now, AI-generated data is not the most reliable.
Default questions are very restricted to reduce the risk of false information
but it can generate wrong data nevertheless. Therefore, all AI-generated data
is marked with *, please double-check it.
"""

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_AIAUTH = "Your OpenAI API key is invalid or you don't have a paid plan."
ERR_NOPROTO = "AI does not recognize {0} as a protocol (message: {1})."

#-----------------------------------------------------------------------------#
# AI class                                                                    #
#-----------------------------------------------------------------------------#

class AI(object):
    """Handle requests to OpenAI to extract data for protocols."""
    def __init__(self):
        # It will raise an exception (not caught this time) if not installed.
        import openai
        openai.api_key = ai.key

    def __security_questions(self, name: str) -> str:
        q_security = {
            "encryption": (ai.has_encryption, ai.has_mandatory_encryption),
            "authentication": (ai.has_authentication, ai.has_mandatory_authentication),
            "integrity checks": (ai.has_integrity, ai.has_mandatory_integrity)
        }
        answer = []
        for security, question in q_security.items():
            r = self.request(ai.yes_no_question.format(name, question[0]))
            if r.lower().startswith("yes"):
                r = self.request(ai.yes_no_question.format(name, question[1]))
                if r.lower().startswith("yes"):
                    r = "Mandatory " + security
                else:
                    r = "Optional " + security
                answer.append(r)
        return ", ".join(answer) if answer else ""
        
    def protocol_generator(self, name) -> str:
        q_yes_no = {
            p.access: ai.is_spec_free,
        }
        q_open = {
            p.description: ai.description,
            p.port: ai.default_port
        }
        # First question is just for checking:
        question = ai.yes_no_question.format(name, ai.is_protocol)
        response = self.request(question)
        if not response.lower().startswith("yes"):
            raise SearchException(ERR_NOPROTO.format(name, response))
        # Questions where answer should be yes or no
        for attribute, question in q_yes_no.items():
            question = ai.yes_no_question.format(name, question)
            response = self.request(question)
            response = "Yes" if response.lower().startswith("yes") else "No"
            yield attribute, response+"*"
        # Questions with open answers
        for attribute, question in q_open.items():
            response = self.request("{0} {1}".format(name, question))
            if attribute == p.port:
                response = ", ".join(findall(r'\d+', response))
            yield attribute, response+"*"
        # Multi-level questions about security features
        response = self.__security_questions(name)
        yield p.security, response+"*"

            
    def request(self, request:str) -> str:
        try:
            return self.__openai_request(request)
        except AuthenticationError as ae:
            raise SearchException(ERR_AIAUTH) from None
        except RateLimitError as rle:
            raise SearchException(str(rle)) from None
        
    def __openai_request(self, request: str) -> str:
        response = openai.Completion.create(
            model=ai.model,
            prompt=request,
            temperature=ai.temperature,
            max_tokens=ai.max_tokens
        )
        return response.choices[0].text.strip()
