if __name__ == '__main__':
    s = input()
    x = False
    a = False 
    d = False 
    l = False
    u = False
    for i in range(len(s)):
        if s[i].isalpha():
            a = True
            x = True
        if s[i].isdigit():
            d = True
            x = True
        if s[i].islower():
            l = True 
        if s[i].isupper():
            u = True
        if l == True and u == True and a == True and d == True:
            break
    print(x)
    print(a)
    print(d)
    print(l)
    print(u)
