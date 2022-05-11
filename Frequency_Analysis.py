# Author:       Trevor Karl
# ULID:         C00441253
# Course:       CMPS 315_Spring 2021
# Assignment:   pa1 - Frequency Analysis
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work


#Counts the occurrence of each letter in alphabetical order
def letterCount(file):

    Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    count = []

    for x in range(0, 26):
        if(file.count(Alphabet[x]) != 0):
            count.append(tuple([Alphabet[x], file.count(Alphabet[x])]))

    count.sort(key = lambda x: x[1], reverse = True)

    return(count)    


#Counts the occurrence of each bigram 
def bigramCount(file):

    bigrams = []
    bigramsNoDupes = []

    count = []

    for x in range(0, len(file) - 2):
        bigrams.append(file[x : x + 2])

    for y in bigrams:
        if y not in bigramsNoDupes:
            bigramsNoDupes.append(y)
    bigrams = bigramsNoDupes        

    for i in range(0, len(bigrams)):
        count.append(tuple([bigrams[i], file.count(bigrams[i])]))

    count.sort(key = lambda x: x[1], reverse = True)    

    return(count)

        
#Counts the occurrence of each trigram
def trigramCount(file):

    trigrams = []
    trigramsNoDupes = []
    
    count = []

    for x in range(0, len(file) - 3):
        trigrams.append(file[x : x + 3])

    for y in trigrams:
        if y not in trigramsNoDupes:
            trigramsNoDupes.append(y)
    trigrams = trigramsNoDupes        

    for i in range(0, len(trigrams)):
        count.append(tuple([trigrams[i], file.count(trigrams[i])]))

    count.sort(key = lambda x: x[1], reverse = True)

    return(count)


#Prints top 5 occurrences
def top5(l):

    top5 = []
    
    for x in range(0, 5):
        top5.append(l[x])
        
    print(top5)
    

#Prompts user for the file name
fileName = input("Enter input filename: ")
file = open(fileName, "r")

print()


#Removes any breaks in the file
fileWithoutBreaks = ""
for line in file:
    strip = line.rstrip()
    fileWithoutBreaks += strip

fileContents = fileWithoutBreaks


#Prints contents of the file
print("Input text: ")
print(fileContents)

print()


#Prints number of characters in the file after being stripped
numCharacters = len(fileContents)
print("Total number of characters: ", numCharacters)

print()


#Prints letter count and the top 5 
print("Individual letter count:")
print(letterCount(fileContents))

print()

print("Top 5 letters:")
top5(letterCount(fileContents))

print()


#Prints bigram count and the top 5
print("Full bigram list:")
print(bigramCount(fileContents))

print()

print("Top 5 bigrams:")
top5(bigramCount(fileContents))

print()


#Prints trigram count and the top 5
print("Full trigram list:")
print(trigramCount(fileContents))

print()

print("Top 5 trigrams:")

top5(trigramCount(fileContents))

file.close()

