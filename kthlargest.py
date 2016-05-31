import random

def minheap(A,i):
    l = 2*i + 1
    r = 2*i + 2
    smallest = i
    if l<len(A) and A[l]<A[smallest]:
        smallest = l
    if r<len(A) and A[r]<A[smallest]:
        smallest = r
    if smallest!=i:
        temp = A[i]
        A[i]=A[smallest]
        A[smallest]=temp
    return 

def makeheap(A):
    l = len(A)/2
    for i in xrange(l):
        minheap(A,i)
    return

def heapify(A,i):
    le=len(A)
    l = 2*i+1
    r = 2*i+2
    smallest = i
    if(l < le and A[l]<A[smallest]):
        smallest = l
    if(r < le and A[r]<A[smallest]):
        smallest = r
    if smallest!=i:
        temp = A[i]
        A[i]=A[smallest]
        A[smallest]=temp
        heapify(A,smallest)
    return 

def extractmin(B):
    l = len(B)
    temp = B[0]
    B[0] = B[l-1]
    del B[l-1]
    heapify(B,0)
    return temp

def bubbleup(A,i):
    p = (i-1)/2
    #print i,A[i],p,A[p]
    if(p >= 0 and A[p]>A[i]):
        temp = A[p]
        A[p] = A[i]
        A[i] = temp
        bubbleup(A,p)
    return
    

def insertheap(A,x):
    A.append(x)
    bubbleup(A,len(A)-1)
    return

    
def findnlargest(A,n):
    B = A[0:n]
    makeheap(B)
    for i in xrange(n,len(A)):
        insertheap(B,A[i])
        extractmin(B)            
    return B[0]

def modify(B):
    B.append([1]*5)
    return

Arr = random.sample(xrange(1000), 10)
print Arr
print 'n largest is',findnlargest(Arr,2)

