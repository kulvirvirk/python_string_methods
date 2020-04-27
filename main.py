# 1. upper() - Call this method to return an upper case version of any string.
# 2. lower() - Call this method to return a lower case version of any string. 
# 3. provide comparision example using a .lower() method
# 4. islower() - call this method to check if string is lowercase or not
# 4. isupper() - call this method to check if string is uppercase or not

some_string = "Lorem ipsum dolor sit amet, an postulant conclusionemque eum. Ex deleniti pertinax est, mei probo euismod intellegebat at. Fierent indoctum vel cu. Qui graeci maiorum nominavi ei, ex nonumy ponderum duo. Atqui quidam mea te. Ius accusamus cotidieque at, et duo aliquip dolores, munere iudicabit expetendis eu his. Ignota delicatissimi pri ne, magna harum te est, cu eum laudem legendos."

# 1. upper() - Call this method to return an upper case version of any string.
print(some_string.upper())
print('===============================')

# note: the original string is still the same, 
print(some_string)
print('===============================')

# 2. lower() - Call this method to return a lower case version of any string. 
print(some_string.lower())
print('===============================')

# 3. provide comparison example using a .lower() method
'''user can enter any value(uppercase or lowercase) in form of input, logic should be able to compare it'''

user_input = input('Play again(Yes/No): ')
while user_input.lower() == 'yes':
  user_input = input('Play again(Yes/No): ')
print('Ok, bye!')
print('===============================')

# 4. islower() - call this method to check if string is lowercase or not
print (some_string.islower())
some_string = some_string.lower()
print (some_string.islower())
