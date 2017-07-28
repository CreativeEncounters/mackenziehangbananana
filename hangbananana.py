word = "njbjlgfj"
hidden = []
used = []
lives = 6
stages = [" O\n_|_\n | \n/ \\",
          " O\n_|\n |\n/ \\",
          " O\n |\n |\n/ \\",
          " O\n |\n |\n/",
          " O\n |\n |",
          " O",
          ""]


for i in range(0, len(word)):
    hidden.append("_")

while lives > 0:

    print "player:\n",stages[lives]
    
    print hidden
    guess = raw_input("guess a letter")

    if not guess in used:
        used.append(guess)
    else:
        continue
    
    if guess in word:
        for j in range(0, len(word)):
            if word[j] == guess:
                hidden[j] = word[j]
    else:
        lives -= 1
        if lives == 0:
            break

    if hidden.count('_') == 0:
        break

print "the word was:", word

if lives > 0:
    print "you won"
else:
    print "you lose"
