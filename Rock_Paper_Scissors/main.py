import random
options = ['r','s','p']
print(" Rock = R",'\n',"Paper = P",'\n',"Scissors = S")
while True:
    user_option = input("Play either 'P','R','S': \n").lower()
    if user_option in options:
        CPU = random.choice(options)
        print(f'You played {user_option}, CPU played {CPU}','\n')
        if user_option == CPU:
            print("It's a tie, play again. \n")
        else:
            if user_option== 'r' and CPU =='s':
                print("Hurray!!!, You win")
            elif user_option == 's' and CPU =='p':
                print("Hurray!!!, You win")
            elif user_option == 'p' and CPU =='r':
                print("Hurray!!!, You win")
            else:
                print("Hurray!!!, CPU wins")
            break
        
        # playagain = input("Do you wish to play again? Type 'Y' to continue 'N' to exit: ").lower()
        # if playagain != 'y' or playagain != 'n':
        #     print("Enter either 'Y' or 'N'")
        # elif playagain == 'y':
        #     continue
        # else: 
        #     break
    else:
        print("Invalid input, type either 'R','S' or 'P' \n")
   