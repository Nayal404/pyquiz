import time 
def quiz():
    print('Welcome to the quiz game. There are 5 maths related questions mixed altogether.')
    print('Give the answers in words')
    score = 0
    userAns = int(input("What is the value of cos(360)° \n"))
    if userAns == 1:
        print('Correct Answer!🥳')
        score+=1
    else:
        print('Incorrect!😴')
    userAns = input('''What is the general term of the sequence :
     3, 6, 10, 15
     \n''')
    if userAns == '(n+1)(n+2)/2' or userAns == '(n+2)(n+1)/2':
        print('Correct Answer!🥳')
        score+=1
    else:
        print('Incorrect!😴')
    userAns = input("If matrix 'X' has order of 2x1 and matrix 'Y' has order of 1x2 so the result of XY is \n")
    if userAns == '2x2' or userAns == '2*2':
        print('Correct Answer!🥳')
        score+=1
    else:
        print('Incorrect!😴')
    time.sleep(1)
    print('''
=> Which of the following is pythagorus theorum?
(i) a+b+c = 180,         (iii) h² = p²+b²
(ii) sin(30+90) = cos30, (iv) an²+bn+c = 0
    ''')
    userAns = input('Answer it according to its numbering \n')
    if userAns == 'iii' or '3':
        print('Correct Answer!🥳')
        score+=1
    else:
        print('Incorrect!😴')
    userAns = int(input("if x = y/2 and y = 6, Then the value of x is \n"))
    if userAns == 3:
        print('Correct Answer!🥳')
        score+=1
    else:
        print('Incorrect!😴')
    time.sleep(1)
    print('Loading your results....')
    time.sleep(4)
    print(f'You got {score} questions correct out of 5.')
    percent = (score//5)*100
    print(f'You got a percentage of {percent}%')
if __name__ == "__main__":
    quiz()