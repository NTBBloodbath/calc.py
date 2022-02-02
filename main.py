from sys import exit
from src.ast import NumberTree
# from src.token import print_tokens
from src.parser import Parser
from src.scanner import Scanner
from src.evaluator import Evaluator
from src.exception import CalcException


class Calc:
    def print_ast(self, ast):
        if isinstance(ast, NumberTree):
            return ast.number
        op = ast.operator
        lhs = self.print_ast(ast.lhs)
        rhs = self.print_ast(ast.rhs)
        if op:
            print(f"({op}", end=" ")
        if lhs:
            print(lhs, end=" ")
        elif self._ast_prev_lhs:
            print(self._ast_prev_lhs, end=" ")
        if rhs:
            print(rhs, end="")
        print(")")
        # Set previous AST lhs as the result of the current AST
        self._ast_prev_lhs = self.evaluator.eval(ast)

    def __init__(self):
        self._ast_prev_lhs = None

        try:
            print("Welcome to calc, type 'exit' to exit calc.")
            while True:
                # Set (and reset) defaults for our calculator class
                self.ast = None
                self.tokens = list()
                self.scanner = Scanner()
                self.parser = Parser()
                self.evaluator = Evaluator()
                # Get expression from REPL
                expr = input(">> ")
                if expr == "exit":
                    return
                expr += "\n"
                # ===== Tokenizer
                self.tokens = self.scanner.scan_expr(expr)
                # Print tokens (debugging)
                # print_tokens(self.tokens)
                # ===== AST generator
                self.ast = self.parser.parse(self.tokens)
                # Print AST (debugging)
                # print("Printing expression AST ...")
                # self.print_ast(self.ast)
                # ===== Evaluator
                result = self.evaluator.eval(self.ast)
                # Print expression result
                print(f"> {result}")
        except CalcException as err:
            # In this way we avoid that ugly traceback
            # when raising our custom exception
            print(err)
            exit(1)


if __name__ == "__main__":
    Calc()
