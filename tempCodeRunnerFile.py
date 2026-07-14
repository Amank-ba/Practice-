def reverse_string(text):
    result = " "
    
    for i in text:
        result = i + result
    return result
    
word = "Hello World 123!!"
print(reverse_string(word))