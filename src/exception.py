class CalcException(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        if self.message:
            return f"CalcException: {self.message}"
        else:
            return "CalcException: Something went wrong ..."
