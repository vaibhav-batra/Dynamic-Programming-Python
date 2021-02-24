import time

# SubSet Sum Knapsack

#Returns the maximum value that can be stored by the bag
def subsetSum(W, wt, val, n):

    K = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]

if __name__ == "__main__":
    # Without Memoization
    values = [50,100,150,200,50,100,150,200,50,100,150,200,50,100,150,200,50,100,150,200]
    weights = [8,16,32,40,8,16,32,40,8,16,32,40,8,16,32,40,8,16,32,40]
    W = 200
    index = len(weights)
    # Call Function
    start1 = time.time()
    b = knapSack(weights, values, W, index)
    end1 = time.time()
    print("Time elapsed without Memoization:{}".format(end1-start1))

    # With Memoization
    val = [50,100,150,200,50,100,150,200,50,100,150,200,50,100,150,200,50,100,150,200]
    wt = [8,16,32,40,8,16,32,40,8,16,32,40,8,16,32,40,8,16,32,40]
    W = 200
    n = len(val)
    start2 = time.time()
    a = knapSackDyn(W, wt, val, n)
    end2 = time.time()
    print("Time elapsed with Memoization:{}".format(end2-start2))

    print("Memoized code is {} times faster, than Non-Memoized code".format( str(round( ((end1-start1) / (end2-start2) ),2))))
