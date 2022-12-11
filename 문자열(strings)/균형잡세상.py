while True:
    sentence = input()
    smallOk = True
    BigOk = True
    small = []
    big = []

    if sentence[0] == ".":
        break

    sentence.replace(".","")
    for s in sentence:
        if s == "(":
            small.append("(")
        elif s == "[":
            small.append("[")
        elif s == "]":
            if small and small[-1] == "[":
                small.pop()
            else:
                smallOk = False
        elif s == ")":
            if small and small[-1] == "(":
                small.pop()
            else:
                smallOk = False

    if small:
        smallOk = False

    if smallOk:
        print("yes")
    else:
        print("no")

