import random
from listword import words

word=random.choice(words)
if " " in word or '-' in word:
    word=random.choice(word)

letters=set('abcdefghijklmnopqrstuvwxyz')

wordletters=set()
for i in word:
    wordletters.add(i)

lives=6
guessedletters=set()
while len(wordletters)>0 and lives>0:
    guess=input("Guess a letter: ")
    progress=[]
    
    if guess in letters-guessedletters:
        guessedletters.add(guess)
        if guess in wordletters:
            wordletters.remove(guess)
            print("Well done!")
        else:
            lives-=1
            print("Sorry, that letter isn't in the word.")
    elif guess in guessedletters:
        print("You've already guessed that letter. ")
    else:
        print("Not a valid letter")
    
    print("You've used the letters: ",' '.join(guessedletters))
    for i in word:
        if i in guessedletters:
            progress.append(i)
        else:
            progress.append("_")
    print("Word:",''.join(progress))
    print("Lives:",lives)
    print("\n")
    

if lives==0:
    print(f"Better luck next time,the word was {word}")
else:
    print(f"Well done! You guessed the word-{word}")

