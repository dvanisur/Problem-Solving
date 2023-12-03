#2. Implement a function to reverse a string without using built-in reverse functions.

#Define the string to be reversed
#slice the  string from the last character to first
#Print the reverse_str

def reverse_str (my_str):
    new_stn = my_str [: :-1]
    print(new_stn)

reverse_str('raju')