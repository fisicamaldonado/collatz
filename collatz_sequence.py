def collatz_sequence(starting_number):
    """
    Calculates the Collatz sequence for a given starting number.
    """
    sequence = [starting_number]
    while starting_number != 1:
        if starting_number % 2 == 0: #if the starting number is even, divide by 2 (N/2).
            starting_number = starting_number // 2
        else:
            starting_number = 3 * starting_number + 1 #if the starting number is odd, multiply by 3 and add 1 (3N + 1).
        sequence.append(starting_number)
    return sequence

n = 10
print(collatz_sequence(n))
