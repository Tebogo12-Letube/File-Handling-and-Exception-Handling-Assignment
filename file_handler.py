import os

def read_and_modify_file():
    try:
        filename = input("Enter the filename to read: ")

        if not os.path.exists(filename):
            raise FileNotFoundError("Error: File does not exist.")

        with open(filename, "r") as file:
            content = file.readlines()

        modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(content)]

        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.writelines(modified_content)

        print(f"Modified content saved to {new_filename}")

    except FileNotFoundError as e:
        print(e)
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

read_and_modify_file()
