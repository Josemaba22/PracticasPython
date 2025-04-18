class OrdenaLista:
    def bubblueSort(arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] < arr[j]:
                    print('[',i,',',j,']')
                    aux = arr[i]
                    arr[i] = arr[j]
                    arr[j] = aux
        print(arr)


arr = [3,5,2,3,1]
OrdenaLista.bubblueSort(arr)
