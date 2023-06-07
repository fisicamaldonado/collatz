def print_collatz_sequence(starting_number, sequence, iterations, max_value):
    """
    Prints the Collatz sequence and related information.
    """
    print('The Collatz Sequence for number', starting_number, 'is:', sequence)
    print('Max value in the sequence is', max_value)
    print('There are', iterations, 'iterations in this sequence')
    print('The ratio between the # of Iterations and the starting number is', iterations / starting_number)
    print('The ratio between the max value and the starting number is', max_value / starting_number)

def collatz_sequence(starting_number):
    """
    Calculates the Collatz sequence for a given starting number.
    """
    if not isinstance(starting_number, int) or starting_number <= 0:
        raise ValueError("Input must be a positive integer.")

    sequence = [starting_number]
    current_number = starting_number

    while current_number != 1:
        if current_number % 2 == 0:
            current_number //= 2
        else:
            current_number = 3 * current_number + 1
        sequence.append(current_number)

    iterations = len(sequence) - 1
    max_value = max(sequence)

    print_collatz_sequence(starting_number, sequence, iterations, max_value)

collatz_sequence(27) #I don't use an input here because is common to use Jupyter Notebooks and it's better with direct inputs in the script.
