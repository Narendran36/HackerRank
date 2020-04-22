if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    distinct = list(set(arr)).sort()
    distinct.sort()    
    if len(distinct) != 1:
        print(distinct[-2])
    else:
        print(distinct[0])
