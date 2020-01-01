# Basic Calculator program
# prompt the user for inputs

def welcome():
        details = input(" \nWelcome, what is your name ? :")
        print(details, ",", "this a basic calculator with 4 operations: \n")
        print(
            "1. Addition \n"
            "2. Substraction \n"
            "3. Multiplication \n"
            "4. Division \n")
        welcome()


# operations
def add(num_1, num_2):
    return num_1 + num_2


def sub(num_1, num_2):
    return num_1 - num_2


def multiply(num_1, num_2):
    return num_1 * num_2


def divide(num_1, num_2):
    return num_1 / num_2


# take user selection
choice = input(" Please select 1,2,3 or 4\n \n")

first_number = int(input('Please enter your first number'))

second_number = int(input('Please enter your second number'))

# format the output

if choice == '1':
    print("The answer is : \n", '{} + {} = '.format(first_number, second_number), add(first_number, second_number))

elif choice == '2':
    print("The answer is : \n", '{} - {} = '.format(first_number, second_number), sub(first_number, second_number))

elif choice == '3':
    print("The answer is : \n", '{} * {} = '.format(first_number, second_number), multiply(first_number, second_number))

elif choice == '4':
    print("The answer is : \n", '{} / {} = '.format(first_number, second_number), divide(first_number, second_number))

else:
    print('Invalid Entry')

