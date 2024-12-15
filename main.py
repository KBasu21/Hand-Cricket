# Cricket Game
 
print(""" ~~~~~~~~~~ Game of Cricket ~~~~~~~~~~
 
Instructions:
 
1. You have to select any random number from 1 to 6.
2. The computer will also select a number.
3. While batting, if the number selected by you and computer is different, then your number will add to your runs.
   If the number selected by you and computer is same, then you will lose your wicket.
4. While bowling, if the number selected by you and computer is different, then the computer's number will add to its runs.
   If the number selected by you and computer is same, then the computer will lose its wicket.
5. Each player will get minimum 1 wicket and maximum 10 wickets with minimum 1 over and maximum 450 overs for batting and bowling.
6. The innings will end after either the all wickets fell or the overs end.
7. The player with maximum runs wins. """)
 
print("\n---------- Start Game ----------")
 
import random

# Overs and wickets selection (atleast 1 over and 1 wicket)
def overschoice():
    over = int(input("Enter No. of overs (atleast 1, max 450):"))
    wickets = int(input("Enter No. of wickets (atleast 1, max 10):"))
    if over == 0 or wickets == 0 or over > 450 or wickets > 10:
        print("\nWrong input!")
        overschoice()
    else:
        return over, wickets
T = overschoice()
# Toss 
 
print("\nHere comes the Toss")
toss = (input("Choose heads or tails: ")).lower()
 
random_toss = random.randint(1,2)            # In random_toss (1 = Heads) and (2 = Tails)
random_opt = random.randint(1,2)             # In random_opt (1 = bat) and (2 = ball)
 
u_opt = 0
c_opt = 0
 
if random_toss == 1 and toss == "heads":
    print("\nYou won the toss")
    u_opt = (input("Choose bat or ball: ")).lower()
 
elif random_toss == 2 and toss == "tails":
    print("\nYou won the toss")
    u_opt = (input("Choose bat or ball: ")).lower()    
  
else:
    print("\nYou lost the toss")
 
    if random_opt == 1:
        c_opt = "bat"
        print("Computer choose to",c_opt)
 
    elif random_opt == 2:
        c_opt = "ball"
        print("Computer choose to",c_opt)
 
# First Innings 
 
print("\n---------- First Innings Begins ----------")
 
runs_1 = 0
wickets_1 = 0
balls_1 = 0
 
while wickets_1 != T[1] and balls_1 != T[0]*6:
 
    u_choice = int(input("\nChoose any number from 1 to 6: "))
    c_choice = random.randint(1,6)
 
    if u_choice < 0 or u_choice > 6:
        print("\nPlease choose a value from 1 to 6.")
 
    else:
        print("Your choice: ",u_choice,"\nComputer's choice: ",c_choice)
 
        if u_choice == c_choice:
            wickets_1 += 1
 
        else:
            if u_opt == "bat" or c_opt == "ball":
                Bat_first = "You"
                Ball_first = "Computer"
                runs_1 += u_choice
 
            elif u_opt == "ball" or c_opt == "bat":
                Bat_first = "Computer"
                Ball_first = "You"
                runs_1 += c_choice
 
        print("\nScore =",runs_1,"/",wickets_1)
 
        balls_1 += 1
 
        for over in range(1, T[0]+1):
            if balls_1 == over * 6:
                print(f"End of Over {over}")

 
        print("Balls remaining: ", T[0]*6 - balls_1)
 
print("\n---------- End of Innings ----------") 
 
print("\nFinal Score:")
print("Runs =",runs_1)
print("wickets =",wickets_1)
 
print("\n",Ball_first,"needs",runs_1 + 1,"runs to win.")
 
# Second Innings 
 
print("\n---------- Second Innings Begins ----------")
 
runs_2 = 0
wickets_2 = 0
balls_2 = 0
 
while wickets_2 != T[1] and balls_2 != T[0]*6 and runs_2 <= runs_1:
 
    u_choice = int(input("\nChoose any number from 1 to 6: "))
    c_choice = random.randint(1,6)
 
    if u_choice < 0 or u_choice > 6:
        print("\nPlease choose a value from 1 to 6.")
 
    else:
        print("Your choice: ",u_choice,"\nComputer's choice: ",c_choice)
 
        if u_choice == c_choice:
            wickets_2 += 1
 
        else:
            if Bat_first == "Computer": 
                runs_2 += u_choice
                Bat_second = "You"
 
            elif Bat_first == "You":
                runs_2 += c_choice
                Bat_second = "Computer"
 
        print("\nScore =",runs_2,"/",wickets_2)
 
        balls_2 += 1
 
        for over in range(1, T[0]+1):  # 1 to 450 inclusive
            if balls_1 == over * 6:
                print(f"End of Over {over}")
 
        if runs_2 <= runs_1 and balls_2 <= T[0]*6 - 1 and wickets_2 != T[1]:
            print("To win:",runs_1 - runs_2 + 1,"runs needed from",T[0]*6 - balls_2,"balls.")
 
print("\n---------- End of Innings ----------") 
 
print("\nFinal Score:")
print("Runs =",runs_2)
print("wickets =",wickets_2)
 
# Result of Match 
 
print("\n~~~~~~~~~~ Result ~~~~~~~~~~")
 
if runs_1 > runs_2:
 
    if Bat_first == "You": 
        print("\nCongratulations! You won the Match by",runs_1 - runs_2,"runs.")
 
    else:
        print("\nBetter luck next time! The Computer won the Match by",runs_1 - runs_2,"runs.") 
 
elif runs_2 > runs_1:
 
    if Bat_second == "You": 
        print("\nCongratulations! You won the Match by",T[1] - wickets_2,"wickets.")
 
    else:
        print("\nBetter luck next time! The Computer won the Match by",T[1] - wickets_2,"wickets.")
 
else:
    print("The Match is a Tie.","\nNo one Wins.")

input("Press 0 to exit...")