from words import words
import random

word = list(random.choice([x for x in words if len(x) < 4]))
ans = []
guessed = []
print(len(word))
def play():
    life = 5
    while word != ans:
        if life != 0:
            print("guess a letter: ")
            a = input()
            guessed.append(a)
            if a in word:
                ans.append(a)
            else:
                life -= 1
                if life == 1:
                    print("last life!")
                else:
                    print(f"{life} lifes left.")
            print(" ".join([x.capitalize() if x in guessed else "_" for x in word]))
        else:
            print(f"you lost, the ans way {word}")
            return
    print("yey, you won")

play()