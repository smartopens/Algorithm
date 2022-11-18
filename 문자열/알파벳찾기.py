from string import ascii_lowercase

alphaList = ("a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
             "s","t","u","v","w","x","y","z")

problem = input()

for a in alphaList:
    if a in problem:
        print(problem.find(a), end = " ")
    else:
        print(-1, end = " ")