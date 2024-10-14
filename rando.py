import random
import time

def compliment_rock():
    compliments = [
        "You're the most amazing rock I've ever seen!",
        "Your texture is so unique and beautiful.",
        "Wow, you really know how to stay grounded!",
        "You're a solid friend, rock.",
        "No one can pebble you!",
        "You're so rock-solid dependable.",
        "You always rock my world.",
        "I could sit and admire you for ages.",
        "You're the diamond in the rough!",
        "You just have that certain rock-star quality!"
    ]

    while True:
        compliment = random.choice(compliments)
        print(f"Dear Rock, {compliment}")
        time.sleep(2)  # Wait 2 seconds before complimenting again

if __name__ == "__main__":
    print("Starting the Rock Compliment Bot...")
    compliment_rock()
