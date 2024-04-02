# Create the main method
def main():
    # Call the pascal function, and generate first 10 rows
    pascal(10)


def pascal(n):
    # When n hits 0, recursion returns nothing
    if n == 0:
        return None

    else:

        # Instantiate a new list at each iteration with 1 as the first element in the new row
        new_list = [1]

        # Going to skip calcs for first row explicitly and second row implicitly via pascal(2-1) => pascal(1)
        if n != 1:

            # Grab results from last iteration
            prior_list = pascal(n - 1)

            # Loop through the prior row / list so new row can be calculated
            for i in range(1, len(prior_list)):
                e0 = prior_list[i - 1]
                e1 = prior_list[i]
                new_list.append(e0 + e1)

            # Add 1 to the right side of the new list
            new_list.append(1)

        # Print without the brackets and delimit with a space
        print(*new_list, sep=" ")

        return new_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
