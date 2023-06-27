# Turn/IP
# Claire-lex - 2023
# Interface to OpenAI for AI-generated data
# pylint: disable=invalid-name,import-error,no-self-use

"""Generate data with OpenAI models.

You need a paid OpenAI account to use this feature.

WARNING: As you may now, AI-generated data is not the most reliable.
Default questions are very restricted to reduce the risk of false information
but it can generate wrong data nevertheless. Therefore, all AI-generated data
is marked with *, please double-check it.
"""

from re import findall
from importlib.util import find_spec
try:
    import openai
    from openai.error import AuthenticationError, RateLimitError
except ModuleNotFoundError:
    pass
# Internal
from config import ai, protocols as p
from . import SearchException

#-----------------------------------------------------------------------------#
# Constants                                                                   #
#-----------------------------------------------------------------------------#

ERR_OAPI = "OpenAI API not found (pip install openai)"
ERR_AIAUTH = "Your OpenAI API key is invalid or you don't have a paid plan."
ERR_NOPROTO = "AI does not recognize {0} as a protocol (message: {1})."

#-----------------------------------------------------------------------------#
# AI class                                                                    #
#-----------------------------------------------------------------------------#

class AI(object):
    """Handle requests to OpenAI to extract data for protocols."""
    def __init__(self):
        # It will raise an exception (not caught this time) if not installed.
        if not find_spec('openai'):
            raise SearchException(ERR_OAPI)
        openai.api_key = ai.key

    #--- Public --------------------------------------------------------------#

    def request(self, request: str) -> str:
        """Send request to OpenAI API using openai library."""
        try:
            return self.__openai_request(request)
        except AuthenticationError:
            raise SearchException(ERR_AIAUTH) from None
        except RateLimitError as rle:
            raise SearchException(str(rle)) from None

    def protocol_generator(self, name: str) -> str:
        """Sequence a list of questions about a protocol to request."""
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

    #--- Private -------------------------------------------------------------#

    def __openai_request(self, request: str) -> str:
        """Prepare request to send to OpenAI API."""
        response = openai.Completion.create(
            model=ai.model,
            prompt=request,
            temperature=ai.temperature,
            max_tokens=ai.max_tokens
        )
        return response.choices[0].text.strip()

    def __security_questions(self, name: str) -> str:
        """Prepare and format answer to security-related questions."""
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
