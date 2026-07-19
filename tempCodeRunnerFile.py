def palin(text):
    reverse = " "
    for i in text:
        if i.isalnum():
            reverse += i.lower()
            
    return reverse == reverse[::-1]

t = "Madam"
palin(t)