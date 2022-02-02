class ExprTree(object):
    def __init__(self):
        self.data = None
        self.lhs = None
        self.rhs = None


class OperatorTree(ExprTree):
    def __init__(self, data, lhs, rhs):
        super().__init__()
        self.data = data
        self.lhs = lhs
        self.rhs = rhs

    @property
    def operator(self):
        """
        Get the OperatorTree operator value, e.g. '+'

        Returns
        -------
        operator
        """
        return self.data


class NumberTree(ExprTree):
    def __init__(self, data):
        super().__init__()
        self.data = data

    @property
    def number(self):
        """
        Get the NumberTree number value, e.g. '3'

        Returns
        -------
        number
        """
        return self.data
