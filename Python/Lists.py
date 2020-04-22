if __name__ == '__main__':
    N = int(input())
    data = []
    for i in range(N):
        task = input().split()
        if(task[0] == "insert"):
            data.insert(int(task[1]),int(task[2]))
        elif(task[0] == "print"):
            print(data)
        elif(task[0] == "remove"):
            data.remove(int(task[1]))
        elif(task[0] == "append"):
            data.append(int(task[1]))
        elif(task[0] == "sort"):
            data.sort()
        elif(task[0] == "pop"):
            data.pop()
        elif(task[0] == "reverse"):
            data.reverse()  
