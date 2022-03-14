signalNum = int(input())
signal = list(input())
lineNum = signalNum // 5
result = list()
idx = 0
nextIdx = 0

while idx <= lineNum - 1:
    if idx >= lineNum:
        break

    if signal[idx] == "#":
        if idx + 1 >= lineNum:
            result.append(1)
            idx += 2
            continue

        # 1,4 case
        if signal[idx + 1] == ".":
            nextIdx = idx + lineNum*3

            # 1 case
            if signal[nextIdx] == "#":
                result.append(1)
                idx += 2
                continue

            # 4 case
            elif signal[nextIdx] == ".":
                result.append(4)
                idx += 4
                continue

        # 0,2,3,5,6,7,8,9 case
        elif signal[idx + 1] == "#" and signal[idx + 2] == "#":
            nextIdx = idx + lineNum

            # 0,8,9 case
            if signal[nextIdx] == "#" and signal[nextIdx + 1] == "." and signal[nextIdx + 2] == "#":
                nextIdx += lineNum

                if signal[nextIdx] == "#" and signal[nextIdx + 1] == "." and signal[nextIdx + 2] == "#":
                    result.append(0)
                    idx += 4
                    continue

                elif signal[nextIdx] == "#" and signal[nextIdx + 1] == "#" and signal[nextIdx + 2] == "#":
                    nextIdx += lineNum

                    if signal[nextIdx] == "#" and signal[nextIdx + 1] == "." and signal[nextIdx + 2] == "#":
                        result.append(8)
                        idx += 4
                        continue

                    elif signal[nextIdx] == "." and signal[nextIdx + 1] == "." and signal[nextIdx + 2] == "#":
                        result.append(9)
                        idx += 4
                        continue

            # 2,3,7 case
            elif signal[nextIdx] == "." and signal[nextIdx + 1] == "." and signal[nextIdx + 2] == "#":
                nextIdx += lineNum

                if signal[nextIdx] == "." and signal[nextIdx + 1] == "." and signal[nextIdx + 2] == "#":
                    result.append(7)
                    idx += 4
                    continue

                elif signal[nextIdx] == "#" and signal[nextIdx + 1] == "#" and signal[nextIdx + 2] == "#":
                    nextIdx += lineNum

                    if signal[nextIdx] == "#" and signal[nextIdx + 1] == "." and signal[nextIdx + 2] == ".":
                        result.append(2)
                        idx += 4
                        continue

                    elif signal[nextIdx] == "." and signal[nextIdx + 1] == "." and signal[nextIdx + 2] == "#":
                        result.append(3)
                        idx += 4
                        continue

            # 5,6 case
            elif signal[nextIdx] == "#" and signal[nextIdx + 1] == "." and signal[nextIdx + 2] == ".":
                nextIdx += lineNum * 2

                if signal[nextIdx] == "." and signal[nextIdx + 1] == "." and signal[nextIdx + 2] == "#":
                    result.append(5)
                    idx += 4
                    continue

                elif signal[nextIdx] == "#" and signal[nextIdx + 1] == "." and signal[nextIdx + 2] == "#":
                    result.append(6)
                    idx += 4
                    continue
    idx += 1

for i in result:
    print(i, end="")