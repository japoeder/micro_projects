# Create exception class for invalid operators
class InvalidOperator(Exception):
    pass

# Class for testing qubit operator
class SingleQubitOperator:
    def __init__(self, o_matrix):
        self.o_matrix = o_matrix
        # Loop through provided matrix and if operation isn't X or H, raise exception
        for o in self.o_matrix:
            if o not in ['X', 'H']:
                raise InvalidOperator("Invalid operator")
                continue
