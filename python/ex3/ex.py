#Learn user Input
#Exercise 3: Print characters from a string that are present at an even index number


word = input('Enter word ')
print("Original String:", word)

size = len(word) #Here len is the equivalent of lenght in C# or JS

print("Printing only even index chars")
for i in range(0, size - 1, 2): #Here the range is to be "enter" every even number of the index of the lenght of the word (ex for the word "Thom", it will only go ahed for the leter H and M)
    print("index[", i, "]", word[i])


#Other whay to do it  (solution 1 is from line 10 to 12)
x = list(word) #Here the list attribute create an "array" (i called it array to compare it to JS)
print(x)
for i in x[0::2]: #Here the [0::2] mean start at 0 and enter the loop each 2 passes
    print(i)