# 1. count()  - call t his method to count specific char in string
# 2. upper() - Call this method to return an upper case version of any string.
# 3. lower() - Call this method to return a lower case version of any string. 
# 4. provide comparision example using a .lower() method
# 5. islower() - call this method to check if string is lowercase or not
# 6. isupper() - call this method to check if string is uppercase or not


some_string = "Lorem ipsum dolor sit amet, an postulant conclusionemque eum. Ex deleniti pertinax est, mei probo euismod intellegebat at. Fierent indoctum vel cu. Qui graeci maiorum nominavi ei, ex nonumy ponderum duo. Atqui quidam mea te. Ius accusamus cotidieque at, et duo aliquip dolores, munere iudicabit expetendis eu his. Ignota delicatissimi pri ne, magna harum te est, cu eum laudem legendos."

# 1. count()  - call t his method to count specific char in string
print('there are ' + str(some_string.count('a')) + '\'a\'found in given text')
print('===============================')

# 2. upper() - Call this method to return an upper case version of any string.
print(some_string.upper())
print('===============================')

# note: the original string is still the same, 
print(some_string)
print('===============================')

# 3. lower() - Call this method to return a lower case version of any string. 
print(some_string.lower())
print('===============================')

# 4. provide comparison example using a .lower() method
'''user can enter any value(uppercase or lowercase) in form of input, logic should be able to compare it'''

user_input = input('Play again(Yes/No): ')
while user_input.lower() == 'yes':
  user_input = input('Play again(Yes/No): ')
print('Ok, bye!')
print('===============================')

# 5. islower() - call this method to check if string is lowercase or not
print (some_string.islower())
 #now change the string to lowercase using the lower() method
some_string = some_string.lower()
 #check again
print (some_string.islower())
print('===============================')

# 6. isupper() - call this method to check if string is uppercase or not
print (some_string.isupper())
 #now change the string to uppercase using the upper() method
some_string = some_string.upper()
 #check again
print (some_string.isupper())
print('===============================')



