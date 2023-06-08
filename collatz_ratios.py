"""
This file, adds the ratios between the iterations of the magical numbers and those numbers.
"""

import matplotlib.pyplot as plt
from plot_collatz import collatz_sequence

    
def find_largest(starting_number):
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
            
    # Defining the 'Magical Numbers' as those numbers in the Collatz sequence that show local maximum iterations
    
    print('The largest number in the sequence is', new_sequence[1][0], 'with', len(new_sequence[0]), 'elements.')
    print('Max iterations between 2 and', starting_number, ': ', max_iterations)
    print('The magical numbers are:', max_sequence)
    
    ratios = list(map(lambda x, y: x / y, max_iterations, max_sequence)) #Creating a list of ratios between iterations and max_sequence
    #ratios2 = [iter / max_seq for iter, max_seq in zip(max_sequence,iterations)] #An optional approach
    plt.plot(max_sequence,ratios, 'b.')
    plt.plot(max_sequence,ratios,'r-')
    plt.xlabel('Magical Numbers')
    plt.ylabel('Max Iterations/Magical Numbers')
    plt.title(f'Ratios Iterations/Collatz Magical numbers until n={starting_number}')
    plt.show()
    print(ratios)

        
find_largest(100)
