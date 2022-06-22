from random import random
from random import randrange

# two lists of cards that can be chosen
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
#dictionary for high card meanings
highdict = {
    'artifact': 'Represents the importance of some physical object that must be obtained, protected, or destroyed at all costs.',
    'beast': 'Represents great rage or passion; something bestial or malevolent hiding in plain sight or lurking just below the surface.', 
    'broken one': 'Represents defeat, failure, and despair; the loss of something or someone important, without which one feels incomplete.',
    'dark lord': 'Represents a single, powerful individual of an evil nature, one whose goals have enormous and far-reaching consequences.', 
    'donjon': 'Represents isolation and imprisonment; being so conservative in thinking as to be a prisoner of ones own beliefs.', 
    'ghost': 'Represents the looming past; the return of an old enemy or the discovery of a secret buried long ago.', 
    'executioner': 'Represents the imminent death of one rightly or wrongly convicted of a crime; false accusations and unjust prosecution.', 
    'horseman': 'Represents death; disaster in the form of the loss of wealth or property, a horrible defeat, or the end of a bloodline.', 
    'innocent': 'Represents a being of great importance whose life is in danger (who might be helpless or simply unaware of the peril).', 
    'marrionette': 'Represents the presence of a spy or a minion of some greater power; an encounter with a puppet or an underling.',
    'mists': 'Represents something unexpected or mysterious that cant be avoided; a great quest or journey that will try ones spirit.', 
    'raven': 'Represents a hidden source of information; a fortunate turn of events; a secret potential for good.', 
    'seer': 'Represents inspiration and keen intellect; a future event, the outcome of which will hinge on a clever mind.', 
    'tempter': 'Represents one who has been compromised or led astray by temptation or foolishness; one who tempts others for evil ends.'
}
def wordsearch():
    word = input('Type word you want to find: ')
    if word in highdict:
        print(highdict[word])
    else:
        print('There was an error finding your word.')
    

print('Hello! Choose your option: 1 = card selection, 2 = word search, 3 = Exit')
index = int(input('Enter your number: '))
while index != 3:
        if index == 1:
            cardselection()
            index = int(input('Enter your number:  1 = card selection, 2 = word search, 3 = Exit '))
        elif index == 2:
            wordsearch()
            index = int(input('Enter your number:  1 = card selection, 2 = word search, 3 = Exit '))
        else:
            print('That is not a valid number')
        


