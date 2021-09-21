#Fibonachi Numbers
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        #print("n = ", n, " elem1 = ", elem1, " elem2 ", elem2, "sum ", sum)
        elem1, elem2 = elem2, sum
        #print("n = ", n, " elem1 = ", elem1, " elem2 ", elem2, "sum ", sum)   
    return sum

for n in range(1, 10): # testing
    print(n, "->", fib(n))