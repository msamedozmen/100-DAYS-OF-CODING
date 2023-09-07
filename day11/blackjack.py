import random
Welcome = input("Do u wanna play a game of BlackJack (y/n)").lower()

if Welcome== "n":
    print("See u later")
    quit
    
cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]
def player_scor(p_score,p_hand):
    if p_hand[0]==11 and p_hand[1] == 11:
        p_hand[1] = 1
        for i in range(0,len(p_hand)):
            p_score += p_hand[i]
        print(f"Your cards: {p_hand}, current score: {p_score}")
    else:
        for i in range(0,len(p_hand)):
            p_score = p_score + p_hand[i]
        print(f"Your cards: {p_hand}, current score: {p_score}")
    return p_score
def final(player,computer):
    if player >21 and computer<22:
            print("You went over. You lose")
    elif player <22 and computer>21:
        print("Computer went over. You win")

    elif player > computer:
        print("You win")
    else:
        print("You lose")
def blackjack():
    computer_score =0
    player_hand = random.sample(cards,2)
    player_score=0
    player_score=player_scor(player_score,player_hand)
    computer_hand = random.sample(cards,1)
    comp_hand = computer_hand[0]
    print(f"Computer's first card: {comp_hand}")
    second_card = random.sample(cards,1)
    
    while player_score<17:
        next_card_ask= input("Type'y' to get another card, type 'n' to pass ").lower()
        if next_card_ask == 'y':
            new_player_card = random.sample(cards,1)
            player_hand.append(new_player_card[0])
            if new_player_card[0]==11:
                if player_score + new_player_card[0] >21:
                    player_score = player_score +1
                    print(f"Your cards: {player_hand}, current score: {player_score}")
                else:
                    player_score = player_score + new_player_card[0]
                    print(f"Your cards: {player_hand}, current score: {player_score}")
            else:
                player_score = player_score + new_player_card[0]
                print(f"Your cards: {player_hand}, current score: {player_score}")

    
    second_card = random.sample(cards,1)

    computer_hand.append(second_card[0])
    comp_sum = computer_hand[0]+computer_hand[1]
    if comp_sum<17:
        while comp_sum<17:
            third_card =random.sample(cards,1)
            computer_hand.append(third_card[0])
            if computer_hand[-1] == 11 and comp_sum+computer_hand[-1]>21:
                comp_sum = comp_sum + 1
                computer_score =comp_sum
            
            else:
                comp_sum =comp_sum+computer_hand[-1]
                computer_score=comp_sum
        print(f"Computer cards: {computer_hand}, current score: {comp_sum}")
    else:
        if computer_hand[0]==11 and computer_hand[1] == 11:
            computer_hand[1] = 1
            for i in range(0,len(computer_hand)):
                computer_score += computer_hand[i]
            print(f"Computer cards: {computer_hand}, current score: {computer_score}")
        else:
            for i in range(0,len(computer_hand)):
                computer_score = computer_score + computer_hand[i]
            print(f"Computer cards: {computer_hand}, current score: {computer_score}")
    
    final(player_score,computer_score)
blackjack()
