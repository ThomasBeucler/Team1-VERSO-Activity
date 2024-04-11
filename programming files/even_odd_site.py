# Bugs introduced:
# Changed if i % 2 == 0: to if i % 2 != 0:
# Changed file from numbers.html to numbers.png
with open("numbers.png", "w") as f:
    f.write("<html>\n<head>\n<title>List of Numbers</title>\n</head>\n<body>\n")
    f.write("<table>\n<tr><th>Even Numbers</th><th>Odd Numbers</th></tr>\n")
    for i in range(1, 50):
        #this is checking if the number is even 
        if i % 2 != 0:
            f.write("<tr><td>{}</td><td></td></tr>\n".format(i))
            #here is the odd number section
        else:
            f.write("<tr><td></td><td>{}</td></tr>\n".format(i))
    f.write("</table>\n</body>\n</html>")

with open("numbers.html", "r") as f:
    print(f.read())
    
