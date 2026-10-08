def create_file():
    filename = input("Enter file name: ")
    try:
        file = open(filename, "w")
        file.close()
        print("File created successfully!")
    except:
        print("Error creating file")
def write_file():
    filename = input("Enter file name: ")
    data = input("Enter data to write: ")
    try:
        file = open(filename, "w")
        file.write(data)
        file.close()
        print("Data written successfully!")
    except:
        print("Error writing file")
def read_file():
    filename = input("Enter file name: ")
    try:
        file = open(filename, "r")
        data = file.read()
        file.close()
        print("File Content:")
        print(data)
    except:
        print("File not found!")
def append_file():
    filename = input("Enter file name: ")
    data = input("Enter data to append: ")
    try:
        file = open(filename, "a")
        file.write(data)
        file.close()
        print("Data appended successfully!")
    except:
        print("Error appending file")