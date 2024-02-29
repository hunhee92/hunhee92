import random
htry_count = 0

while True:
    ran_num = random.randint(1, 10)
    try_count = 1
    while True:

        user_num = int(input("1~100까지의 숫자를 입력 : "))
        try:
            if 1 > user_num or user_num > 100:
                print("1~100까지의 숫자를 입력해 주세요.")

            elif user_num > ran_num:
                print("다운!")
                try_count += 1

            elif user_num < ran_num:
                print("업!")
                try_count += 1

            elif user_num == ran_num:
                print("정답입니다!")
                if htry_count < try_count:
                    htry_count = try_count
                    print(f"시도 횟수: {try_count}")
                    conti = input("게임을 계속 할까요? y / n")
                else:
                    print(f"이전 게임 최고시도 횟수 :{htry_count}")
                    conti = input("게임을 계속 할까요? y / n")

                if conti == "y":

                    break
                else:

                    exit()

        except ValueError:
            print("숫자만 입력해 주세요")
