import numpy as np


class MatrixNotInvertible(Exception):
    pass


class PlaintextKeyMismatch(Exception):
    pass


class HillCypher:

    # initialize an HilLCypher object with a key and plaintext
    def __init__(self, P, K):
        self.P = P
        self.K = K
        self.m = 26

        # Create translation dicts for use later
        self.alpha_num = {chr(i + 64): i - 1 for i in range(1, 27)}
        self.num_alpha = {y: x for x, y in self.alpha_num.items()}
        return

    def string_to_alist(self, in_text, my_key):
        # Grab the dimensions of the key matrix
        r1 = my_key.shape[0]
        c1 = my_key.shape[1]

        # Check to see if string is evenly divisible by c1
        if len(in_text) % c1 != 0:
            # If not, throw error that dimensions don't match
            raise PlaintextKeyMismatch("Plaintext length doesn't match key dimension")
        else:
            # Next, determine the dimensions of the resultant plaintext matrix
            r2 = c1
            c2 = len(in_text) // r2

            # Create an array list, and parse plaintext into a list
            plist = []
            for c in in_text:
                plist.append(self.alpha_num[c])

            # Use list comprehension to break the string into groups that we'll transpose to column vectors
            alist = [plist[i:i + r2] for i in range(0, len(plist), r2)]

            # Convert list to array and reshape
            p_array = []
            for l in alist:
                p_array.append(np.array(l).reshape(r2, 1))

        return p_array

    def alist_to_string(self, hc_array, my_key):
        # Grab the dimensions of the key matrix
        r1 = my_key.shape[0]
        c1 = my_key.shape[1]

        # Grab the dimensions of the input array
        r2 = c1
        c2 = len(hc_array)

        # Convert array to list and reshape
        p_array = []
        for a in hc_array:
            x = np.ndarray.tolist(a.reshape(1, r2))
            p_array.append(x[0])

        # Convert list of lists to single list
        flat_list = [item for sublist in p_array for item in sublist]

        # Convert flattened list to encrypted string
        e_str = ''
        for n in flat_list:
            e_str += self.num_alpha[n]

        return e_str

    def determinant(self):
        # Test to see if the matrix is square.  If not, raise error.
        if np.asmatrix(self.K).shape[0] != np.asmatrix(self.K).shape[1]:
            raise MatrixNotInvertible('The matrix is not square')

        # If the matrix is square, calculate the determinant.
        else:
            D = np.linalg.det(self.K)
            # If the determinant is 0, raise error
            if D == 0:
                raise MatrixNotInvertible('The determinant = 0')

            # If the determinant can be calc'd and isn't 0, return value.
            else:
                return int(D)

    def invertible(self):
        try:
            HillCypher.determinant(self)
            return True
        except:
            return False

    def mod_inverse(self, m, D):
        # Calculate the modular multiplicative inverse
        # Note that we need to use abs value of determinant
        minv = pow(abs(D), -1, m)
        return minv

    def encrypt(self, p_string, in_key):
        # Check invertibility
        HillCypher.determinant(self)

        # Convert string to list of array
        hc_array = HillCypher.string_to_alist(self, p_string, in_key)

        # Process each column vector
        e_hc_list = []
        for a in hc_array:
            e_hc_list.append(np.matmul(in_key, a) % self.m)

        # Grab the encrypted string
        e_str = HillCypher.alist_to_string(self, e_hc_list, in_key)

        # Print some inputs
        print('')
        print(f'Plaintext: {p_string}')
        print(f'Plaintext column vectors: {hc_array}')
        print('')

        print(f'Ciphertext: {e_str}')
        print(f'Ciphertext column vectors: {e_hc_list}')
        print('')

        return e_str, e_hc_list

    def decrypt(self, c_text):
        # Grab the determinant and modular inverse
        D = abs(HillCypher.determinant(self))
        minv = HillCypher.mod_inverse(self, self.m, D)

        # Calculate the modular multiplicative inverse of our key matrix
        # Start with the inverse of the key matrix
        K_inv = np.linalg.inv(self.K)

        # Multiply by determinant and modular inverse
        mmi = minv * (D * K_inv)

        # Grab columns of from first part of mmi
        n_cols = mmi.shape[0]

        # Create identity matrix of same size and flip
        i_flip = np.eye(n_cols)[::-1]

        # Multiply flipped identity matrix by mod and add to mmi to complete the calculation
        mmi = i_flip * self.m + mmi

        # Convert string to list of array
        d_array = HillCypher.string_to_alist(self, c_text, mmi)

        # Process each column vector
        d_hc_list = []
        for a in d_array:
            d_hc_list.append(np.matmul(mmi, a).astype(int) % self.m)

        d_str = HillCypher.alist_to_string(self, d_hc_list, mmi)

        # Print some inputs
        print(f'Plaintext: {d_str}')
        print(f'Plaintext column vectors: {d_hc_list}')
        print('')

        return d_str


def main():
    P = 'ATTACKATDAWN'
    m = 26

    """
    # Input 1
    K1 = np.array([[19, 8, 4], [3, 12, 7]])
    c1 = HillCypher(P, K1)
    print(c1.encrypt(P, K1))
    """

    # Input 2
    K2 = np.array([[7, 8], [11, 11]])
    c2 = HillCypher(P, K2)
    e_val = c2.encrypt(P, K2)[0]
    d_val = c2.decrypt(e_val)

    """
    # Input 3
    K3 = np.array([[5, 15], [4, 12]])
    c3 = HillCypher(P, K3)
    print(c3.encrypt(P, K3))
    """


if __name__ == "__main__":
    main()
