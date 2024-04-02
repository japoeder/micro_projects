import numpy as np


# Create the exception class for invalid prob amps
class InvalidProbabilityAmplitude(Exception):
    pass


class Qubit:
    # Define qubit constructor
    def __init__(self, in_kets, v_amp=0):
        self.in_kets = in_kets
        # Only run the amplitude validation when flagged
        if v_amp == 1:
            Qubit.validate_amplitudes(self)

    # Method to calculate the probability amplitudes
    def prob_amplitudes(self):

        # This is the square of alpha and the square of beta
        ik0 = np.square(self.in_kets[0])
        ik1 = np.square(self.in_kets[1])

        # Return tuple with the probability of 0 or 1 qubit from a measurement
        p_amps = (ik0, ik1)
        return p_amps

    # Method to validate the amplitudes
    def validate_amplitudes(self):
        # Run prob amp calculation
        va = Qubit.prob_amplitudes(self)
        # Need to ensure alpha and beta sum of squares equals 1
        va_test = va[0] + va[1]
        # Raise error when the sum of squares doesn't equal one, but include some tolerance
        if abs(1 - va_test) > .00000001:
            raise InvalidProbabilityAmplitude("Invalid probability amplitude(s).")
        return

    # Run binomial dist experiment
    def experiment(self, states):
        # Only need to choose one of the states' prob amps, choosing second
        p = float(states[1][0])
        # Sample the binomial distribution n=1 times in 1000 experiments
        s = np.random.binomial(1, np.square(p), 1000)
        # Calculate the ratio to get % of 1s
        one_p = sum(s) / 1000
        # 1 minus one_p to get % of 0s
        zero_p = 1 - one_p
        # Stick in a dictionary and return
        e_res = {0: zero_p, 1: one_p}
        return e_res

    def __str__(self, states=[]):
        # If no processed states, grab from original list to print
        if len(states) == 0:
            states = self.in_kets
            s0 = float(states[0])
            s1 = float(states[1])
        # If processed states, grab from numpy array
        else:
            s0 = float(states[0][0])
            s1 = float(states[1][0])

        # Deal with small amplitude numbers
        if abs(s0) < .0000000000000001:
            s0 = 0.0
        if abs(s1) < .0000000000000001:
            s1 = 0.0

        return f"{s0}|0> + {s1}|1>"
