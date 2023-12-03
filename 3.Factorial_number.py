#3.Create a program to calculate the factorial of a given number.
# 5!=5*4*3*2*1
# Negetive number doesn't existfor factorial number
# 0 and 1 factorial is 1
# use for loop in range function from 1 to given number+1 and multipy them
 
def factorial_number(n):
   
    if n < 0 :
        print(f"Sorry, Factorial doesn't exist for {n} negative number")

    elif n == 0 :
        print(f"{n} factorial is 1 ")
    else:
        f = 1
        for i in range(1, n+1 ):  
            f = f*i
        print(f)          
            
factorial_number(1)

