
def main():
    print("Hello World")
    data = input()

    dataArray = data.split(" ")

    print(" name: " + dataArray[0] + " surname: " + dataArray[1] + " year: " + dataArray[2])

    #=========================================ZAMEK SZYFROWY==================================================
    key = 1234
    i = 0
    for i in range(0, 3):
        data = input("Enter key(" + str((3-i)) + " attemps left):")
        if int(data) == key:
            print("Success")
            return
        else:
            print("Try again")
    print("Too many failures")

if __name__ == '__main__':
    main()