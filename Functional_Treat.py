#Functional Treat

def welcome():
    print("=" * 60)
    print("Welcome to the Data Analyzer and Transformer Program")
    print("=" * 60)

def menu():

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")


# Input Data Function

def input_data():

    user_input = input("Enter data for a 1D array (separated by spaces):\n")

    data = list(map(int, user_input.split()))

    print("\nData has been stored successfully!")

    return data

# Display Summary Function

def display_summary(*args, **kwargs):

    global summary

    if len(args) == 0 or len(args[0]) == 0:
        print("No data available!")
        return

    data = args[0]

    summary = {
        "Total elements": len(data),
        "Minimum value": min(data),
        "Maximum value": max(data),
        "Sum of all values": sum(data),
        "Average value": round(sum(data) / len(data), 2)
    }

    print("\nData Summary:")

    for key, value in summary.items():
        print(f" {key}: {value}")

    if kwargs:
        print("\nAdditional Characteristics:")

        for key, value in kwargs.items():
            print(f"{key}: {value}")


# Factorial Function (Recursion)

def factorial(n):

    if n < 0:
        return "Factorial is not defined for negative numbers."

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

# Filter Data Function (Lambda)

def filter_data(data):

    if len(data) == 0:
        print("No data available!")
        return

    limit = int(input("\nEnter a threshold value to filter out data above this value:\n"))

    new_data = list(filter(lambda x: x >= limit, data))

    print(f"\nFiltered Data (values >= {limit}):")

    if len(new_data) == 0:
        print("No values found.")
    else:
        print(", ".join(map(str, new_data)))


# Sort Data Function

def sort_data(data):

    if len(data) == 0:
        print("No data available!")
        return

    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = input("\nEnter your choice: ")

    temp = data.copy()

    if choice == "1":
        temp.sort()
        print("\nSorted Data in Ascending Order:")

    elif choice == "2":
        temp.sort(reverse=True)
        print("\nSorted Data in Descending Order:")

    else:
        print("Invalid choice!")
        return

    print(", ".join(map(str, temp)))


# Dataset Statistics Function

def dataset_statistics(data):

    if len(data) == 0:
        return None, None, None, None

    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = round(total / len(data), 2)

    return minimum, maximum, total, average

# ---------------- Main Program ----------------

data = []

welcome()

while True:

    menu()

    choice = input("\nPlease enter your choice: ")

    if choice == "1":

        print("\n1: Input Data")

        data = input_data()

    elif choice == "2":

        print("\n2: Display Data Summary (Built-in Functions)")

        display_summary(
            data,
            dataset_type="1D Array",
            status="Active"
        )

    elif choice == "3":

        print("\n3: Calculate Factorial (Recursion)")

        number = int(input("Enter a number to calculate its factorial: "))

        answer = factorial(number)

        print(f"\nFactorial of {number} is: {answer}")

    elif choice == "4":

        print("\n4: Filter Data by Threshold (Lambda Function)")

        filter_data(data)

    elif choice == "5":

        print("\n5: Sort Data")

        sort_data(data)

    elif choice == "6":

        print("\n6: Display Dataset Statistics (Return Multiple Values)")

        minimum, maximum, total, average = dataset_statistics(data)

        if minimum is not None:

            print("\nDataset Statistics:")
            print(f" Minimum value: {minimum}")
            print(f" Maximum value: {maximum}")
            print(f" Sum of all values: {total}")
            print(f" Average value: {average}")

        else:
            print("No data available!")

    elif choice == "7":

        print("\n7: Exit Program")
        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")

        break

    else:

        print("\nInvalid choice! Please try again.")
