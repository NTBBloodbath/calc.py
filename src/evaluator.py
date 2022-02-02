from .exception import CalcException
from .ast import OperatorTree, NumberTree


class Evaluator:
    def __init__(self):
        pass

    def eval(self, ast):
        """
        Evaluates the given AST

        Parameters
        ----------
        ast:
                Calculator AST

        Returns
        -------
        AST operations result, e.g. '+ 1 2' => '3'
        """
        if isinstance(ast, NumberTree):
            return ast.number
        op = ast.operator
        lhs, rhs = self.eval(ast.lhs), self.eval(ast.rhs)
        # We cannot use a lambda for division because we have to
        # handle ZeroDivisionError exception
        def _div(x, y):
            try:
                return x // y if x % 2 == 0 else x / y
            except ZeroDivisionError:
                raise CalcException("Trying to divide by zero")

        operations = {
            "*": lambda x, y: x * y,
            "/": lambda x, y: _div(x, y),
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
        }
        # print(f"Operation: {op}, LHS: {lhs}, RHS: {rhs}, Result: {operations[op](lhs, rhs)}")
        return operations[op](lhs, rhs)
