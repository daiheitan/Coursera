def quicksort(arr,start,end):
    if start==end||start+1==end:
        return
    pivot=arr[start]
    f=start
    e=end
    for i in range(start+1,end):
        if arr[i]<pivot:
            arr[start]=arr[i]
            f++
        elif arr[i]>pivot:
            p=arr[end-1]
            arr[end-1]=arr[i]
            arr[i]=p
            i--
            end--
    arr[f]=pivot
    quicksort(arr,start,f)
    quicksort(arr,f+1,end)
f=open('QuickSort.txt','r')
arr=[]
while(temp=f.readline()):
    arr.append(int(temp))
f.close()
quicksort(arr,0,len(f))
f=open('result.txt','w')
for i in arr:
    f.write(i)
f.close()
