words = ["hi", "python", "is", "cool", "code", "a"]
print(f"Original Words: {words}")
large=lambda word:len(word)>3
# for word in words:
#     if(large(word)):
#         long_words.append(word)
long_words=[word for word in words if large(word)]
print(f"Long Words: {long_words}")