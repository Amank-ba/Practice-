def custom_join(iterable, delimiter=" "):
    current = " "
    for i, item in enumerate(iterable):
        if i > 0:
            current += delimiter
        current += str(item)
    return current

word = ["Hello","World","123"]
print(custom_join(word))