import string

#cubes every number in the given list  list_1 = [1,2,3,4,5,6,7,8,9]
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cubed_list = list(map(lambda x: x**3, list_1))
print(cubed_list)



#Write a LC program to create an output dictionary which contains only the odd numbers that are present in the input list = [1,2,3,4,5,6,7] as keys and their cubes as values
input_list = [1, 2, 3, 4, 5, 6, 7]
output_dict = {x: x**3 for x in input_list if x % 2 != 0}
print(output_dict)


#Make a dictionary of the 26 english alphabets mapping each with the corresponding integer
alpha_dict = {char: idx+1 for idx, char in enumerate(string.ascii_lowercase)}
print(alpha_dict)

