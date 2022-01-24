from stack import MyStack

def mathcheck(string):
    s = MyStack()
    for i in string:
        if i == "{" or i == "[" or i == "(":
            s.push(i)
        elif i == "}" or i == "]" or i == ")":
           if s.is_empty():
               return False
           elif s.top() == "{" and i == "}":
               s.pop()
           elif s.top() == "[" and i == "]":
               s.pop()
           elif s.top() == "(" and i == ")":
               s.pop()
           else:
               return False

    if s.is_empty():
        return True
    else:
        return False

print(mathcheck("([2+4]+[5+6])"))
print(mathcheck("{"))
print(mathcheck(""))
print(mathcheck("}"))




