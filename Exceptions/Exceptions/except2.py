def func2():
    return 1/0

def func1():
    return func2()

print("aaaaaaaaa")
print("bbbbbbbbbb")
print("cccccccccc")
try:
    print(func1())
except:
    print("delenie na nol")
print("ddddddddd")
print("iiiiiiiii")
print("ffffffff")
print("gggggggg")