# You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
print("The given list:", heros)

# Using this find out:

# 1. Length of the list
print("Length of the list: ", len(heros))

# 2. Add 'black panther' at the end of this list
heros.append("black panther")
print("The list after adding 'black panther':", heros)

# 3. You realize that you need to add 'black panther' after 'hulk'
#    so remove it from the list first and then add it after 'hulk'
heros.pop()
heros.insert(3, "black panther")
print("The list after adding 'black panther':", heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
print("The list after removing 'thor' and 'hulk':", heros[:1] + ["doctor strange"] + heros[3:])


# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
# print(dir(heros))
heros[1:3] = ["doctor strange"]
heros.sort()
print("The sorted list:", heros)