from operators import *
import numpy as np


# Create class for paulix operator, inherit from SingleQubitOperator
class Hadamard(SingleQubitOperator):
    def __init__(self, in_ops=[]):
        self.in_ops = in_ops
        # If a list of operators is provided, validate with SingleQubitOperator
        if len(in_ops) > 0:
            super().__init__(self.in_ops)

    # Define method for operator calculation
    def operator(self, in_ket_state):
        h_gate = np.multiply(1 / np.sqrt(2), np.array([[1, 1], [1, -1]]))
        eq_wt_super = np.matmul(h_gate, in_ket_state)
        return eq_wt_super
