import time

# SubSet Sum Knapsack


def equalSum(set, n):

    sum = 0

    # For two partitions of equal value, total value must be even
    # If Even, we only want to find a subset of of value sum/2
    for i in set:
        sum+= i

    if sum%2!=0:
        return False

    K = [[False  for i in range(int(sum/2)+1)] for i in range (n+1)]

    # If sum is 0, then answer is True
    for i in range(1, n+1):
        K[i][0] = True

    for i in range(1,n+1):
        # i is iterating over the indexes of elements
        for j in range(1,(int(sum/2)+1)):
            # j is iterating over values of S
            if set[i-1] > j:
            # Don't include
                K[i][j] = K[i-1][j]
            else:
                # Check both case where include or not and if either of them is True
                K[i][j] = K[i-1][j] or K[i-1][j-set[i-1]]
    return K[n][int(sum/2)]

if __name__ == "__main__":

    wt = [1,5,5,3]
    n = len(wt)
    start = time.time()

    a = equalSum(wt, n)
    end = time.time()
    # print("Time elapsed with Memoization:{}".format(end-start))
    print(a)
