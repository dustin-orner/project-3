# Hey professor, this is the start of a "game" that I have been thinking of making for a while.
# During quarantine, when gyms were closed, I would use a deck of cards to "generate" a workout that was different each day. 
# It wasn't the only way I kept fit, but it did help to spice things up when I started expecting the same workout every day.  
# That game was inspired by a specific YouTube video, but upon further research it looks like this fitness game was popularized long before then.
# It's not a complete game yet, as I'm not entirely sure how to even code everything yet. 
# This first draft is just to show my progress so far with Python. 
# The rules of the game are as follows: 
# 1. Pick four exercises. Each exercise will be represented by a face card.
# 2. Set a card limit for your exercise (drawing between 10 to 30 cards is usually good) 
# 3. Begin drawing cards. 
# 4. The value on the face of each card is how many reps of the exercises are performed + 10. 
# Example: Drawing a 2 would be 12 reps of that exercise. 
# Jack, Queen, and King are also worth ten reps! Aces are "rest" cards you can rest for a minute or two. 
# 5. The game ends when the set number of cards are drawn.
# Most of this code is from the YouTube tutorial "Making a Deck of Playing Cards in Python" by Brian Fediuk.
# I only recoded it by hand so that I could understand his logic in coding this deck of cards. 
# I hope to use that knowledge later in turning it into something more interactive!

import random 

cardfaces = []
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
facecards = ["Jack", "Queen", "King", "Ace"]
deck = []

for i in range(2,11):
    cardfaces.append(str(i))

#I noticed that Brian used range 2-11, which I thought was strange. 
#Turns out, using the range function in Python goes from the lowest number to one below the highest number in the range!

for j in range(4): 
    cardfaces.append(facecards[j]) 

for k in range(4): 
    for l in range(13): 
        card = (cardfaces[l] + " of " + suits[k])
        deck.append(card) 

random.shuffle(deck) 

for m in range(52): 
    print(deck[m]) 

# One of the things that I thought was coolest about this video was how Brian used these loop functions to generate the deck and suits easily. 
# While it was a lot of work up front, it ended up being easier than manually typing the lists! 
# I ran into a lot of syntax errors while making this, but I'm glad that I was able to get it working. 
# My goal is to iterate on this until I have a program that can: 
# 1. Generate a shuffled deck of cards. (Complete) 
# 2. Allow the user to generate a single card at a time. 
# 3. Allow the user to generate single cards WITHOUT repeating any. 
# 4. Allow the user to set a specific card limit in order to increase or decrease difficulty. 
# 5. Allow the user to allocate specific exercises to each suit of cards. 
# 6. Actually add graphics to the game. 
# 7. Get this program working on my own phone!