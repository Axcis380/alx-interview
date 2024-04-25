def minOperations(n):
    if n <= 1:
        return n

    # Initialize the minimum number of operations required for each position
    min_ops = [0] * (n + 1)

    for i in range(2, n + 1):
        min_ops[i] = float('inf')
        for j in range(1, i):
            # If i is divisible by j, it means that you can obtain i by copying j times and pasting i//j times
            if i % j == 0:
                min_ops[i] = min(min_ops[i], min_ops[j] + i // j)

    return min_ops[n]

# Testing the function
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
