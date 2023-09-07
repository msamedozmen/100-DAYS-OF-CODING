
with open("myfile.txt",mode="r") as f:
    cont = f.read()




with open("myfile.txt",mode="w") as f:
    f.write("abc")


with open("myfile1.txt",mode="a") as fs:
    fs.write("asfasfsafaaaaaaaaaaaaa\n")
    fs.write("131")