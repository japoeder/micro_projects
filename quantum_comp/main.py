from paulix import *
from hadamard import *
from qubit import *


def main():
    # Import & pre-process qubits
    q_file = open('../support/qubits.txt', 'r', encoding='utf-16')
    q_lines = q_file.readlines()
    qubits = {}
    for n, q in enumerate(q_lines):
        # Instantiate some items
        ket_list = []
        gate_list = []

        # Split the record from the data
        l_temp = (q.split())

        # Append ket elements to corresponding list
        ket_list.append(float(l_temp[0]))
        ket_list.append(float(l_temp[1]))

        # Append gate elements to corresponding list
        for e in range(2, len(l_temp)):
            gate_list.append(l_temp[e])

        qubits[n] = (ket_list, gate_list)

    for q in range(n + 1):
        # Pars dictionary for data of interest
        kets = qubits[q][0]
        kets_a = np.reshape(kets, (2, 1))
        ops = qubits[q][1]
        try:
            # Test amplitudes
            Qubit(kets, 1)

            # Next lets check the gates (can call paulix or hadamard)
            try:
                q_test = Qubit(kets)
                print(f"Initial state: {q_test.__str__()}")
                p = PauliX(ops)

            except:
                print("Invalid operator.")
                print("")
                continue

        except:
            print("Invalid probability amplitude(s).")
            print("")
            continue

        # If both tests pass, run gate operations
        for o in ops:
            if o == 'X':
                o_temp = PauliX()
                kets_a = o_temp.operator(kets_a)
            else:
                o_temp = Hadamard()
                kets_a = o_temp.operator(kets_a)

        # Print the final state information
        print(f"Final state: {q_test.__str__(states=kets_a)}")

        # Run the binomial experiment method
        exp = q_test.experiment(kets_a)
        print(f"Percentage of 0's measured: {round((1 - exp[1]) * 100,2)}")
        print(f"Percentage of 1's measured: {round((exp[1]) * 100, 2)}")

        print("")

    return None


if __name__ == "__main__":
    # Print initial state of the qubit at the beginning and the final state once operators have been applied
    # pprint.pprint(main())
    main()
