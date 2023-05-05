# Turn/IP
# Claire-lex - 2023
# Interface to OpenAI for AI-generated data

import openai
from openai.error import AuthenticationError
# Internal
from config import ai

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

#-----------------------------------------------------------------------------#
# AI class                                                                    #
#-----------------------------------------------------------------------------#

class AIException(Exception):
    pass

class AI(object):
    """Handle requests to OpenAI to extract data for protocols."""
    def __init__(self):
        openai.api_key = ai.key

    def scenario_generator(self, protocol) -> str:
        # Global information
        {
            ai.is_protocol: ai.yes_no_question.format()
        }
        
    def request(self, request:str) -> str:
        try:
            return self.__openai_request(request)
        except AuthenticationError as ae:
            raise AIException(ERR_AIAUTH) from None
        
    def __openai_request(self, request: str) -> str:
        response = openai.Completion.create(
            model=ai.model,
            prompt=request,
            temperature=ai.temperature,
            max_tokens=ai.max_tokens
        )
        return response.choices[0].text.strip()
