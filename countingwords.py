wordCount = 1
characterCount = 0
introString = input("Enter a string")
for i in introString:
  characterCount = characterCount + 1
  if(i == " "):
    wordCount = wordCount + 1
print("Your amount of words are ", wordCount)
print("Your amount of characters are ", characterCount)