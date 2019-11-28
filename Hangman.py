#!/usr/bin/env python
# coding: utf-8

# In[8]:


def hangman(word):
    wrong = 0
    stages = ["",
            "______________         ",
            "|                      ",
            "|          |           ",
            "|         ( )          ",
            "|         /|V          ",
            "|          LL          ",
            "|                      ",
            ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print ("Welcome, hangman.")
    
    while wrong < len(stages) -1:
        print("\n")
        msg ="Please predict one letter of the word: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong +1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you win!")
            print(" ".join(board))
            win= true
            break

    if not win :
        print("\n".join(stages[0:wrong+1]))
        print("You lose! The correct word is '{}'.".format(word))    


# In[9]:


hangman("cat")


# In[ ]:


def hangman2(word):
    wrong = 0
    stages = ["",
            "______________         ",
            "|                      ",
            "|          |           ",
            "|         ( )          ",
            "|         /|V          ",
            "|          LL          ",
            "|                      ",
            ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print ("Welcome, hangman.")
    
    while wrong < len(stages) -1:
        print("\n")
        msg ="Please predict one letter of the word: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong +1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you win!")
            print(" ".join(board))
            win= true
            break

    if not win :
        print("\n".join(stages[0:wrong+1]))
        print("You lose! The correct word is '{}'.".format(word))    


# In[ ]:




