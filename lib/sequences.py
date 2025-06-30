# Function that prints a list of Fibonacci sequences. 

# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21]
# Logic: [[0]=0, [1]=1+0, [2]=1+0, [3]=1+1, [4] =1+2, [5]=2+3......]

def print_fibonacci(length): # Takes an argument length that defines how many fibonacci sequences you want to print
    if length <= 0:
        print([]) # No element
        return

    sequence = [0,1] # Initialize the Fibonacci series with the 1st 2 no.s

    while len(sequence) < length:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)

    print(sequence[:length])       
    