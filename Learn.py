# No arguments, no return
def greet():
    print('Welcome to the fight club')
    
# Arguments, no return
def log_message(msg):
    print(f"log: {msg}")
    
# No arguments, return
def get_current_year():
    import datetime
    return datetime.datetime.now().year

# Arguments, return
def add(salary, bonus):
    return salary + bonus

add(35240,3000)

# Multiple return values
def multi_values(x):
    return min(x),max(x),sum(x)

multi_values([5, 10, 15])

# Default arguments
def classify_movies(minutes, threshold=90):
    return 'Short' if minutes < threshold else 'Long'

classify_movies(89)

# Keyword arguments
def add_to_catelog(title, type='MOVIE',country='USA'):
    print(f"Added {title} {type} from {country}")
    
add_to_catelog("matrix")

# Positional arguments
def rate_content(title,rating):
    print(f"{title} is rated {rating}")
    
rate_content('Matrix',9.2)

# *args
def run_time(*minute):
    return sum(minute)/len(minute)

run_time(60)

# **kwargs
def content_info(**details):
    for key, values in details.items():
        print(f"{key}:{values}")
        
# Nested functions
def analyze_movie(minutes):
    def is_short(m): return m < 90
    return [is_short(m) for m in minutes]

analyze_movie([45,89,90])

# Function as argument
def square(x):
    return x * x

def apply_function(items, operation):
    return [operation(item) for item in items]

numbers = [1, 2, 3, 4, 5]
result = apply_function(numbers, square)
result

# Function returning another function
def multiplier(factor):
    def multiply(x): return x * factor
    return multiply

multiplier(100)

# Anonymous (lambda) function
normalize = lambda x: x / 100
normalize(200)

# Recursive function
def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)

factorial(5)

# -----------------------------
# Employee Salary Calculator
# One-time Input + Table Output
# -----------------------------

def get_valid_amount(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("  Amount cannot be negative. Try again.")
                continue
            return value
        except ValueError:
            print("  Invalid input. Please enter a number.")


def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("  Must be at least 1. Try again.")
                continue
            return value
        except ValueError:
            print("  Invalid input. Please enter a whole number.")


def calculate_salary(base, bonus):
    return base + bonus


def calculate_tax(salary):
    if salary <= 500000:
        return salary * 0.10
    elif salary <= 1200000:
        return salary * 0.20
    else:
        return salary * 0.30


def collect_all_employees():
    employees = []

    print("\n========================================")
    print("      EMPLOYEE SALARY CALCULATOR")
    print("========================================")

    n = get_valid_int("\nHow many employees do you want to add? ")

    for i in range(n):
        print(f"\n--- Employee {i+1} of {n} ---")

        name = input("  Name        : ").strip()
        while not name:
            print("  Name cannot be empty.")
            name = input("  Name        : ").strip()

        base  = get_valid_amount("  Base Salary : ₹")
        bonus = get_valid_amount("  Bonus       : ₹")

        salary = calculate_salary(base, bonus)
        tax    = calculate_tax(salary)
        net    = salary - tax

        employees.append({
            "name":   name,
            "base":   base,
            "bonus":  bonus,
            "salary": salary,
            "tax":    tax,
            "net":    net
        })

    return employees


def display_table(employees):

    # column widths
    cw = {
        "name":   20,
        "base":   14,
        "bonus":  12,
        "salary": 14,
        "tax":    12,
        "net":    14
    }

    # separator line
    sep = ("+"+"-"*(cw["name"]+2)
          +"+"+"-"*(cw["base"]+2)
          +"+"+"-"*(cw["bonus"]+2)
          +"+"+"-"*(cw["salary"]+2)
          +"+"+"-"*(cw["tax"]+2)
          +"+"+"-"*(cw["net"]+2)+"+"
    )

    # header
    print("\n\n========================================")
    print("         EMPLOYEE SUMMARY TABLE")
    print("========================================")
    print(sep)
    print(
        f"| {'NAME':<{cw['name']}} "
        f"| {'BASE SAL':>{cw['base']}} "
        f"| {'BONUS':>{cw['bonus']}} "
        f"| {'GROSS SAL':>{cw['salary']}} "
        f"| {'TAX':>{cw['tax']}} "
        f"| {'NET SAL':>{cw['net']}} |"
    )
    print(sep)

    # rows
    total_salary = 0
    total_tax    = 0
    total_net    = 0

    for emp in employees:
        print(
            f"| {emp['name']:<{cw['name']}} "
            f"| ₹{emp['base']:>{cw['base']-1},.0f} "
            f"| ₹{emp['bonus']:>{cw['bonus']-1},.0f} "
            f"| ₹{emp['salary']:>{cw['salary']-1},.0f} "
            f"| ₹{emp['tax']:>{cw['tax']-1},.0f} "
            f"| ₹{emp['net']:>{cw['net']-1},.0f} |"
        )
        total_salary += emp['salary']
        total_tax    += emp['tax']
        total_net    += emp['net']

    # totals row
    print(sep)
    print(
        f"| {'TOTAL':<{cw['name']}} "
        f"| {' ':>{cw['base']}} "
        f"| {' ':>{cw['bonus']}} "
        f"| ₹{total_salary:>{cw['salary']-1},.0f} "
        f"| ₹{total_tax:>{cw['tax']-1},.0f} "
        f"| ₹{total_net:>{cw['net']-1},.0f} |"
    )
    print(sep)

    # bottom summary
    print(f"\n  Total Employees : {len(employees)}")
    print(f"  Total Payroll   : ₹{total_salary:,.0f}")
    print(f"  Total Tax       : ₹{total_tax:,.0f}")
    print(f"  Total Net Pay   : ₹{total_net:,.0f}")
    print("\n========================================\n")


def main():
    employees = collect_all_employees()
    display_table(employees)

main()

# \Why do functions exist?
# Ans: Functions exist in programing czo they make code reusable, organized, easier to understand, and maintainable.instead of repeating code everywhere you define at
# once inside a function and called whenever it needed. It save your time, reduce error, and improve clearity.\*

# \Difference between return and print.
# Ans: Return give you the product in your hand, however the print just show it on the display\*

# \Why is None returned?
# Ans: In python, if a function doesn't explicitly use return, it automatically return none.\* 

# \Are functions objects in Python?
# Ans: Yes, In pyhton everything is an object. which means functions cab be assign to veriables, passed as arguments to other functions.\*

# \Can a function be stored inside a list?
# Ans: Yes, in python a function can absolutely be stored inside a list coz functions are objects \*
def square(x):
    return x * x

def cube(x):
    return x * x * x

def double(x):
    return x * 2

function = [square, cube, double]
for i in function:
    print(i(4))

# \Can a function be passed to another function?
# Ans:  Yes, a function can definately be passed to another function. This is one of the most powerful feature on this langage.\*
def square(x):
    return x * x

def apply_function(func, value):
    return func(value)

print(apply_function(square,5))

# \What is first-class function support?
# Ans: first‑class function support means that in Python, functions are treated like any other object (like integers, strings, or lists). 
# They aren’t “special cases” — they’re full citizens of the language.\*
def greet(name): 
    return f"Hello, {name}"

say_hello = greet
print(say_hello("Aman"))  

# \ Difference between parameter and argument.
# Ans:Parameters define what a function expects, arguments provide the actual data.\*
def calculate_salary(base, bonus):    # base, bonus = parameter
    return base + bonus

print(calculate_salary(40000, 13000)) # 40000, 13000 = arguments

# \Why avoid global variables?
# Ans: Global variables are like leaving your house keys on the street — anyone can grab them and mess with your stuff. Clean code avoids globals because 
# they destroy clarity, testability, and safety.\* 

# \What is function scope?
# Ans: Function scope in python means the region of code where variable is accessable. Every veriable lives inside some scope, and functions create their own scope.\* 

# Write code and explain the output. Explain why each output appears.
s = "Python"

print(s[0])
print(s[-1])
print(s[2])
print(s[-2])
# This is basucelly indexing where 0 means first character seems like -1 mean last character and so on..

# Show that strings are immutable.Don't just say they are.Prove it. Then explain why Python made strings immutable.?
s = "Rock"
s[0] = 'L'

# Attempting s[0] = "L" fails because Python enforces immutability.
# Why: Safety & Reliability, Hashing & Performance, Thread Safety, Consistency.

# Predict the output first. Then run. Explain every slice. 
s = "DataScience"

print(s[:4])
print(s[4:])
print(s[::2])
print(s[::-1])
print(s[-5:-1])

# This is also a sicing, [:4] means 4 letters from staring like 0,1,2,3 indexes, [4:] everything after 4 letters, [::2] means everything 2nd character
# [::-1] means reverse this string, [-5:-1] means last 5th to last 2nd character.

# For each method:explain what it does, when you would use it., one real-world example.
# upper - Upper is besicaly will convert anu string into upper letter
word = "Python"
new_word = word.upper()
print(new_word)

# lower - Lower will convert the string into lower case.
word = 'PyThon'
new_word = word.lower()
print(new_word)


# title - This will convert your string first letter into capital letter of each word.
word = 'welcome to the fight club.!'
new_word = word.title()
print(new_word)


# capitalize - This will capitalizes only the first letter of the string.
word = "python"
new_word = word.capitalize()
print(new_word)


# strip - This will remove the unwanted spaces in the given string.
word = ' Say_my_name '
new_word = word.strip()
print(new_word)

# lstrip - Removes whitespace from the left side.
word = " Ballia"
new_word = word.lstrip()
print(new_word)


# rstrip - Remove whitespace from thee right side.
word = "Ballia "
new_word = word.rstrip()
print(new_word)


# replace - Replace all occurance of a substring
word = "ballia"
new_word = word.replace('ballia','Varanshi')
print(new_word)


# split - Split string into a list by seprators.
word = "Aman123 Ballia"
print(word.split())

# join - Joins elements of a list into a string with a separator.
print(",".join(["2026","07","13"]))  

# find - This find the values in the given string or list that is present or not.
word = "Welcome to fight club.!"
print(word.find('fight'))


# index - Same as find, but raises error if not found.
word = "Let me guess.!"
print(word.index('me')) 


# count - This count the occurance (frequency) of substring.
word = "banana"
print(word.count('a')) 

# startswith - This will check the if any string starts with prefix.
word = "Telus International"
print(word.startswith("I"))

# endswith - This will check if string ends with suffix.
word = "Telus International"
print(word.endswith('l'))

# isalpha - This check is the given string or characters are letters.?
word = "Batman"
print(word.isalpha())

# isdigit - This check if the given value or all characters are digits.
word = '12345'
print(word.isdigit())
 
# isalnum - This check if all characters are letters or digits.
word = "UttarPradesh277403"
print(word.isalnum())

# isspace - Checks if string contains only whitespace.
word = "  "
print(word.isspace())

# Difference between find() and index().?
# Ans - you use this to check if something eixst without crashing the program. However, index Returns the index of the first occurrence of a substring.

# Difference between split() and join().
# Ans - Split break a string into a list of substing based on substrings. However, Combine element of a list into a single string,with seprator 
# between them.

# Why is ''.join(list) faster than + inside loops?
# Ans: Because strings are immutable, using + in loops creates a new string object every time, while ''.join(list) builds the final string in 
 #one pass (fast, O(n)).

# Difference between == and is for string.
# Ans: we use == to check whether two values contain same values/content. However "is" check Whether two variables point to the same object in memory.
a = "Python"
b = "Python"
print(a is b)
print( a == b)

# What is string interning.?
# Ans: String interining is a memory optimization technique in python where certain string are stored only once in the memory and reused whenever
# the same value appears.

# Problem Solving: Write reusable functions.
# Count:- Uppercase, Lowercase , Digits ,Spaces, Special characters
# input: "Hello World 123!!"
# Return a dictionary.

def count_characters(text):
    count = {
        "uppercase" : 0,
        "lowercase" : 0,
        "digit": 0,
        "spaces" : 0,
        "special" : 0
    }

    for i in text:
        if i.isupper():
            count['uppercase'] += 1
        elif i.islower():
            count['lowercase'] += 1
        elif i.isdigit():
            count['digit'] += 1
        elif i.isspace():
            count['spaces'] += 1
        else:
            count['special'] += 1
    return count

word = "Hello World 123!!"
result = count_characters(word)
print(result)

# Write your own: reverse_string() and don't use [::-1].?
def reverse_string(text):
    result = " "
    
    for i in text:
        result = i + result
    return result
    
word = "Hello World 123!!"
print(reverse_string(word))

# Check whether a string is a palindrome. Ignore: spaces, punctuation, case.
def palindrome(text):
    cleaned = []
    for i in text:
        if i.isalnum():
            cleaned += i.lower()
    return cleaned == cleaned[::-1]

texts = "mada,m!"
print(palindrome(texts))

# OR

def is_pelindrome(word):
    cleaned = ' '.join(i.lower() for i in word if i.isalnum())
    return cleaned == cleaned [::-1]
    
word = 'Madam'
print(is_pelindrome(word))

# Compress a string.
# Ex:- aaabbccccdd -> a3b2c4d2

def string_compresation(text):
    if not text:
        return " "
    
    compressed = " "
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == text[i -1]:
            count += 1
        else:
            compressed += text[i - 1] + str(count)
            count = 1
    compressed += text[i - 1] + str(count)
    return compressed

word = "aaabbccccdd"        
print(string_compresation(word))
    
# Find the first non-repeating character.
# Eg ; programming -> p

def first_non_repeating(text):
    count = {}
    for i in text:
        count[i] = count.get(i,0) + 1
    for i in text:
        if count[i] == 1:
            return i
        
    return None

word = "programing"
print(first_non_repeating(word))

# Find the most frequent character.

def most_frequent(text):
    count = {}
    for i in text:
        count[i] = count.get(i,0) + 1
    max_char = max(count,key=count.get)
    return max_char,count[max_char]

word = "programing"
print(most_frequent(word))

# Write your own implementation of split() and don't use split().
def custom_split(text,delimiter=" "):
    result  = []
    current = " "
    
    for i in text:
        if i == delimiter:
            result.append(current)
            current = " "
        else:
            current += i
            
    result.append(current)
    return result

word = "Hello World 123!"
print(custom_split(word))
    
# Write your own implementation of join() and don't use join()
def custom_join(iterable, delimiter=" "):
    current = " "
    for i, item in enumerate(iterable):
        if i > 0:
            current += delimiter
        current += str(item)
    return current

word = ["Hello","World","123"]
print(custom_join(word))

