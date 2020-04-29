# Enter your code here. Read input from STDIN. Print output to STDOUT

N,M = input().split()
N = int(N)
M = int(M)
t_b = N//2
m = (M-7)//2

for x in range(1,t_b+1):
    print("-"*((M-3*(2*x-1))//2)+".|."*(2*x-1)+"-"*((M-3*(2*x-1))//2))

print("-"*m+"WELCOME"+"-"*m)

for x in range(t_b,0,-1):
    print("-"*((M-3*(2*x-1))//2)+".|."*(2*x-1)+"-"*((M-3*(2*x-1))//2))
