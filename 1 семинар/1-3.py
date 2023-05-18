def bracket_check(test_string):
    brackets = []

    for symb in test_string:
        if symb == "(":
            brackets.append("(")
        elif symb == ")":
            if len(brackets) == 0 or brackets[-1] != "(":
                print("NO")
                return
            brackets.pop()

    if len(brackets) == 0:
        print("YES")
    else:
        print("NO")