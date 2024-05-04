import random
wins = 0
lose = 0


def rps(wins, lose):

    r = ['ROCK', 'PAPER', 'SCISSORS']
    npc = random.choice(r)
    ans = ''
    a = int(input('CHOOSE QUICKLY\n'
                  '1) ROCK\n'
                  '2) PAPER\n'
                  '3) SCISSORS\n\n'))
    if a == 1:
        ans += 'ROCK'
        if ans == npc:
            print('TIE, AGAIN!!')
        elif ans != npc:
            if npc == 'PAPER':
                print('YOU LOSE, AGAIN!!')
                lose += 1
            elif npc == 'SCISSORS':
                print('YOU WIN, AGAIN!!')
                wins += 1
        print(f'wins: {wins}\nloses: {lose}\n')
        rps(wins, lose)

    elif a == 2:
        ans += 'PAPER'
        if ans == npc:
            print('TIE, AGAIN!!')
        elif ans != npc:
            if npc == 'SCISSORS':
                print('YOU LOSE, AGAIN!!')
                lose += 1
            elif npc == 'ROCK':
                print('YOU WIN, AGAIN!!')
                wins += 1
        print(f'wins: {wins}\nloses: {lose}\n')
        rps(wins, lose)

    elif a == 3:
        ans += 'SCISSORS'
        if ans == npc:
            print('TIE, AGAIN!!')
        elif ans != npc:
            if npc == 'ROCK':
                print('YOU LOSE, AGAIN!!')
                lose += 1
            elif npc == 'PAPER':
                print('YOU WIN, AGAIN!!')
                wins += 1
        print(f'wins: {wins}\nloses: {lose}\n')
        rps(wins, lose)

    else:
        print('Invalid answer')
        rps(wins, lose)


rps(wins, lose)




