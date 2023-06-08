import matplotlib.pyplot as plt

def collatz_sequence(starting_number):
    """
    Calculates the Collatz sequence for a given starting number.
    Returns a list of iterations and the corresponding number sequence.
    """
    if not isinstance(starting_number, int) or starting_number <= 0:
        raise ValueError("Input must be a positive integer.")
    sequence = [starting_number]
    iteration_count = [0]
    counter = 0
    while starting_number != 1:
        if starting_number % 2 == 0:
            starting_number = starting_number // 2
        else:
            starting_number = 3 * starting_number + 1
        counter += 1
        iteration_count.append(counter)
        sequence.append(starting_number)
    return [iteration_count, sequence]

def plot_collatz_sequence(starting_number):
    """
    Plots the Collatz sequence for a given starting number.
    """
    collatz_seq = collatz_sequence(starting_number)
    iteration_count = collatz_seq[0]
    number_sequence = collatz_seq[1]
    plt.plot(iteration_count, number_sequence, 'b.') #plots the Collatz sequence as dots versus the number of iterations
    plt.plot(collatz_seq[0], collatz_seq[1], 'r-') #Trace a line between each pair of points in the sequence
    plt.xlabel('Iterations')
    plt.ylabel('Sequence numbers')
    plt.title(f'Collatz sequence for n={starting_number}')
    plt.show()

plot_collatz_sequence(10)
