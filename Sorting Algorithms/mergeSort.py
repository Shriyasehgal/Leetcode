'''Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. '''

def merge(nums,l,r,m):
    L=nums[l:m+1]
    R=nums[m+1:r+1]

    i=j=0
    k=l
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            nums[k]=L[i]
            i+=1
        else:
            nums[k]=R[j]
            j+=1
        k+=1

    while i<len(L):
        nums[k]=L[i]
        i+=1
        k+=1

    while j<len(R):
        nums[k]=R[j]
        j+=1
        k+=1



def mergeSort(nums,l,r):
    if l < r:

        m=(l+r)//2
        mergeSort(nums,l,m)
        mergeSort(nums,m+1,r)
        merge(nums,l,r,m)

nums=[7,5,6,4,3,32,3,1,3,4,5,9,8,4,5,6,87,9,7,65,4,3,4,5,7,8,64,3,34,4,3,2,6,778,6,5,7,5,6,4,3,32,3,1,3,4,5,9,8,4,5,6,87,9,7,65,4,3,4,5,7,8,64,3,34,4,3,2,6,778,6,5]

mergeSort(nums,0,len(nums)-1)
print(nums)
