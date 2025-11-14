try:
    with open("students.txt", "r") as file:
        data = file.read()
        print("Contents of students.txt:")
        print(data)

except FileNotFoundError:
    print("Error: students.txt file not found.")

except PermissionError:
    print("Error: You don't have permission to read this file.")

except Exception as e:
    print("An unexpected error occurred:", e)
