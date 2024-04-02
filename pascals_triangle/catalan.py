# Create the main method
def main():
    # Start with 4 sided p-gon and loop through 17 sided to get order 15
    for c in range(4, 18):
        catalan(c)
    # Return NoneType
    return


def catalan(p):
    # Start catalan function by asking for new input if p < 4
    if p <= 3:
        p = input('Please enter number of sides > 3: ')

    # Set initial catalan output to 1 for factorial calc
    cat_num = 1

    # Set n from formulae to initial value of p - 2
    n = p - 2

    # Loop through k from formulae, from 2 to n as specified by formula range
    for k in range(2, n + 1):
        # Calculate the ratio value for the loop
        r = (n + k) / k
        # Use '*=' to represent the product notation pi
        cat_num *= r

    # Print results from the catalan function
    print(f'Order {n} Catalan number = {round(cat_num)}')

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
