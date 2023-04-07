# wirte file
data = "hello"
with open("test.txt", "w") as fp:
    fp.write(data)

# read file
with open("test.txt", "r") as fp:
    print("=========[result of read file]=======")
    print(fp.read())