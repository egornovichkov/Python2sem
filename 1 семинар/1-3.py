def bracket_check(string):
    brackets = []

    for symb in string:
        if symb == "(":
            brackets.append("(")
        elif symb == ")":
            if len(brackets) == 0 or brackets[-1] != "(":
                print("NO")
            brackets.pop()

    if len(brackets) == 0:
        print("YES")
    else:
        print("NO")