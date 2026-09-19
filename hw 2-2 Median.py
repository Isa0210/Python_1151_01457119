arr=[]
#print("test")
try:
    while True:
        t=input()
        arr.append(int(t))
        '''
        print(f"t = {t}")#輸出t數值
        print("array:", end=' ')#輸出arr
        for i in range(len(arr)):
                print(arr[i], end=' ')
        print()
        '''
        #arr.sort()
        for d in range(0, len(arr)-1):#要比較的
            #print(f"len(arr) = {len(arr)}")#debug輸出陣列長度
            if arr[len(arr)-1] < arr[d]:
                arr.insert(d, arr.pop())
                break
        '''
        print("sorted array:", end=' ')#輸出排序後arr
        for i in range(len(arr)):
                print(arr[i], end=' ')
        print()
        '''
        n = len(arr)
        if n % 2 == 0:
            median = (arr[n//2 - 1] + arr[n//2]) // 2
        else:
            median = arr[n//2]
        #print("median:", end=' ')
        print(median)
except EOFError:
    pass