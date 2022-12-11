n = int(input())
short_key_set = set()

for _ in range(n):
    words = input().split()
    first_done, second_done = False, False
    new_words = []
    idx = 0

    for word in words:
        if not first_done and word[0].lower() not in short_key_set:
            new_words.append("[")
            new_words.append(word[0])
            new_words.append("]")
            for i in word[1:]:
                new_words.append(i)

            short_key_set.add(word[0].lower())
            first_done = True
        else:
            for i in word:
                new_words.append(i)

        if idx == len(words)-1:
            break
        new_words.append(" ")
        idx += 1

    idx = 0
    if first_done:
        print(''.join(new_words))

    if not first_done:

        new_words = []
        for word in words:
            for i in word:
                if not second_done and i.lower() not in short_key_set:
                    short_key_set.add(i.lower())
                    second_done = True
                    new_words.append("[")
                    new_words.append(i)
                    new_words.append("]")
                else:
                    new_words.append(i)

            if idx == len(words) - 1:
                break
            new_words.append(" ")
            idx += 1

        print(''.join(new_words))
