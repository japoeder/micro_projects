from operators import *
import numpy as np


# Create class for paulix operator, inherit from SingleQubitOperator
class PauliX(SingleQubitOperator):
    def __init__(self, in_ops=[]):
        self.in_ops = in_ops
        # If a list of operators is provided, validate with SingleQubitOperator
        if len(in_ops) > 0:
            super().__init__(self.in_ops)

    # Define method for operator calculation
    def operator(self, in_ket_state):
        x_gate = np.identity(2)[::-1]
        rev_state = np.matmul(x_gate, in_ket_state)
        return rev_state
