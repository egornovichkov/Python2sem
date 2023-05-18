def calculate_expression(expression, values):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []

    
    for symb in expression:
        if symb.isalpha():
            output.append(str(values[symb]))
        elif symb in operators:
            while stack and stack[-1] != '(' and operators[symb] <= operators.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(symb)
expression = input()
values = []
while True:
    k = input
    if k == 'quit':
        break
    else:
        values.append(k)
