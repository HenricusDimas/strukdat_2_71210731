import timeit


def deret_prima(n): 
    x = 1 
    y = 1 
    for y in range(1,n):
        if ((y+1) % 5 == 0):
            print(end="")
        z = y
        y = y+x
        x = z
    
for y in range(1,101):
    start = timeit.default_timer()
    deret_prima(y)  
    end = timeit.default_timer()
    print("n=",y,"iteratif ->", end-start,"second")
print()


def deretprima(n):
    if n <= 1:
        return n
    else:
        return (deretprima(n-1)+deretprima(n-2))

for y in range(1,101):
    start = timeit.default_timer()
    deretprima(y)  
    end = timeit.default_timer()
    print("n=",y,"rekursif ->", end-start,"second")
