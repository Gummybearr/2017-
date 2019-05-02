'''
"퀴즈프로그램 ""Who wants to be a billionaire?""에서는 총 8개의 퀴즈를 내서 문제들을 모두 맞추는 출연자에게 100만달러를 지급한다. 문제는 가장 쉬운 문제부터 가장 어려운 문제의 순서로 제출되며, 가장 쉬운 문제의 정답율은 50%로, 난이도가 올라갈 때마다 정답율은 1/2로 감소한다. 도전상금은 100달러부터 시작하여 문제의 난이도가 올라갈 때마다 10배씩 올라간다. 그리고 출연자는 정답을 맞출 때 마다 다음단계로 나아갈지, 문제를 포기하고 지금까지의 상금을 가지고 집으로 돌아갈 지 결정할 수 있다. 문제를 맞추었을 때는 ""pass"", ""You have achieved 상금"",  ""Challenge or give up?""를 출력하고, 문제를 포기하였을 때는 ""You will walk away with 상금"", 문제를 틀렸을 경우에는 ""Fail"", ""Good-bye,"", 다른 문자를 입력했을 경우에는 ""Wrong
answer, Good-bye""를 출력하는 프로그램을 만들어라. 단, 마지막 문제를 맞추었을 때는 ""축하합니다. 당신은 billionaire""입니다.”라는 문구를 출력해야 한다. 또 ""Challenge"", ""challenge""를 입력받았을 때의 출력값과 ""GIve up"", ""give up"", ""Giveup"". ""giveup""을 입력받았을때의 출력값이 같아야 한다.
예) Welcome to “Who
wants to be a billionaire”
Challenge or Give
up?
출력)Challenge 
Pass
You have achieved
$100
Challenge or give up?
2017.10.15.16.44"
'''
print('Welcome to "Who wants to be a billionaire?"')
response = input("Challenge or giveup?")
price = 10
possibility = 1.0
number= 1
import random
for i in range(8):
    if response == "challenge":
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
    if response == "Challenge":
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
    elif response == "Giveup":
        if i == 0:
            print("You will walk away with $",0)
        else:
            print("You will walk away with $",price/(10))
        break
    elif response == "give up":
        if i == 0:
            print("You will walk away with $",0)
        else:
            print("You will walk away with $",price/(10))
        break
    elif response == "Give up":
        if i == 0:
            print("You will walk away with $",0)
        else:
            print("You will walk away with $",price/(10))
        break
    else:
        print("Wrong answer. Good-bye")
        break
