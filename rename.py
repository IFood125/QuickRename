import os

def main():
    extension = input("Enter extension(Ex pdf or leave empty for all files): ")
    if extension:
        extension = "." + extension
    count = 1
    baseName= input("Enter default string: ")
    while(not baseName):
        baseName= input("Enter default string: ")
    cwd = os.getcwd()
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        oldExtension = os.path.splitext(f)[1]
        fileName = baseName + str(count) + oldExtension
        if not extension and oldExtension != ".py":
            os.rename(os.path.join(cwd, f), fileName) 
        elif extension == oldExtension:
            os.rename(os.path.join(cwd, f), fileName) 
        count+=1

if __name__ == "__main__":
    main()
