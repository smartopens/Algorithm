while True:
    print("지금 무엇을 먹을지 정해드립니다.")
    print("먼저 먹고 싶은 음식의 느낌을 말해주세요.")
    print("1. 매운맛 2.달콤한 3.따듯한 4. 시원한")
    print("한글 부분만을 그대로 입력해주세요.")
    foodFeel = input("음식 느낌: ")

    print("이제 먹고 싶은 음식의 종류를 말해주세요.")
    print("1. 면 2.밥 3.패스트푸드")
    foodCategori = input("음식 종류: ")

    if foodFeel == "매운맛":
        if foodCategori == "면":
            print("짬뽕을 드셔보세요!")
        elif foodCategori == "밥":
            print("김치 볶음밥을 드셔보세요!")
        elif foodCategori == "패스트푸드":
            print("핫 치킨을 드셔보세요!")
    elif foodFeel == "달콤한":
        if foodCategori == "면":
            print("까르보나라를 드셔보세요!")
        elif foodCategori == "밥":
            print("짜장 볶음밥을 드셔보세요!")
        elif foodCategori == "패스트푸드":
            print("스노윙 치킨을 드셔보세요!")
    elif foodFeel == "따듯한":
        if foodCategori == "면":
            print("칼국수를 드셔보세요!")
        elif foodCategori == "밥":
            print("국밥을 드셔보세요!")
        elif foodCategori == "패스트푸드":
            print("맘스터치 햄버거를 드셔보세요!")
    elif foodFeel == "시원한":
        if foodCategori == "면":
            print("냉면을 드셔보세요!")
        elif foodCategori == "밥":
            print("초밥을 드셔보세요!")
        elif foodCategori == "패스트푸드":
            print("인절미 빙수를 드셔보세요!")

    print()