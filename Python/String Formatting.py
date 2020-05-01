def print_formatted(number): 
    width = len(str(bin(number))[2:])
    for n in range(1,number+1):
        d = str(n)
        o = str(oct(n)[2:])
        h = str(hex(n)[2:]).upper()
        b = str(bin(n)[2:])
        print ("{0:>{width}} {1:>{width}} {2:>{width}} {3:>{width}}".format(d,o,h,b,width=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
