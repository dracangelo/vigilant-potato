import webbrowser
import time
import random

def annoying_bot():
    # A list of random annoying links
    annoying_links = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # Rick Astley - Never Gonna Give You Up
        "https://www.youtube.com/watch?v=oHg5SJYRHA0",  # Another Rick Roll
        "https://www.youtube.com/watch?v=j5a0jTc9S10",  # Nyan Cat
        "https://www.youtube.com/watch?v=kfVsfOSbJY0",  # Friday by Rebecca Black
        "https://www.youtube.com/watch?v=ZZ5LpwO-An4",  # He-Man Sings
        "https://www.youtube.com/watch?v=ub82Xb1C8os",  # Trololo song
        "https://www.youtube.com/watch?v=QH2-TGUlwu4",  # Nyan Cat (extended)
        "https://www.youtube.com/watch?v=9o19CaOSuD8",  # Baby Shark Dance
        "https://www.youtube.com/watch?v=3GwjfUFyY6M",  # Celebration by Kool & The Gang
        "https://www.youtube.com/watch?v=C-du33Go4RE",  # Hamster Dance
        "https://www.youtube.com/watch?v=L_jWHffIx5E",  # Who Let the Dogs Out
        "https://www.youtube.com/watch?v=hY7m5jjJ9mM",  # Cat Vibing to Ievan Polkka
        "https://www.youtube.com/watch?v=y6120QOlsfU",  # Darude - Sandstorm
        "https://www.youtube.com/watch?v=I1ywrb2Qd0Y",  # Crazy Frog - Axel F
        "https://www.youtube.com/watch?v=1Q3MRfvMGIY",  # Mii Channel Music
    ]

    while True:
        link = random.choice(annoying_links)
        webbrowser.open(link)  # Open the link in the default browser
        print(f"Opening link: {link}")
        time.sleep(5)  # Wait 5 seconds before opening another link

if __name__ == "__main__":
    print("Starting the Annoying Bot...")
    annoying_bot()
