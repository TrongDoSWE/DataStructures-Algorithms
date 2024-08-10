# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
print("Input max number: ")
max = int(input())

list_of_odd_numbers = []
for i in range(max):
    if i % 2 != 0:
        list_of_odd_numbers.append(i)

print("The list of all odd numbers between 1 and", max, ":", list_of_odd_numbers)