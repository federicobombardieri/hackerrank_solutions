#https://www.hackerrank.com/challenges/crush/problem
def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    for operation in queries:
            arr[operation[0] -1]+=operation[2]
            arr[operation[1] -1 +1]+=-operation[2]
    max_val=0
    s=0
    for i in arr[:-1]:       
        s+=i
        max_val = max(max_val, s)
    return(max_val)
