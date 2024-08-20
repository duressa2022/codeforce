def helper(array,left,right):
    pivot=array[right]
    i=left-1
    for j in range(left,right):
        if array[i]<pivot:
            j=j+1
            (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[right])=(array[right],array[i+1])
    return i+1
def solver(array):
    temp=[value for value in array]
    result=[]
    def minSolver(array,left,right):
        if left>=right:
            return 
        index=helper(array,left,right)
        if array[index]==temp[index]:
            result.append(array[index])
        else:
            minSolver(array,left,index-1)
            minSolver(array,index+1,right)
    minSolver(array,0,len(array)-1)
    return result








    
    




    


