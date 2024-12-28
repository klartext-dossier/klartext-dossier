""" Module providing exceptions.
"""

from klartext import Token


class ParseError(Exception):

    """ Indicates a parse error.

        This exception is thrown whenever the parser encounters a problem with
        the syntax of the parsed text.
        
        Args:
            message: A message describing the cause of the exception.
            token:   The token that triggered the exception.
    """

    def __init__(self, message: str, token: Token | None = None) -> None:            
        super().__init__(message)
        self.token = token
