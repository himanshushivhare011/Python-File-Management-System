from pathlib import Path

def read_file_and_folder():
    path = Path('.')   # current directory
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")

def createfile():
    try:
        read_file_and_folder()
        name = input("please tell me your file name : ")
        p = Path(name)

        if not p.exists():
            with open(p, "w") as fs:
                data = input("what you want to write in file : ")
                fs.write(data)
            print("file created successfully")
        else:
            print("this file already exists")

    except Exception as err:
        print(f"an error occurs: {err}")

def readfile():
    try:
        read_file_and_folder()
        name = input("which file do you want to read : ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, "r") as fr:
                data = fr.read()
                print(data)
            print("successfully read")
        else:
            print("the file does not exist")

    except Exception as err:
        print(f"an error occurs: {err}")

def update():
    try:
        read_file_and_folder()
        name = input("Tell me the file name for update : ")
        p = Path(name)

        if p.exists() and p.is_file():
            print("press 1 for changing the name of file")
            print("press 2 for overwriting the data of your file")
            print("press 3 for appending some content in your file")

            res = int(input("enter your response : "))

            if res == 1:
                newname = input("enter new name : ")
                p.rename(Path(newname))
                print("file renamed successfully")

            elif res == 2:
                with open(p, 'w') as fs:
                    data = input("enter data to overwrite the file : ")
                    fs.write(data)
                print("file overwritten successfully")

            elif res == 3:
                with open(p, 'a') as fs:
                    data = input("enter the data to append : ")
                    fs.write(f"\n{data}")
                print("data appended successfully")

            else:
                print("invalid choice")
        else:
            print("file does not exist")

    except Exception as err:
        print(f"error is: {err}")
        
def delete():
  try:
    read_file_and_folder()
    name=input("enter the name of file for deletion :")
    p=Path(name)
    if p.exists() and p.is_file():
        p.unlink()
        print("file deleted successfully")
    else:
        print("file does not exist")
  except Exception as err:
    print(f"the file has some error {err}")

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for delete a file")

check = int(input("Enter the number for operation : "))

if check == 1:
    createfile()
elif check == 2:
    readfile()
elif check == 3:
    update()
elif check == 4:
    delete()