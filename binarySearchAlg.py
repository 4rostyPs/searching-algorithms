#binary search alg

sampleList = [1,2,3,4,5,6,7,8,9]
element = 103
low = 0 
high = len(sampleList)-1
mid = (low+high)//2
while low <= high:
    if element == sampleList[mid]:
        print(mid)
        break
    elif element < sampleList[mid]:
        high = mid - 1
        mid = (low+high)//2
    else:
        low = mid + 1
        mid = (low+high)//2
print("End")
