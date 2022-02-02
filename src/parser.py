from .ast import *
from .token import TokenType
from .exception import CalcException


class Parser:
    def __init__(self):
        self.tokens = list()
        self.iterator = 0
        self.current_token = None
        self.ast = None

    def consume_token(self):
        """Advances position and consumes next token in the tokens list"""
        if self.iterator <= self.tokens.index(self.tokens[-1]):
            self.iterator += 1
        if self.iterator > self.tokens.index(self.tokens[-1]):
            self.current_token = None
        else:
            self.current_token = self.tokens[self.iterator]

    def parse_number(self):
        """Parse numbers in expression"""
        if not self.current_token:
            raise CalcException("Reached end of tokens while expecting a number in 'Parser.parse_number'")
        if self.current_token.type == TokenType.NUMBER:
            value = self.current_token.value
            self.consume_token()
            return NumberTree(value)
        else:
            raise CalcException(f"Expected a number, got '{self.current_token.value} ({self.current_token.type})'")

    def parse_mult_div(self):
        """Parse multiplication and div"""
        mult_div = self.parse_postfix()
        while self.current_token and self.current_token.type in [TokenType.TIMES, TokenType.DIV]:
            op = self.current_token.value
            self.consume_token()
            mult_div = OperatorTree(op, mult_div, self.parse_postfix())
        return mult_div

    def parse_expr(self):
        """Parse an expression"""
        expr = self.parse_mult_div()
        while self.current_token and self.current_token.type in [TokenType.PLUS, TokenType.MINUS]:
            op = self.current_token.value
            self.consume_token()
            expr = OperatorTree(op, expr, self.parse_mult_div())
        return expr

    def parse_postfix(self):
        """Parse postfix operators (parenthesis)"""
        if not self.current_token:
            raise CalcException("Reached end of tokens while expecting a number in 'Parser.parse_postfix'")
        postfix = None
        if self.current_token.type == TokenType.LPAREN:
            self.consume_token()
            postfix = self.parse_expr()
            if not self.current_token or self.current_token.type != TokenType.RPAREN:
                raise CalcException("Malformed parenthesized expression, missing right parenthesis")
            self.consume_token()
        else:
            postfix = self.parse_number()
        return postfix

    def parse(self, tokens):
        """Parse the given tokens"""
        if not tokens:
            raise CalcException("Parser received an empty tokens list")
        self.tokens = tokens
        self.current_token = self.tokens[0]
        expr_ast = self.parse_expr()
        if self.current_token is not None:
            raise CalcException(f"Unconsumed token '{self.current_token}' at the end of the expression")
        return expr_ast
