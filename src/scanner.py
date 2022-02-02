from .token import *
from .exception import CalcException


class Scanner:
    def __init__(self):
        self.token = None
        self.tokens = list()
        self.position = 0
        self.next_char = ""
        self.expr = ""
        self.eof = False
        self.is_number = False
        self.has_past_decimal = False

    def advance_position(self):
        """Advances position and consumes next expression character"""
        self.position += 1
        if self.position >= len(self.expr):
            self.eof = True
        else:
            self.next_char = self.expr[self.position]

    def is_whitespace(self, char):
        """
        Check if current character is a whitespace

        Parameters
        ----------
        char: str
        	Character to be checked
        	
        Returns
        -------
        Boolean value
        """
        return char in [" ", "\t"]

    def is_parenthesis(self, char):
        """
        Check if current character is a parenthesis

        Parameters
        ----------
        char: str
        	Character to be checked
        	
        Returns
        -------
        Boolean value
        """
        return char in ["(", ")"]

    def is_number_or_float(self, char):
        """
        Check if current character is a number or a decimal point

        Parameters
        ----------
        char: str
        	Character to be checked
        	
        Returns
        -------
        Boolean value
        """
        return ("0" <= char <= "9") or char == "."

    def is_operator(self, char):
        """
        Check if current character is an operator

        Parameters
        ----------
        char: str
        	Character to be checked
        	
        Returns
        -------
        Boolean value
        """
        return char in ["*", "/", "+", "-"]

    def scan_number(self):
        """Scans a number"""
        # Reset defaults
        self.is_number = False
        self.has_past_decimal = False
        # _whole_number retains the whole number (e.g. '4.0')
        # _float_part retains the float part of the number (e.g. '.5')
        self._whole_number, self._float_part = 0.0, 0.0
        # _float_multiplier holds the value we are going to use to multiply the float part
        # it is 0.1 to retain the same value we are multiplying
        self._float_multiplier = 0.1

        while not self.eof and self.is_number_or_float(self.next_char):
            if self.next_char == ".":
                # Check if there was already a decimal point and raise error
                if self.has_past_decimal:
                    raise CalcException(
                        f"""Malformed number at position {self.position}, multiple decimal points

\t{self.expr}\t{' ' * self.position}^

Hint: float numbers cannot have more than one decimal point"""
                    )
                self.has_past_decimal = True
            elif self.is_number_or_float(self.next_char):
                self.is_number = True
                if not self.has_past_decimal:
                    self._whole_number = int(self._whole_number) * 10 + int(self.next_char)
                else:
                    self._float_part += int(self.next_char) * self._float_multiplier
                    # We divide our float multiplier so it will always affect only last decimal place, e.g.
                    # 0.1 for 1 decimal place, 0.01 for 2 decimal places and so on
                    self._float_multiplier /= 10
            self.advance_position()
        if not self.is_number:
            raise CalcException(
                f"""Malformed number at position {self.position - 1}, decimal point without digits

\t{self.expr}\t{' ' * (self.position - 1)}^

Hint: float numbers consists in an optional number followed by a decimal point
        and a decimal value, e.g. \'.7\' or \'4.5\'"""
            )
        self._whole_number += self._float_part
        if self._whole_number.is_integer():
            return int(self._whole_number)
        return self._whole_number

    def get_next_token(self):
        """Gets the next token based on next character in expression"""
        self.token = None
        if self.next_char == TokenType.EOF:
            self.eof = True
        if self.eof:
            self.token = None
        elif self.is_whitespace(self.next_char):
            self.token = TokenType._WHITESPACE
            self.advance_position()
        elif self.is_parenthesis(self.next_char):
            self.token = ParenthesisToken(self.next_char)
            self.advance_position()
        elif self.is_operator(self.next_char):
            self.token = OperatorToken(self.next_char)
            self.advance_position()
        elif self.is_number_or_float(self.next_char):
            self.token = NumberToken(self.scan_number())
        else:
            return self.token
        return self.token

    def scan_expr(self, expr):
        """
        Scans a given expression and returns the expression tokens

        Parameters
        ----------
        expr: str
        	
        Returns
        -------
        A list of tokens
        """
        self.expr = expr
        self.token = None
        self.position = -1
        self.advance_position()
        while True:
            self.token = self.get_next_token()
            if self.token is not None and not self.eof:
                # Skip whitespace tokens
                if self.token != TokenType._WHITESPACE:
                    self.tokens.append(self.token)
            else:
                break
        return self.tokens
