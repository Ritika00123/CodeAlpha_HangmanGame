import random
words=['python','robot','amazon','coding','intern']
word=random.choice(words)
guessed=[]
attempts=6
while attempts>0:
    display=''.join(c if c in guessed else '_' for c in word)
    print('Word:',display)
    if '_' not in display:
        print('You won!')
        break
    letter=input('Guess a letter: ').lower()
    if letter in word:
        guessed.append(letter)
    else:
        attempts-=1
        print('Wrong! Attempts left:',attempts)
if attempts==0:
    print('Game Over! Word was:',word)
