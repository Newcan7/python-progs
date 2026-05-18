words = ["apple", "bat", "orange", "umbrella", "cat"]

words1=list(filter(lambda x: x[0] in "aeiouAEIOU",words))
words2=sorted(words1,key=len)
print(words2)