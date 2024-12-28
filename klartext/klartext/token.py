""" Module defining a token.
"""

from typing import Any


class Token:

    """ A Token used while parsing the klartext language. 
    """

    # Tokens used by the parser
    TEXT  = 'TEXT'
    EMPTY = 'EMPTY'
    EOF   = 'EOF'
    TAG   = 'TAG'
    XML   = 'XML'
    
    def __init__(self, indent:int, type: str, content: Any) -> None:

        """ Creates a token.

            Args:
                indent:  The level of indentation of the token
                type:    The type of token
                content: Additional content depending on the type of token
        """
        self._indent: int = indent
        self._type: str = type
        self._content: Any = content
    

    def indent(self) -> int:

        """ Get the level of indent.
        
            Returns:
                The level of indentation of the token
        """
        return self._indent
    

    def type(self) -> str:

        """ Get the type of token.
        
            Returns:
                The type of the token
        """
        return self._type
    

    def content(self) -> Any:

        """ Get the content of the token.

            Returns:
                Additional content depending on the type of token
        """
        return self._content
    

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return self._type == other
        return False
 