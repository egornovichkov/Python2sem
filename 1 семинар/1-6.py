def bracket_check(string):
    brackets = []

    for symb in string:
        if symb == "(":
            brackets.append("(")
        elif symb == ")":
            if len(brackets) == 0 or brackets[-1] != "(":
                return "NO"
            brackets.pop()

    if len(brackets) == 0:
        return "YES"
    else:
        return "NO"

def bracket_create(length):
    brackets = []
    for i in range(2 ** length):
        s = ""
        for j in range(length):
            s = str(i % 2) + s
            i = i // 2
        brackets.append(s)
    for i in range(2 ** length):
        brackets[i] = brackets[i].replace("0", "(")
        brackets[i] = brackets[i].replace("1", ")")
    return brackets

length = int(input())
brackets = bracket_create(length)
for i in range(2 ** length):
    if bracket_check(brackets[i]) == "YES":
        print(brackets[i])
