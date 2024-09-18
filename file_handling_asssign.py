# file_handling_assignment.py

# File Creation and Writing
def write_to_file():
    try:
        # Create a new file 'my_file.txt' in write mode
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("This is line 2 with a number: 42\n")
            file.write("This is line 3\n")
        print("File 'my_file.txt' created and written successfully.")
    except PermissionError:
        print("Permission denied: Unable to write to file.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# File Reading and Display
def read_from_file():
    try:
        # Open and read the content of 'my_file.txt'
        with open("my_file.txt", "r") as file:
            content = file.read()
        print("\nReading from 'my_file.txt':\n")
        print(content)
    except FileNotFoundError:
        print("File not found: Please create the file first.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

# File Appending
def append_to_file():
    try:
        # Open 'my_file.txt' in append mode and add more lines
        with open("my_file.txt", "a") as file:
            file.write("This is line 4 appended\n")
            file.write("This is line 5 appended with another number: 100\n")
            file.write("This is line 6 appended\n")
        print("\nContent successfully appended to 'my_file.txt'.")
    except FileNotFoundError:
        print("File not found: Unable to append to the file.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

# Main function to handle file operations
def main():
    write_to_file()  # Step 1: Write to file
    read_from_file()  # Step 2: Read and display file contents
    append_to_file()  # Step 3: Append to the file
    read_from_file()  # Step 4: Read again to show updated content

# Execute the main function
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nFile operations completed.")

