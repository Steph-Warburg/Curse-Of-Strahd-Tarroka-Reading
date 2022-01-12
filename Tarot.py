#!/usr/bin/env python
# coding: utf-8

# In[13]:


from random import random
from random import randrange


# In[53]:



high = ['artifact', 'beast', 'broken one', 'dark lord', 'donjon', 'ghost', 'executioner', 'horseman', 'innocent', 'marrionette',
       'mists', 'raven', 'seer', 'tempter']
cards = ['avenger', 'paladin', 'soldier', 'mercenary', 'myrmidon', 'berserker', 'hooded one', 'dictator', 'torturer', 'warrior', 
        'transmuter', 'diviner', 'enchanter', 'abjurer', 'elementalist', 'evoker', 'illusionist'] 
def cardselection():
    h = randrange(len(high))
    h2 = randrange(len(high))
    c = randrange(len(cards))
    c2 = randrange(len(high))
    
    print("Your first card is " + high[h])
    input("Press Enter to continue ")

    if(h2 == h):
         h3 = randrange(len(high))
         print('Your second card is: ' + high[h3])
    else:
        print('Your second card is: ' + high[h2])
    
    input("Press Enter to continue ")
    print("Your third card is " + cards[c])
    input("Press Enter to continue ")
    if(c2 == c):
         h3 = randrange(len(high))
         print('Your forth card is: ' + cards[c3])
    else:
        print('Your forth card is: ' + cards[c2])
    input("Press Enter to continue ")
    c3 = randrange(len(high))
    if c3 == c2 or c3 == c:
        c4 = randrange(len(high))
        print('Your fifth card is: ' + cards[c4])
    else:
         print('Your fifth card is: ' + cards[c3])
    


# In[54]:


highdict = {
    'artifact': 'i like cheese',
    'beast': '', 
    'broken one': '',
    'dark lord': '', 
    'donjon': '', 
    'ghost': '', 
    'executioner': '', 
    'horseman': '', 
    'innocent': '', 
    'marrionette': '',
    'mists': '', 
    'raven': '', 
    'seer': '', 
    'tempter': '' 
}
def wordsearch():
    word = (input('Type word you want to find: '))
    if word in highdict:
        print(highdict[word])
    else:
        print('There was an error finding your word.')
    


# In[ ]:


print('Hello! Choose your option: 1 = card selection, 2 = word search, 3 = Exit')
index = int((input('Enter your number: ')))
while index != 3:
        if index == 1:
            cardselection()
            index = int((input('Enter your number:  1 = card selection, 2 = word search, 3 = Exit ')))
        elif index == 2:
            wordsearch()
            index = int((input('Enter your number:  1 = card selection, 2 = word search, 3 = Exit ')))
        else:
            print('That is not a valid number')
print("Thank you for using this service!")
        


# In[ ]:




