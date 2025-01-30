word = input("Enter a word: ")
updated_word = ''
for i in range (0,len(word)):
    if (i%2!=0):
        updated_word+=word[i].upper()
    else:
        updated_word+=word[i]

print(updated_word)
        