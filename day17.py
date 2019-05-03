inp1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
inp2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

def countlines(string):
    print(string)
    c = 0
    for char in string:
        if char == '\t':
            c += 1
    return c

def getFS(inp):
    s = inp.split('\n')

    for x in s:
        count = countlines(x)
        if "." in x:
            print(len(x))

print(getFS(inp1))
