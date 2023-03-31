import time
import random

normal_move = ['R', 'U', 'L', 'B', 'D', 'F']
negative_move = ["R'", "U'", "L'", "B'", "D'", "F'"]
double_move = ['R2', 'U2', 'L2', 'B2', 'D2', 'F2']

print("Do you want a scramble? (y/n)")
answer = input()

if answer.lower() == "y":
    scramble = []
    last_move = ""
    
    while len(scramble) < 20:
        move = random.choice(normal_move + negative_move + double_move)
        if len(last_move) > 0 and move[0] == last_move[0]:
            continue
        scramble.append(move)
        last_move = move
    
    scramble_str = " ".join(scramble)
    print("Your Generated Scramble -> " + scramble_str)
    
    input("Press Enter To Start The Timer....")
    start_time = time.time()
    
    input("Press Enter To Stop The Timer....")
    elapsed_time = time.time() - start_time
    
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print("Time Elapsed: {} Minutes and {} Seconds".format(minutes, seconds))
else:
    print("Okay - Exiting The Scrambler....")
