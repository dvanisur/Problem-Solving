# 1.Write a function to check if a given number is prime.

# 0 or 1 isn't prime number
# 2 is prime number
# if that's number devidate by range of 2 and that's number and 
# modulus is 0 then isn't prime and 1 Is prime.

def is_prime (number):
    if number == 0 or number == 1:
        print(f"This {number} Number isn't prime number")
    elif number == 2 :
        print(f"This {number} number is a Prime Number")

    else:
        for numbers in range(2, number):
            if number % numbers == 0:
                check = " isn't"
            else:
                check ='is'
        print(f"This {number} number {check} Prime number")
is_prime(11)
