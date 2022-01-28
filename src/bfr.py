import os

def main():
    i = 0
    path = input("Input the path: ")
    filename = input("Input the filename: ")
    for filename in os.listdir(path):
        myDest = "file" + str(i) + filename
        mySource = path + filename
        myDest = path + myDest
        os.rename(mySource, myDest)
        i += 1
if __name__ == "__main__":
    main()
