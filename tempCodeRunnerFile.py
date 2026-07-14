def most_frequent(text):
    count = {}
    for i in text:
        count[i] = count.get(i,0) + 1
    max_char = max(count,key=count.get)
    return max_char,count[max_char]

word = "programing"
print(most_frequent(word))