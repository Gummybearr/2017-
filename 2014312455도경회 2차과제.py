#1번문제 Who wants to be a millionaire?
print('Welcome to "Who wants to be a billionaire?"')
response = input("Challenge or giveup?")
price = 10
possibility = 1.0
number= 1
import random
for i in range(8):
    if response == "challenge" and "Challenge":
        price *=10
        number = number*2
        possibility = possibility/number
        challenge = random.random()
        if challenge <= possibility:
            if i == 7:
                print("Congratulations, you are a billionaire!")
            else:
                print("Pass")
                print("You have achieved $",price)
                response = input("Challenge or give up?")
        else:
            print("Fail")
            print("Good-bye")
            break
    elif response == "giveup":
        if i == 0:
            print("You will walk away with $",0)
        else:
            print("You will walk away with $",price/(10))
        break
    else:
        print("Wrong answer. Good-bye")
        break

#2번문제 학번과 입력을 2차원으로 출력해주는 프로그램
identification = []
while True:
    hakbun = input('학번을 입력하세요: ')
    if hakbun =='exit':
        for i in range(len(identification)):
            print('학번은',identification[i][0],'이고','이름은',identification[i][1],'입니다.')
            if i == len(identification):
                print('학번은',identification[i][0],'이고','이름은',identification[i][1],'입니다.')
                break
        break
    else:
        name= input('이름을 입력하세요: ')
        identification.append([hakbun, name])
