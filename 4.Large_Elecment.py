#4.Write a function to find the largest element in a list.
#[2,3,8,9,64,3]
#using sort finction for arrangement accending order
# Slicing the last number is large.

element_list = [1560,97,2,74,925,6,1,0,9]
element_list_new = sorted(element_list)
largest_number = element_list_new[-1]
print(largest_number)


#or usng max() function

largest_number_f= max(element_list)
print(largest_number_f)