def min_players(N, K, heights):
    count = 0
    for h in heights:
        if h > K:
            count += 1
    return count

# Read number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read inputs for each test case
    N, K = map(int, input().split())
    heights = list(map(int, input().split()))
   
    # Calculate and print the result for the current test case
    result = min_players(N, K, heights)
    print(result)
