# As we understand from the name sort it is a way of sorting that makes the 
#    list of element look like a wave

# For example an array after a wave sort will be:
#    >=arr[1]<=arr[2]>=arr[3]<=


# The code for Wave sort:

def swap(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]

def WaveSort(arr,n):

    for i in range(0,n-1,2):
        if i>0 and arr[i-1]>arr[i]:
            swap(arr,i,i-1)
        
        if i<n-1 and arr[i]<arr[i+1]:
            swap(arr,i,i+1)

    return arr




# Driver code for the function:

if __name__=='__main__':

   
    numbers=[]

    n=int(input("Length of arr: "))

    print("Enter the elements: ")

    for i in range(n):
        elements=int(input())
        numbers.append(elements)

    numbers=WaveSort(numbers,n)

    print("After Wave Sort: ")
    for i in range(0,n):
        print(numbers[i])