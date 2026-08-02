def filter_adults(age):
    result = []
    for i in age:
        if i.get("age",0)>= 18:
            result.append(i)
    return result

print(filter_adults([
    {"name": "Aman", "age": 22},
    {"name": "Ravi", "age": 16},
    {"name": "Anita", "age": 18},
    {"name": "Sunil", "age": 15}
]))