#linear search alg

sampleList = [1,6,7,8,9,2,3,4,5]
element = 3
for i in range(len(sampleList)):
    if element == sampleList[i]:
        print(i)
        break