import os
import json
def smallest_missing_positive_integer(A):
    A.sort()
        #usporiadaj array of integers od najmensieho
    N = len(A)
    #N je dlzka pola
    
    i = 0
    previous = 0
    while i < N:
        current = A[i]

        if current > 0:
            if current > previous + 1: # breaks consecutiveness
                return previous + 1
            else:
                previous = current
        
        i += 1
    
    return max(previous+1, current+1)
C = open("C:\\temp\smallest.txt","r")
print(type(C))
B = [(line.strip(",")) for line in open("C:\\temp\smallest.txt","r")]
#C=print(B.read())
#C=print(list((B.read()).split(",")))
print(type(B))
print(B,len(B))
#C = [int(k.strip(',')) for k in B]
#print(type(C))
#D=list(C.split(","))
#print(D)
#D=json.loads(C)
#D=int(C.split(','))
#print(D)
#x=[0,1,4,5,7,6]
#print(smallest_missing_positive_integer(C))