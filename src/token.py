class TokenType:
    TIMES = "*"
    DIV = "/"
    PLUS = "+"
    MINUS = "-"
    LPAREN = "("
    RPAREN = ")"
    NUMBER = "NUMBER"
    EOF = "\n"
    _WHITESPACE = " "


class Token:
    def __init__(self):
        pass

    @property
    def type(self):
        return None


class NumberToken(Token):
    def __init__(self, value):
        super().__init__()
        self.val = value

    @property
    def type(self):
        return TokenType.NUMBER

    @property
    def value(self):
        return self.val


class OperatorToken(Token):
    def __init__(self, value):
        super().__init__()
        self.val = value

    @property
    def type(self):
        self._types = {
            "*": TokenType.TIMES,
            "/": TokenType.DIV,
            "+": TokenType.PLUS,
            "-": TokenType.MINUS,
        }
        return self._types[self.val]

    @property
    def value(self):
        return self.val


class ParenthesisToken(Token):
    def __init__(self, value):
        super().__init__()
        self.val = value

    @property
    def type(self):
        return TokenType.LPAREN if self.val == "(" else TokenType.RPAREN

    @property
    def value(self):
        return self.val


def print_tokens(tokens: list):
    i = 0
    exprs = ""
    print("Printing tokens and expression ...")
    while i != len(tokens):
        token_type, token_value = tokens[i].type, tokens[i].value
        if token_type == TokenType.NUMBER:
            print(f"Number:\t\t{token_value}")
            exprs += str(token_value) + " "
        elif token_type == TokenType.LPAREN or token_type == TokenType.RPAREN:
            print(f"Parenthesis:\t{token_value}")
            exprs += str(token_value) + " "
        elif (
            token_type == TokenType.TIMES
            or token_type == TokenType.DIV
            or token_type == TokenType.PLUS
            or token_type == TokenType.MINUS
        ):
            print(f"Operator:\t{token_value}")
            exprs += str(token_value) + " "
        i += 1
    # Trim whitespaces between parenthesis tokens
    exprs = exprs.replace("( ", "(").replace(" )", ")")
    print(f"Expression:\t{exprs}")
