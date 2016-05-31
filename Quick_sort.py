def partition(A,start,end):
    if(start>=end):
        return
    pivot = A[end]
    pindex = start
    for i in range(start,end):
        if(A[i]<=pivot):
            A[i],A[pindex]=A[pindex],A[i]
            pindex= pindex+1
    A[pindex],A[end]=A[end],A[pindex]
    return pindex

def q_sort(A,start,end):
    if(start < end):
        p = partition(A,start,end)
        q_sort(A,start,p-1)
        q_sort(A,p+1,end)
    return

#test case 1
A = [4,1,8,2,5,6]
q_sort(A,0,len(A)-1)
print A

#test case 2
A = [1]
q_sort(A,0,len(A)-1)
print A

#test case 3
A = []
q_sort(A,0,len(A)-1)
print A

#test case 4
A = [-1,0,2,9,6]
q_sort(A,0,len(A)-1)
print A
