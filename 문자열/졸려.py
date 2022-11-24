x = int(input())
word = input()
word_len = len(word)
idx = 0
is_even = True

ori_word = word
t_i = 0

if word_len % 2 == 0:
    idx = word_len//2
else:
    idx = word_len//2 + 1
    is_even = False

while True:
    new_word = ""
    second_word = word[idx:]
    se_len = len(second_word)

    for i in range(idx):
        new_word += word[i]
        if not is_even and i == idx -1:
            break
        new_word += second_word[se_len-i-1]
    t_i += 1

    word = new_word
    if ori_word == word:
        break


x = x % t_i
word = ori_word

for j in range(x):
    first_word = ""
    second_word = ""

    for i in range(0,word_len,2):
        first_word += word[i]
        if not is_even and i == word_len -1:
            break
        second_word = word[i+1] + second_word

    word = first_word + second_word

print(word)