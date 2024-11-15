class ParseError(Exception):

    """ Parse error.

        Indicates any failure during parsing.
    """

    def __init__(self, message, token=None):            
        super().__init__(message)
        self.token = token
