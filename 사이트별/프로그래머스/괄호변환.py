def isRight(sen):
    sentence = list(sen)
    checkList = list()

    for sen in sentence:
        if sen == "(":
            checkList.append("(")
        else:
            if checkList:
                checkList.pop()
            else:
                return False

    if checkList:
        return False
    else:
        return True


def testUV(sen):
    if sen == "":
        return ""

    fSen = sen[0]
    sameCnt = 0
    u = ""
    v = ""
    idx = 0

    for s in sen:
        if s == fSen:
            sameCnt += 1
            u += s
        else:
            sameCnt -= 1
            u += s

        if sameCnt == 0:
            v = sen[idx + 1:]
            if isRight(u):
                u += testUV(v)
                return u
            else:
                newSentence = "("
                newSentence += testUV(v)
                newSentence += ")"

                u = u[1:]
                u = u[:-1]
                uReversed = ""
                for i in u:
                    if i == "(":
                        uReversed += ")"
                    else:
                        uReversed += "("

                return newSentence + uReversed
        idx += 1


def solution(p):
    answer = ''

    if isRight(p):
        return p
    answer = testUV(p)

    return answer