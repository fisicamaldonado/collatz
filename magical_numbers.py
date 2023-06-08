import matplotlib.pyplot as plt
from plot_collatz import collatz_sequence


def find_largest(starting_number):
    """
    Find the Largest number is Collatz set startting from 2 to the given number.
    Creates a set of 'Magical numbers'. Each of one of those magical numbers produces a local maximum of iterations.
    """
    max_iterations = []
    max_sequence = []
    new_sequence = collatz_sequence(2)
    for i in range (2, starting_number+1):
        test_sequence = collatz_sequence(i)
        iterations = test_sequence[0]
        if len(iterations) > len(new_sequence[0]):
            max_sequence.append(test_sequence[1][0])  # Store the new local maximum of the sequence
            max_iterations.append(len(iterations))  # Store the iteration for that maximum
            new_sequence = test_sequence
    print_magical_numbers(max_sequence,max_iterations,new_sequence,starting_number)
        
    
# Defining the 'Magical Numbers' as those numbers in the Collatz sequence that show local maximum iterations
    
def print_magical_numbers(max_sequence,max_iterations,new_sequence,starting_number):
    '''
    Plots the Numbers with maximum iterations in the Range (2,starting_number)
    '''
    print('The largest number in the sequence is', new_sequence[1][0], 'with', len(new_sequence[0]), 'elements.')
    print('Max iterations between 2 and', starting_number, ': ', max_iterations)
    print('The magical numbers are:', max_sequence)
    plt.plot(max_sequence, max_iterations, 'b.')
    plt.xlabel('Magical Numbers')
    plt.ylabel('Max Iterations')
    plt.title(f'Collatz Magical numbers until n={starting_number}')
    plt.show()
    
find_largest(100)
