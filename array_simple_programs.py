def find_largest_number():
    try:
        numbers = list(map(int, input("Enter numbers separated by space: ").split()))
        if not numbers:
            print("List is empty.")
            return
        largest = numbers[0]
        for num in numbers:
            if num > largest:
                largest = num
        print("The largest number is:", largest)
    except ValueError:
        print("Invalid input. Please enter integers only.")

def count_even_numbers():
    try:
        numbers = list(map(int, input("Enter numbers separated by space: ").split()))
        even_count = sum(1 for num in numbers if num % 2 == 0)
        print("Count of even numbers:", even_count)
    except ValueError:
        print("Invalid input. Please enter integers only.")

def remove_duplicates():
    try:
        numbers = list(map(int, input("Enter numbers separated by space (with duplicates): ").split()))
        unique_numbers = list(set(numbers))
        print("List without duplicates:", unique_numbers)
    except ValueError:
        print("Invalid input. Please enter integers only.")

def reverse_list():
    try:
        numbers = list(map(int, input("Enter numbers separated by space: ").split()))
        reversed_numbers = []
        for i in range(len(numbers) - 1, -1, -1):
            reversed_numbers.append(numbers[i])
        print("Reversed list:", reversed_numbers)
    except ValueError:
        print("Invalid input. Please enter integers only.")

def sort_list():
    try:
        numbers = list(map(int, input("Enter numbers separated by space: ").split()))
        numbers.sort()
        print("Sorted list:", numbers)
    except ValueError:
        print("Invalid input. Please enter integers only.")

def list_comprehension_squares():
    try:
        n = int(input("Enter how many squares to generate: "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return
        squares = [x**2 for x in range(1, n + 1)]
        print("Squares:", squares)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def main_menu():
    while True:
        print("\n--- MENU ---")
        print("1. Find the largest number in a list")
        print("2. Count even numbers in a list")
        print("3. Remove duplicates from a list")
        print("4. Reverse a list (without reverse())")
        print("5. Sort a list")
        print("6. List comprehension: Squares")
        print("7. Exit")

        choice = input("Enter your choice (1-7 or 'exit'): ").strip()

        if choice == "1":
            find_largest_number()
        elif choice == "2":
            count_even_numbers()
        elif choice == "3":
            remove_duplicates()
        elif choice == "4":
            reverse_list()
        elif choice == "5":
            sort_list()
        elif choice == "6":
            list_comprehension_squares()
        elif choice == "7" or choice.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
