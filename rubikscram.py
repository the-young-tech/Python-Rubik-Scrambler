import time
import random

normal_move = ['R', 'U', 'L', 'B', 'D', 'F']
negative_move = ["R'", "U'", "L'", "B'", "D'", "F'"]
double_move = ['R2', 'U2', 'L2', 'B2', 'D2', 'F2']

red_text = "\033[91m"
green_text = "\033[92m"
end_color = "\033[0m"
print("Do You Want A Scramble? (" + green_text + "Y" + end_color + "/" + red_text + "N" + end_color + ")")
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
    print("The Generated Scramble -> " + scramble_str)
    
    input("Press Enter To " + green_text + "Start " + end_color + "The Timer....")
    start_time = time.time()
    
    input("Press Enter To " + red_text + "Stop " + end_color + "The Timer....")
    elapsed_time = time.time() - start_time
    
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print("Time Elapsed: {} Minutes and {} Seconds".format(minutes, seconds))
else:
    print("Okay - Exiting The Scrambler....")
