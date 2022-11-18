import random


def gcd(a, b):
    # find greatest common denominator
    if (b == 0 ) :
        return a
    return gcd(b, a % b)

def extendedEuclid(a, b):
    # used for inverse of a mod b
    if a == 0:
        return b, 0, 1
     
    gcd, x1, y1 = extendedEuclid(b%a, a)

    x = y1 - (b // a) * x1
    y = x1
    
    # x = a inverse mod b, y = b inverse mod a
    return gcd, x, y

def multiplicativeOrder(a, n):
    if (gcd(a, n) != 1):
        return -1
    result = 1
    i = 1
    while (i < n): 
        # modular arithmetic
        result = (result * a) % n
        # return smallest + ve integer
        if (result == 1):
            return i
        # increment power
        i += 1
    return -1

def findPrimitive(n):
    # lists all primitive elements in field Zn
    for a in range(1, n):
        if multiplicativeOrder(a, n) == (n-1):
            print(a)

def squareAndMult(base, pow, mod):
    # exponent in mod
    binstring = format(pow, 'b')
    current = 1
    for i in binstring:
        current = (current * current) % mod
        if i=='1':
            current = (current * base) % mod
    return current

def fermatTest(p, s): # retuns true if prime, false if composite
    for i in range(0, s):
        a = random.randint(2, p-2)
        if gcd(a, p) == 1:
            if squareAndMult(a, p-1, p) != 1:
                return False # is composite
    return True # is prime

def checkPrime(n): # returns true if prime, false if not
    for i in range(2, int(n**(1/2))):
        if n % i == 0:
            return False
    return True

def carmichael(n):
    for i in range(5, n, 2):
        if fermatTest(i, 20):
            if not checkPrime(i):
                print(i)

def discreteLog(a, base, mod):
    x=0
    while True:
        if squareAndMult(base, x, mod) == a:
            return x
        x+=1
        if x>500:
            return 0

def main():
    while True:
        command = input(">>")
        calc = command.split(" ")
        if calc[0] == 'q':
            return
        elif calc[0] == "gcd":
            print(gcd(int(calc[1]), int(calc[2])))
        elif calc[0] == "euclid":
            print(extendedEuclid(int(calc[1]), int(calc[2])))
        elif calc[0] == "order":
            print(multiplicativeOrder(int(calc[1]), int(calc[2])))
        elif calc[0] == "primitive":
            print(findPrimitive(int(calc[1])))
        elif calc[0] == "modPow":
            print(squareAndMult(int(calc[1]), int(calc[2]), int(calc[3])))
        elif calc[0] == "checkPrime":
            print(checkPrime(int(calc[1])))
        elif calc[0] == "discreteLog":
            print(discreteLog(int(calc[1]), int(calc[2]), int(calc[3])))
        else:
            print("Command not recognized")
        
main()