def subsetSum(ar,k,subset,i, curr=0):
    global res
    if curr==k:
        res.append(subset[:])
        return

    elif curr>k or i>=len(ar):
        return

    else:
        subset.append(ar[i])
        curr+=ar[i]
        subsetSum(ar,k,subset,i+1,curr)
        subset.pop()
        curr-=ar[i]
        subsetSum(ar,k,subset,i+1,curr)


res=[]
subsetSum([5,10,12,13,15,18],30,[],0,0)
