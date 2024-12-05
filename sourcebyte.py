# Copy and Paste this code into a .py file

while True:
    global answer
    answer = input("Sourcebyte:> ")
    if (answer == "makefile"):
        ask = input("Enter the content: ")
        fileNew = open("documentation.html", "x")
        fileNew.write(ask)
        fileNew.close()
        print("File created.")
