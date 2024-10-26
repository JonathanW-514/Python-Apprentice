"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']

#story = words['once upon a time a 👦 and a 👧 went to a park to play ⚽']
story = [ words[0] , words[2], words[7] ]
# Create a story using the words in the list

# Display the story to the user
print(' '.join(story))