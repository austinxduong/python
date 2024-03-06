message = input(">")
wordsInput = message.split(' ')

emojis = {
    ":)": "😀",
}
print(wordsInput)

output = ""
for word in wordsInput:
    output += emojis.get(word, word) + " " #if key is present, return the value of that key. otherwise, default word returns the word
print(output)