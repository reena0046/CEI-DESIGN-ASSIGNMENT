#Q2. Create a program that takes user input to add multiple elements to an array, then prints the final array. 


numbers = []
num_elements = int(input("How many numbers do you want to add to the array? "))
for _ in range(num_elements):
    new_number = int(input("Enter a number: "))
    numbers.append(new_number)
print("Final array:", numbers)


