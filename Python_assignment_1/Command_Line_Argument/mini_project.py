
'''
MINI PROJECT 1
hroughcommand line arguments three strings separated by space aregiven to you. Eachstring is a series of numbersseparated by hyphen(-). You like all the numbers in string 1 and dislike all the numbers in string 2.
Third string contains thenumbers given to you. Your initial happiness is 0. When you encounter anumberwhich is present in string 1, add 1 to yourhappiness, if it is present in string 2, add -1 to your happiness.Otherwise, your happiness does not change. Output your final happiness at the end.
'''
import sys


if len(sys.argv) != 4:
    print("Please provide exactly three hyphen-separated strings as command line arguments.")
else:
    
    liked = set(map(int, sys.argv[1].split('-')))
    disliked = set(map(int, sys.argv[2].split('-')))
    given = list(map(int, sys.argv[3].split('-')))

    happiness = 0

   
    for num in given:
        if num in liked:
            happiness += 1
        elif num in disliked:
            happiness -= 1
       

   
    print(happiness)
