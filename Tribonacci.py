# Function that returns nth element of tribonacci sequence

def tri(signature, n):
    
    if n == 0:
        return []
    
    next_tri = 0
    #0, 0, 1, 1, 2, 4, 7, 13, ...
    #p, p, c, n
       #p, p, c, n
    
    lst = []
    print("Starting terms for Tribonacci sequence are:", signature)
    for i in range(n):
      #print(signature[0])
      lst.append(signature[0])
      next_tri = signature[0] + signature[1] + signature[2]
      signature[0] = signature[1]
      signature[1] = signature[2]
      signature[2] = next_tri
    
    return "The first " + str(n) + " terms of the Tribonacci sequence are: " + str(lst)

print(tri([0,0,1],15))

file = open("FibonacciLog.txt", "w") # if file is not already there it will make it auto
file.write(str(tri([0,0,1],15)))
file.close()

# for n in range(1,11):
#     newline = "This is line " + str(n) + "\n"
#     file.write(newline)
    
