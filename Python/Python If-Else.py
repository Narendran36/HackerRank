n = int(input())
if(n%2 != 0 ):
    print("Weird")
else:
    if(n<=5 and n>=2):
        print("Not Weird") 
    elif(n<=20 and n>=6):
        print("Weird")
    else: 
        print('Not Weird')
