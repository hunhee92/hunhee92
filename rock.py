import random
# - 가위 바위 보 게임 ROCK, PAPER, SCISSORS
# - 플레이어가 가위, 바위, 보 중 하나를 입력합니다.
# - 컴퓨터도 무작위로 가위, 바위, 보 중 하나를 선택합니다.
# - 플레이어와 컴퓨터의 선택을 비교하여 승패를 판정합니다.
# - 결과를 출력하여 플레이어가 이겼는지, 컴퓨터가 이겼는지, 비겼는지를 알려줍니다.
# - 게임을 반복하거나 종료할 수 있는 기능을 추가하세요.

# **추가 도전 과제:**

# 1. 게임의 승, 패, 무승부 횟수를 기록하고, 게임 종료 시에 플레이어에게 통계를 제공하세요.
# 2. 플레이어가 입력할 때 대소문자를 구분하지 않도록 프로그램을 개선하세요.
# 3. 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요.

wdl = [0, 0, 0]

while True:

    user_num: 0

    while True:

        ran_rock = random.randint(1, 3)

        user = input("무엇을 내시겠습니까(ROCK, PAPER, SCISSORS): ").lower()

        if user == "rock":
            user_num = 1  # 1, 3

        elif user == "paper":
            user_num = 2  # 2 ,1

        elif user == "scissors":
            user_num = 3  # 3 ,2

        else:
            print("잘못 입력 하셨습니다. ROCK, PAPER, SCISSORS 중에 하나를 입력 해주세요")
            continue

        if user_num == ran_rock:
            print("비겼습니다.")
            wdl[1] += 1
        elif (user_num == 1 and ran_rock == 3) or (user_num == 2 and ran_rock == 1) or (user_num == 3 and ran_rock == 2):
            print("이겼습니다.")
            wdl[0] += 1

        else:
            print("졌습니다.")
            wdl[2] += 1

        
            conti = input("게임을 계속 하시겠습니까? (y/n): ").lower()

            if conti == "y":
                continue
            elif conti == "n":
                print(f"승: {wdl[0]}, 무: {wdl[1]}, 패: {wdl[2]}")
                exit()
            else:
                print("잘못 입력 하셨습니다. 게임을 종료합니다")
                exit()
