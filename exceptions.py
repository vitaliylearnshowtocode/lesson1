#import random

def cut_cake(people):
    try:
        parts = 1 / people
        print(f"Каждый человек получит {parts} пирога")
    except KeyboardInterrupt:
        print("Пока")
cut_cake (5)

#while True:
#    p = random.randint(1, 10)
#    cut_cake(p)