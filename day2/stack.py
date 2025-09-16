
def insert(stack, elem):
    stack.append(elem)

def remove(stack):
    return stack.pop()


stack = []

f = open("seq.txt")

for line in f:
    line = line.split()
    if line[0] == "insert":
        insert(stack, line[1])
    elif line[0] == "remove":
        elem = remove(stack)
        print("popped", elem)
    print(stack)
