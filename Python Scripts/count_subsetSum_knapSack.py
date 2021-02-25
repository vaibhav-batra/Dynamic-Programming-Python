import time

# SubSet Sum Knapsack

#Returns the maximum value that can be stored by the bag
def countsubSetSum(set, n, S):

    K = [[0 for i in range(S+1)] for i in range (n+1)]

    # If sum is 0, then answer is True~1
    for i in range(n+1):
        K[i][0] = 1

    for i in range(1,n+1):
        # i is iterating over the indexes of elements
        for j in range(1,S+1):
            # j is iterating over values of S
            if set[i-1] > j:
            # Don't include
                K[i][j] = K[i-1][j]
            else:
                # Take counts of subsets where sum matches S
                K[i][j] = K[i-1][j] + K[i-1][j-set[i-1]]
    return K[n][S]

if __name__ == "__main__":

    wt = [1,5,5,11,4,7,2]
    S = 11
    n = len(wt)
    start = time.time()
    a = countsubSetSum(wt, n, S)
    end = time.time()
    # print("Time elapsed with Memoization:{}".format(end-start))
    print(a)
