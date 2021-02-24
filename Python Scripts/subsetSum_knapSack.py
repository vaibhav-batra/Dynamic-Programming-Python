import time

# SubSet Sum Knapsack

#Returns the maximum value that can be stored by the bag
def subsetSum(set, n, S):

    K = [[False for i in range(S+1)] for i in range (n+1)]

    for i in range(n+1):
        K[i][0] = True

    for i in range(1,n+1):
        # i is iterating over the indexes of elements
        for j in range(1,S+1):
            # j is iterating over values of S
            if set[i-1] > j:
            # Don't include
                K[i][j] = K[i-1][j]
            else:
                # Check both case where include or not and if either of them is True
                K[i][j] = K[i-1][j] or K[i-1][j-set[i-1]]
    return K[n][S]

if __name__ == "__main__":

    wt = [8,16,32,40,8,16,32,40,8,16,32,40,8,16,32,40,8,16,32,40]
    S = 200
    n = len(wt)
    start = time.time()
    a = subsetSum(wt, n, S)
    end = time.time()
    # print("Time elapsed with Memoization:{}".format(end-start))
    print(a)
