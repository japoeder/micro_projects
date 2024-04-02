# Set initial password 8bit string (this is the password)
# Decide the tap position
import pprint


class LFSR:
    # create an LFSR with initial state ‘seed’ and tap ‘tap’
    def __init__(self, seed: str, tap: int):
        self.seed = seed
        self.tap = tap

    # return the bit at index ‘i’
    def bit(self, i: int):
        beg = len(self.seed) - i
        end = beg + 1
        bit_select = self.seed[beg:end]
        return bit_select

    # execute one LFSR iteration and return new (rightmost) bit as an int
    # you will find the binary XOR operator useful here
    def step(self):
        lfsr_newbit = 1 if self.seed[0] != LFSR.bit(self, self.tap) else 0
        return lfsr_newbit

    def __str__(self):
        lfsr = self.seed[1:] + str(LFSR.step(self))
        return lfsr


# your executable code that invokes LFSR
def main():
    print(LFSR('0110100111', 2), LFSR('0110100111', 2).step())
    print(LFSR('0100110010', 8), LFSR('0100110010', 8).step())
    print(LFSR('1001011101', 5), LFSR('1001011101', 5).step())
    print(LFSR('0001001100', 1), LFSR('0001001100', 1).step())
    print(LFSR('1010011101', 7), LFSR('1010011101', 7).step())


if __name__ == "__main__":
    main()
