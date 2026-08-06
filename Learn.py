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
def factorial(num):
    if num == 0: return 1
    return num * factorial(num-1)

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

    print("\num========================================")
    print("      EMPLOYEE SALARY CALCULATOR")
    print("========================================")

    num = get_valid_int("\nHow many employees do you want to add? ")

    for i in range(num):
        print(f"\num--- Employee {i+1} of {num} ---")

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
    print("\num\num========================================")
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
    print(f"\num  Total Employees : {len(employees)}")
    print(f"  Total Payroll   : ₹{total_salary:,.0f}")
    print(f"  Total Tax       : ₹{total_tax:,.0f}")
    print(f"  Total Net Pay   : ₹{total_net:,.0f}")
    print("\num========================================\num")


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
 #one pass (fast, O(num)).

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

# Design Thinking
# For each problem below, don't code immediately. First answer: Input, Output, Edge cases, Algorithm, Time Complexity, Space Complexity.
# Only then write code.
# Problem A: Validate an email. Don't use regex.

# Input: A string
# Output: True/ False
# Edge cases: Missing @, Multiple @, missing username, Email without domain, empty string, Spaces inside the email.
# Algorithm: check exactly one @ symbol, Split into local part (before @) and domain part (after @).Validate local part: Not empty.
# Contains only allowed characters (letters, digits, ., _, -). Doesn’t start or end with . 
# Validate domain part: Not empty. Must contain at least one . (like example.com). Each section between dots must be non‑empty and alphanumeric.
# If all checks pass → return True, else False. 

def validate_email(email):
    if not email:
        return False
    if email.count('@') != 1:
        return False
    username, domain = email.split('@')
    if not username:
        return False
    if username.startswith(".") or username.endswith("."):
        return False
    
# Username can only have letters, digits, dots, underscores, hyphens
    allowed = "abcdefghijklmnopqrstuvwxyz" \
              "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
              "0123456789._-"
              
    for i in username:
        if i not in username:
            return False
        
# Domain validation.
    if not domain:
        return False
    if "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    if ".." in domain:
        return False

# Extension validation
    extension = domain.split(".")[-1]
    # Extension must be at least 2 characters, (.c is invalid, .com is valid)
    if len(extension) < 2:
        return False
    # Extension can have only letters
    if i in extension:
        if i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return False
    return True

test = "aman@gmail.c"
print(validate_email(test)) 
    

# Password validator.
# Rules: ≥8 chars, uppercase, lowercase, digit, special character.

# Input - Any string the user provides as a password.
# Output - True / False  → is password valid or not. Specific feedback → WHAT exactly is missing. Missing: uppercase letter, digit, special character.
# Password too short (minimum 8 characters).
# Edge Cases - Empty string, only spaces, only lower or digit ot upper, has length but missing upper or lower or digit or special character.
# Algorithm - If empty → immediately return False. "Password cannot be empty"
# Check length: If less than 8 characters → add "too short" to errors. Loop through every character once. After loop check all 4 flags
# Any flag still False → add that to errors list. If errors list is empty → password is valid → True
# If errors list has items → password invalid → False + show errors
# Time complexity- O(num) where num = length of password string
# Space Complexity - O(1) — constant space, Only 4 boolean flags + errors list. Errors list maximum 5 items regardless of password length.
# No extra data structures that grow with input.

def validate_password(password):
    # Define special characters allowed
    special_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    
    # Collect all errors here
    errors = []
    # Empty password
    if not password:
        return False, ["Password cannot be empty"]
    
    # Minimum length
    if len(password) < 8:
        errors.append(f"Too short — {len(password)} chars (minimum 8 required)")
        
    # Character type flag
    has_upper = False
    has_lower = False
    has_digit = False
    has_spaces = False
    has_special = False
    
    for i in password:
        if i.isupper():
            has_upper = True
        if i.islower():
            has_lower = True
        if i.isdigit():
            has_digit = True
        if i in special_chars:
            has_special = True
        if i == " ":
            has_spaces = True
            
    # Build an error messages
    if not has_upper:
        errors.append("Missing uppercase letters (A-Z)")
    if not has_lower:
        errors.append("Missing lowercase letters (a-z)")
    if not has_digit:
        errors.append('Missing digits (0-9)')
    if not has_special:
        errors.append(f"Missing special character ({special_chars[:10]}...)")
    if has_spaces:
        errors.append("Spaces are not allowed")
    
    # Result
    if not errors:
        return True,["Strong Password"]
    else:
        return False, errors
    
# Display function — clean output
def check_password(password):
    is_valid, messages = validate_password(password)
    status = "valid" if is_valid else "invalid"
    print(f"\nPassword : {repr(password)}")
    print(f"Status   : {status}")
    
    if not is_valid:
        print("Issue :")
        for i in messages:
                print(f"  {i}")
    else:
        print(f"  {messages[0]}")
    print("-" * 45)
    
test_password = ("Aman!1234")
check_password(test_password)

############ OR ################

def validate_password(password):
    special_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    
    rules = [
        (lambda p: len(p) >=8,
         "too short, Minimum 8 characters required"),
        (lambda p: any(i.isupper() for i in p),
         "Missing uppercase letter (A-Z)"),
        (lambda p: any(i.islower() for i in p),
         "Missing lowercase letter (a-z)"),
        (lambda p: any(i.isdigit() for i in p),
         "Missing digit (0-9)"),
        (lambda p: any(i in special_chars for i in p),
         "Missing special characters"),
        (lambda p: " " not in p,
         "Spaces are not allowed")              
    ]
    
    if not password:
        return False,["Password cannot be empty"]
    errors = [msg for rule, msg in rules if not rule(password)]
    
    is_valid = len(errors) == 0
    return is_valid,["Strong Password"] if is_valid else errors

def check_password(password):
    is_valid, messages = validate_password(password)
    status = "VALID" if is_valid else "INVALID"

    print(f"\nPassword : {repr(password)}")
    print(f"Status   : {status}")
    for msg in messages:
        tag = "  " if is_valid else "  →"
        print(f"          {tag} {msg}")
    print("-" * 45)
    
test_password = ("Aman1234")
check_password(test_password)
 
# Username validator.
# Rules: no spaces, starts with letter, only letters digits underscore.

def validate_username(username):
    rules = [(
        lambda p: len(p) >0,
        "Username cannot be empty"),
        (lambda p: p[0].isalpha() if p else False,
         "Must start with letters (a-z) or (A-Z)"),
        (lambda p: " " not in p,
         "Spaces are not allowed"),
        (lambda p: all(c.isalnum() or c == "_" for c in p),
         "Only letters, digits, and underscore (_) allowed")
    ]
    
    if not username:
        return False, ["Username cannot be empty"]
    
    error = [msg for rule, msg in rules if not rule(username)]
    is_valid = len(error) == 0
    return is_valid,["Valid username"] if is_valid else error

def check_username(username):
    is_valid, messages = validate_username(username)
    status = "Valid" if is_valid else "Invalid"
    
    print(f"\nUsername : {repr(username)}")
    print(f"Status   : {status}")
    for msg in messages:
        tag = "   " if is_valid else "  →"
        print(f"          {tag} {msg}")
    print("-" * 45)

t = "Aman0123"
check_username(t)

# Count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for i in text if i in vowels)

print(count_vowels("Mango"))
    
# Count digits
def count_digit(digit):
    return sum(1 for i in digit if i.isdigit())

print(count_digit("aman012364"))

# Count spaces
def count_spaces(text):
    return sum(1 for i in text if i == " ")

print(count_spaces("am a num"))

# Find largest number
def largest_num(digit):
    if not digit:
        return None
    largest = digit[0]
    for i in digit:
        if i > largest:
            largest = i
    return largest

print(largest_num([1, 9, 3, 7]))

# Find smallest number
def smallest_num(digit):
    if not digit:
        return None
    small_num = digit[0]
    for i in digit:
        if i < small_num:
            small_num = i
    return small_num
    
print(smallest_num([32,23,43,6]))

# Sum only even numbers
def sum_even(digit):
    return sum(i for i in digit if i %2 == 0)

print(sum_even([2,3,4,5,6]))

# Reverse a string (without slicing)
def reverse_string(text):
    string = " "
    for i in text:
        string = i + string
    return string

print(reverse_string("Batman")) 

# Remove duplicates
def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 1]))

# Find longest word
def longest_word(text):
    word = text.split()
    if not word:
        return None
    longest = word[0]
    for i in word:
        if len(i) > len(longest):
            longest = i
    return longest

print(longest_word("I love programming"))

# Count consonants.
def count_consonants(text):
    vowels = ("aeiouAEIOU")
    return sum(1 for i in text if i.isalpha() and i not in vowels)

print(count_consonants("Fight123"))

# Count uppercase letters.
def count_uppercase(text):
    return sum(1 for i in text if i.isupper())

print(count_uppercase("AmanKumar"))

# Count lowercase letters.
def count_lowercase(text):
    return sum(1 for i in text if i.islower())

print(count_lowercase("AMANKUMar"))

# Count special characters.
def count_special(text):
    special_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    return sum(1 for i in text if i in special_chars)

print(count_special("Sun@123#"))

# Find the second largest number.
def  second_largest(num):
    if len(num) < 2:
        return None
    first = second = float('-inf')
    for i in num:
        if i > first:
            second = first
            first = i
        elif i > second and i != first:
            second = i
            
    return second if second != float('-inf') else None

print(second_largest([10, 20, 4, 45, 99]))

# Find the second smallest number.
def second_smallest(num):
    if len(num) < 2:
        return None
    first = second = float('inf')
    for i in num:
        if i < first:
            second = first
            first = i
        elif i < second and i != first:
            second = i
    return second if second != float('inf') else None
        
print(second_smallest([10, 20, 4, 45, 99]))

# Find the first negative number.
def first_negative(num):
    for i in num:
        if i < 0:
            return i
    return None

print(first_negative([5, -2, -7, 10]))

# Find the index of the first vowel.
def first_vowel_index(text):
    vowel = "aeiouAEIOU"
    for idx, i in enumerate(text):
        if i in vowel:
            return idx
    return None

print(first_vowel_index("Python")) 

# Average of odd numbers only.
def avg_odd_count(num):
    odds = [i for i in num if i % 2 != 0]
    if not odds:
        return None
    return sum(odds) / len(odds)

print(avg_odd_count([1, 2, 3, 4, 5]))

# Product of all positive numbers.
def product_of_positive(num):
    product = 1
    found = False
    for i in num:
        if i > 0:
            product *= i
            found = True
    return product if found else None

print(product_of_positive([2, -2, 3, 4]))     

# Difference between largest and smallest.
def difference_max_min(num):
    if not num:
        return None
    return max(num) - min(num)

print(difference_max_min([2,3,4,5,6]))

# Return only prime numbers.
def is_prime(num):
    if num <=1:
        return False
    if num == 2:
        return False
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def primes_only(nums):
    return [num for num in nums if is_prime(num)]

print(primes_only([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Return words longer than five letters.
def word_more_then_5(text):
    word = text.split()
    return[i for i in word if len(i) > 5]

print(word_more_then_5("python programing is powerful and enjoyable"))

# Remove all digits from a string.
def remove_digits(text):
    return ''.join(i for i in text if not i.isdigit())

print(remove_digits("Hello123World456")) 

# Return only unique vowels.
def unique_vowels(text):
    vowels = "aeiouAEIOU"
    found = {i.lower() for i in text if i in vowels}
    return sorted(found) if found else None

print(unique_vowels("Programming is powerful"))

# Count occurrences of each character.
def char_count(text):
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

print(char_count("banana"))

# Most frequent word.
from collections import Counter

def most_frequent_word(text):
    word = text.split()
    count = Counter(word)
    return count.most_common(1)[0]

print(most_frequent_word("apple banana apple orange banana apple"))

# Least frequent character.
def least_frequent_char(text):
    counts = Counter(text)
    min_count = min(counts.values())
    return [ch for ch, cnt in counts.items() if cnt == min_count]

print(least_frequent_char("hello world"))

# Check if two strings are anagrams
def are_anagrams(str1, str2):
    # remove spaces and convert to lowercase for fair comparison
    str1, str2 = str1.replace(" ", "").lower(), str2.replace(" ", "").lower()
    
    # if lengths differ, they can't be anagrams
    if len(str1) != len(str2):
        return False
    
    counts = {}
    
    # count characters in str1
    for ch in str1:
        counts[ch] = counts.get(ch, 0) + 1
    
    # subtract counts using str2
    for ch in str2:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] < 0:
            return False
    
    return True

print(are_anagrams("listen", "silent"))   # True
print(are_anagrams("hello", "world"))     # False

# Rotate a string left by one character
def rotate_left(text):
    if len(text) <= 1:
        return text
    return text[1:] + text[0]

print(rotate_left("Python"))   # "ythonP"

# Count how many numbers in a list are greater than 50.
def num_check(num):
    count = 0
    for i in num:
        if i > 50:
            count += 1
    return count

print(num_check([20, 12, 65, 70, 51, 31]))

# Count how many strings in a list have more than 5 characters.
def string_count(text):
    word = text.split()
    return [i for i in word if len(i) > 5]

print(string_count("Welcome to the fightclub"))

# Given a sentence, count how many words start with a vowel (a, e, i, o, u).
def count_vowel(text):
    vowel = "aeiouAEIOU"
    count = 0
    word = text.split()
    
    for i in word:
        if i[0] in vowel:
            count += 1
    return count

print(count_vowel("Apple is on the orange table"))

# Count how many even numbers exist in a list.
def even_count(num):
    return sum(1 for i in num if i % 2 == 0)

print(even_count([2,3,4,5,6]))

# Count how many times the digit 3 appears across all numbers in a list.
def num_count(num):
    count = 0
    for i in num:
        for j in str(i):
            if j == "3":
                count += 1
    return count

print(num_count([1,1,2,3,0,3,3,0,3,]))

# Given a list of temperatures, count how many days were above 35°C.
def check_temp(temperatures):
    count = 0
    for i in temperatures:
        if i > 35:
            count += 1
    return count

print(check_temp([12,35,39,85,52]))

# Count how many negative numbers are in a list.
def count_negative(num):
    count = 0
    for i in num:
        if i < 0:
            count += 1
    return count

print(count_negative([0,-1,5,8,-3]))

# Given a list of words, count how many are palindromes.
def palindrome(text):
    replace = []
    for i in text:
        if i.isalnum():
            replace += i.lower()
    return replace == replace[::-1]

print(palindrome("Nitin"))


# Count how many numbers in a list are divisible by both 3 and 5.
def check_num(num):
    return sum(1 for i in num if i % 3 == 0 and i % 5 == 0)

print(check_num([12,34,30,15,50]))

# Given a list of student scores, count how many students passed (score >= 40).
def check_score(score):
    count_pass = 0
    for i in score:
        if i >= 40:
            count_pass += 1
    return count_pass

print(check_score([23,52,47,65,12]))            

# Count how many characters in a string are uppercase letters.
def uppercase_count(text):
    count = 0
    for i in text:
        if i.isupper():
            count += 1
    return count

print(uppercase_count("HelloWorld"))

# Given a list of lists, count how many inner lists have more than 3 elements.
def count_long_lists(data):
    count = 0
    for i in data:
        if len(i) > 3:
            count += 1
    return count

print(count_long_lists([[1,2,3], [4,5,6,7], [8], [9,10,11,12,13]]))

# Count how many numbers in a list are perfect squares.
import math
def count_perfect_square(num):
    count = 0
    for i in num:
        if i >= 0:
            root = int(math.sqrt(i))            
            if root * root == i:
                count += 1
    return count

print(count_perfect_square([4, 9, 15, 16, 20, 25]))


# Given a list of emails, count how many contain the word "gmail".
def count_gmail(gmail):
    count = 0
    for i in gmail:
        if "gmail" in i.lower():
            count += 1
    return count

print(count_gmail(["abc@gmail.com", "xyz@yahoo.com", "test@GMAIL.com", "hello@outlook.com"]))

# Count how many numbers in a list are between 10 and 50 (inclusive).
def num_check(num):
    count = 0
    for i in num:
        if i >=10 and i <= 50:
            count += 1
    return count

print(num_check([5, 10, 25, 50, 60, 45]))

# Given a string, count how many words have exactly 4 letters.
def check_word_len(word):
    count = 0
    words = word.split()
    for i in words:
        if len(i) == 4:
            count += 1
    return count

print(check_word_len("This code will find four word tests"))

# Count how many elements in a list appear more than once.
def count_duplicates(num):
    count = 0
    for i in set(num):
        if num.count(i) > 1:
            count += 1
    return count

print(count_duplicates([1, 2, 2, 3, 4, 4, 5, 5, 6]))

# Given a list of prices, count how many items cost less than ₹500.
def check_price(price):
    return sum(1 for i in price if i < 500)

print(check_price([200, 450, 600, 499, 800, 120]))

# Count how many numbers in a list are prime.
def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_prime(nums):
    count = 0
    for i in nums:
        if check_prime(i):
            count += 1
    return count

print(count_prime([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))

# Given a list of dates (as strings "YYYY-MM-DD"), count how many fall in the year 2023.
def count_2023_dates(date):
    count = 0
    for i in date:
        if i.startswith('2023-'):
            count += 1
    return count

print(count_2023_dates(["2023-01-15", "2022-12-31", "2023-07-20", "2024-03-10"]))

# Find the first number in a list that is divisible by 7.
def check_devisible(num):
    for i in num:
        if i % 7 == 0:
            return i
    return None

print(check_devisible([5, 10, 14, 20, 28]))  

# Search for a name in a list and return its index. If not found, return -1.
def search_index(name, target):
    for i in range(len(name)):
        if name[i] == target:
            return i
    return -1

print(search_index(["Aman", "Ravi", "Priya", "Neha"], "Priya"))

# Find the last occurrence of a given element in a list.
def last_occurance(lst,target):
    for i in range(len(lst)-1,-1,-1):
        if lst[i] == target:
            return i
    return -1

print(last_occurance([1,2,3,2,4,5,2],2))

# Given a list of words, find the first word that has more than 8 characters.
def check_word_len(text):
    word = text.split()
    for i in word:
        if len(i) > 8:
            return i
    return None

print(check_word_len("This sentence contains extraordinary words"))

# Search a list of numbers and return the first negative number found.
def negative_num(num):
    for i in num:
        if i < 0:
            return i
    return None

print(negative_num([0,1,3,-1,9,-2]))

# Given a list of dictionaries (each with a "name" key), find the dictionary where name equals "Aman".
def find_person(name):
    for i in name:
        if i.get("name") == "Aman":
            return i
    return None
people = [
    {"name": "Ravi", "age": 25},
    {"name": "Priya", "age": 30},
    {"name": "Aman", "age": 28},
    {"name": "Neha", "age": 22}
]
print(find_person(people))

# Find the index of the maximum value in a list without using max().
def index_of_max(lst):
    if not lst:
        return -1
    
    max_val = lst[0]
    max_index = 0
    
    for i in range(1, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
            max_index = i
    return max_index
print(index_of_max([10, 25, 7, 30, 18]))

# Given a list of strings, find the first string that starts and ends with the same character.
def check_string(text):
    for i in text:
        if i[0] == i[-1]:
            return i
    return None

print(check_string(["apple", "banana", "civic", "level"]))

# Search for the first duplicate in a list (first number that has already appeared before it).
def search_duplicate(num):
    seen = set()
    for i in num:
        if i in seen:
            return i
        seen.add(i)
    return None

print(search_duplicate([3, 5, 2, 4, 5, 6, 2]))

# Given a 2D list (matrix), find the position (row, col) of a target value.
def find_position(matrix,target):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return (i,j)
    return None
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(find_position(matrix,50))            

# Find the first pair of adjacent elements in a list where the second is smaller than the first.
def first_desc_pair(lst):
    for i in range(len(lst) -1):
        if lst[i+1] < lst[i]:
            return (lst[i], lst[i+1])
    return None
print(first_desc_pair([5, 7, 4, 6, 8]))


# Given a list of numbers, find the first number that is greater than the average of the list.
def greater_num(num):
    if not num:
        return None
    avg = sum(num) / len(num)
    for i in num:
        if i > avg:
            return i
    return None
print(greater_num([2, 4, 6, 8]))

# Search a string for the first character that appears more than once.
def first_duplicate_num(text):
    seen = set()
    for i in text:
        if i in seen:
            return i
        seen.add(i)
    return None
print(first_duplicate_num("programming"))


# Given a list of tuples (name, score), find the name of the person with the highest score.
def highest_socre(data):
    if not data:
        return None
    max_name, max_score = data[0]
    for i, j in data[1:]:
        if j > max_score:
            max_name, max_score = i, j
    return max_name

people = [("Ravi", 85), ("Priya", 92), ("Aman", 95), ("Neha", 88)]
print(highest_socre(people))

# Find the first missing positive integer in an unsorted list.
def missing_num(num):
    num = set(num)
    i = 1
    while True:
        if i not in num:
            return i
        i += 1
print(missing_num([3, 4, -1, 1]))
    
# Given a list of words, find the first word that is a substring of the next word.
def first_substring(text):
    for i in range(len(text)-1):
        if text[i] in text[i+1]:
            return text[i]
    return None
print(first_substring(["car", "cartoon", "dog", "cat"]))

# Search a list for the first number that is both even and greater than 100.
def even_greater_num(num):
    for i in num:
        if i % 2 == 0 and i > 100:
            return i
    return None
print(even_greater_num([50, 75, 102, 99, 200]))

# Given a list of prices, find the first item where price drops compared to the previous item.
def first_price_drop(price):
    for i in range(1, len(price)):
        if price[i] < price[i-1]:
            return price[i]
    return None
print(first_price_drop([100, 120, 115, 130, 125]))

# Find the index of the second occurrence of a given value in a list.
def second_occurance(lst,target):
    count = 0
    for i in range(len(lst)):
        if lst[i] == target:
            count += 1
            if count == 2:
                return i
    return None
print(second_occurance([10, 20, 30, 20, 40, 20], 20))
        
# Given a list of sentences, find the first sentence that contains more than 5 words.
def first_sentence_more_than_5_words(sentences):
    for sentence in sentences:
        if len(sentence.split()) > 5:
            return sentence
    return None
sentences = [
    "I love Python",
    "Python is very easy to learn and use",
    "Hello World"
]

print(first_sentence_more_than_5_words(sentences))

# Find the sum of all odd numbers from 1 to n.
def sum_of_odds(num):
    total = 0
    for i in range(1, num + 1):
        if i % 2 != 0:
            total += i
    return total

print(sum_of_odds(10))

# Calculate the product of all numbers in a list (without using any built-in).
def prod_of_num(num):
    result = 1
    for i in num:
        result *= i
    return result

print(prod_of_num([5,1,2,6]))

# Build a new list containing only the squares of numbers from 1 to n.
def square_of_n(n):
    result = []
    for i in range(1, n + 1):
        result.append( i * i)
    return result

print(square_of_n(10))

# Concatenate all strings in a list into a single string, separated by " | ".
def concat_strings(text):
    result = " "
    for i in range(len(text)):
        result += text[i]
        if i != len(text) - 1:
            result += " | "
    return result

print(concat_strings(["SQL", "Python", "Pandas"]))

# Find the sum of all digits of a given number (e.g., 1234 → 10).
def digit_sum(number):
    number = abs(number)
    digits = str(number)
    total = 0
    for ch in digits:
        total += int(ch)
    return total
tests = [1234, 9999, 0, -456, 100, 5, 999999, -1000]

# Loop through list — pass ONE number at a time
for n in tests:
    print(f"{n:>10}  →  digit sum = {digit_sum(n)}")

# Build a running total list: given [1,2,3,4], produce [1,3,6,10].
def running_total(num):
    result = []
    total = 0
    for i in num:
        total += i
        result.append(total)
    return result

print(running_total([1,2,3,4,5]))

# Compute the sum of every alternate element in a list (index 0, 2, 4...).
def sum_alternate(num):
    total = 0
    for i in range(0, len(num),2):
        total += num[i]
    return total

# ---------- OR --------------
def sum_alternate(num):
    return sum(num[::2])

print(sum_alternate([0,1,3,5,9]))

# Given a list of words, build a new list of their lengths.
def len_word(word):
    result = []
    for i in word:
        result.append(len(i))
    return result

print(len_word(["SQL", "Python", "Data", "Science"]))

# Calculate the sum of squares of all numbers from 1 to n.
def sum_of_square(num):
    result = 0
    for i in range(1, num +1):
        result += i * i
    return result

print(sum_of_square(5))

# Given a list of prices with a 10% discount, build a list of discounted prices.
def discounted_price(price):
    result = []
    for i in price:
        result.append(i * 0.9)
    return result

print(discounted_price([100, 250, 400]))

# Find the product of only the positive numbers in a list.
def positive_num(num):
    result = 1
    found = False
    for i in num:
        if i > 0:
            result *= i
            found = True
    return result if found else 0

print(positive_num([2, -3, 4, 0, 5]))

# Build a string that reverses each word in a sentence but keeps word order. (e.g., "hello world" → "olleh dlrow")
def reverse_words(text):
    word = text.split()
    result = []
    for i in word:
        result.append(i[::-1])
    return " ".join(result)

print(reverse_words("Hello World"))        

# Accumulate a list of only unique elements from a given list, preserving order.
def unique_element(item):
    result = []
    seen = set()
    for i in item:
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result

print(unique_element([1,1,1,2,4,3,3,4,5]))

# Given a list of numbers, build a new list where each element is the difference from the previous element. First element stays as is.
def diff_element(num):
    if not num:
        return []
    result = [num[0]]
    for i in range(1,len(num)):
        diff = num[i] - num[i-1]
        result.append(diff)
    return result

print(diff_element([1,2,4,5]))

# Find the sum of all numbers in a list that are greater than the running average up to that point.
def sum_greater_then_running(num):
    total_sum = 0
    running_sum = 0
    count = 0
    for i in num:
        count += 1
        running_sum += i
        running_avg = running_sum / count
        if i > running_avg:
            total_sum += i
    return total_sum

print(sum_greater_then_running([2, 4, 6, 8]))

# Build a multiplication table for a given number n (1×n to 10×n) as a list.
def math_table(num):
    result = []
    for i in range(1,11):
        result.append(i * num)
    return result

print(math_table(5))

# Given a list of sentences, accumulate a list of word counts per sentence.
def count_senteces(text):
    result = []
    for i in text:
        word = i.split()
        count = len(word)
        result.append(count)
    return result

print(count_senteces(["Python is fun and easy"]))

# Compute the factorial of n using accumulation (no recursion).
def factorial(n):
    count = 1
    for i in range(1, n+1):
        count *= i
    return count

print(factorial(5))

# Given a list of temperatures in Celsius, build a list converted to Fahrenheit.
def celsius_to_fahrenheit(lst):
    result = []
    for i in lst:
        f = (i * 9/5) + 32 
        result.append(f)
    return result

print(celsius_to_fahrenheit([0, 20, 37, 100]))

# Accumulate only the numbers from a mixed list (containing both strings and numbers).
def accumulate_numbers(item):
    result = []
    for i in item:
        if isinstance(i,(int, float)):
            result.append(i)
    return result

print(accumulate_numbers([10, "apple", 3.5, "banana", -2, "42", 7]))

# Filter all even numbers from a list.
def even_filter(num):
    result = []
    for i in num:
        if i % 2 == 0:
            result.append(i)
    return result

print(even_filter([1,2,3,4,5,6,7,8]))

# From a list of words, keep only words longer than 4 characters.
def word_check(text):
    result = []
    word = text.split()
    for i in word:
        if len(i) > 4:
            result.append(i)
    return result

print(word_check("I am amans friend"))
        
# Filter out all negative numbers from a list, keeping only positives.
def filter_positive(num):
    result = []
    for i in num:
        if i > 0:
            result.append(i)
    return result

print(filter_positive([1,2,-3,0,-4,]))

# Given a list of names, return only names that start with "A".
def start_with_a(text):
    result = []
    for i in text:
        if i.startswith("A"):
            result.append(i)
    return result

print(start_with_a(["Aman", "Ravi", "Anita", "Sunil", "Arjun"]))

# From a list of numbers, filter only those divisible by 3 but not by 9.
def filter_division(num):
    result = []
    for i in num:
        if i % 3 == 0 and i % 9 != 0:
            result.append(i)
    return result

print(filter_division([3, 6, 9, 12, 15, 18, 21, 27]))

# Given a list of emails, filter only valid ones (must contain "@" and ".").
def email_check(email):
    result = []
    for i in email:
        if "@" in i and "." in i:
            result.append(i)
    return result

print(email_check([
    "aman@example.com",
    "friend@gmail",
    "test@domain.org",
    "hello.world",
    "user@site.co.in"]))

# Filter all prime numbers from a list of integers.
import math
def check_prime(num):
    if num < 2:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
def filter_number(prime):
    result = []
    for i in prime:
        if check_prime(i):
            result.append(i)
    return result

print(filter_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))

# From a list of dictionaries (each with "age" key), keep only those where age >= 18.
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

# Given a list of strings, filter out any that contain numeric characters.
def filter_numeric(lst):
    result = []
    for i in lst:
        if not any(j.isdigit() for j in i):
            result.append(i)
    return result

print(filter_numeric(["apple", "banana123", "grape", "mango9", "pear"]))

# From a list of numbers, keep only those that appear exactly once.
def unique_num(num):
    result = []
    for i in num:
        if num.count(i) == 1:
            result.append(i)
    return result

print(unique_num([1, 2, 2, 3, 4, 4, 5]))

# Filter all words from a sentence that are not stop words. Stop words = ["is", "the", "a", "an", "and", "to"].
def filter_stop_word(text):
    stop_words = ["is", "the", "a", "an", "and", "to"]
    result = []
    for i in text.split():
        if i.lower() not in stop_words:
            result.append(i)
    return result

print(filter_stop_word("This is the best way to learn and grow"))

# Given a list of tuples (product, price), filter only items where price is between ₹100 and ₹1000.
def filter_product(products):
    result = []
    for name, price in products:
        if 100 <= price <=1000:
            result.append((name,price))
    return result

print(filter_product([("Pen", 50),
    ("Book", 150),
    ("Bag", 950),
    ("Laptop", 45000),
    ("Shoes", 700)]))

# From a list of numbers, keep only those whose digit sum is even.
def digit_sum(num):
    num = abs(num)
    return sum(int(i) for i in str(num))
def even_digit_sum(nums):
    result = []
    for j in nums:
        if digit_sum(j) % 2 == 0:
            result.append(j)
    return result

print(even_digit_sum([13, 28, 19, 22, 45, 100, 77]))
            
# Given a list of strings, filter only those that are valid Python identifiers (no spaces, no special chars, doesn't start with digit).
def filter_valid_string(text):
    result = []
    for i in text:
        if i.isidentifier():
            result.append(i)
    return result

print(filter_valid_string(["name", "first_name", "2ndVar", "hello world", "valid123", "class"]))

# Filter all numbers from a list that are larger than both their neighbours (local maximums).
def local_maximums(num):
    result = []
    if len(num) < 3:
        return result
    for i in range(1, len(num) - 1):
        left = num[i - 1]
        current = num[i]
        right = num[i + 1]
        if current > left and current > right:
            result.append(current)
    return result

print(local_maximums([1, 3, 2, 5, 4, 7, 6]))

# From a list of sentences, filter only sentences that end with a question mark.
def sentence_end(text):
    result = []
    for i in text:
        if i.strip().endswith("?"):
            result.append(i)
    return result

print(sentence_end(["How are you?",
    "This is a statement.",
    "Is this working?",
    "No issues here."]))

# Given a list of numbers, filter those that are perfect cubes.
def is_perfect_cube(lst):
    root = round(abs(lst) ** (1/3))
    return root ** 3 == abs(lst)
def filter_cube(cube):
    result = []
    for i in cube:
        if is_perfect_cube(i):
            result.append(i)
    return result
print(filter_cube([1, 8, 9, 27, 64, 100, -27, -8]))    

# From a mixed list, filter only the string elements.
def filter_strings(item):
    result = []
    for i in item:
        if isinstance(i,str):
            result.append(i)
    return result

print(filter_strings([1, "hello", 3.14, "world", True, "Python", None]))

# Given a list of words, filter only those where all vowels come before all consonants.
def vowel_before_conconent(text):
    vowel = "aeiouAEIOU"
    seen_conconent = False
    for i in text:
        if i in vowel:
            if seen_conconent:
                return False
    else:
        seen_conconent = True
def filter_vowel(word):
    return [j for j in word if vowel_before_conconent(j)]
print(filter_vowel(["aeiobcd", "apple", "iouxyz", "banana", "aeiou", "ooofff"]))

# From a list of numbers, keep only those where the number reversed is also in the list.
def filter_reverse_num(num):
    result = []
    for i in num:
        rev = int(str(i)[::-1])
        if rev in num:
            result.append(i)
    return result

print(filter_reverse_num([12,21, 34, 43, 56, 65, 99, 100]))

# Count the frequency of each character in a string.
def char_frequency(text):
    result = {}
    for i in text:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result
print(char_frequency("hello"))

# Given a list of numbers, find which number appears the most (mode).
def num_appearence(num):
    result = {}
    for i in num:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    mode = max(result,key=result.get)
    return mode
print(num_appearence([1,1,2,3,4,1,5]))

# Count the frequency of each word in a sentence.
def word_frequency(word):
    words = word.split()
    frequency = {}
    for i in words:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency

print(word_frequency("this is a test this is only a test"))            

# Given a list, find all elements that appear exactly twice.
def find_exactly_twice(word):
    freq = {}
    for i in word:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return [i for i, count in freq.items() if count == 2] 
print(find_exactly_twice([1, 2, 2, 3, 3, 3, 4, 4, 5]))

# Count how many times each digit (0–9) appears in a given number.
def count_digit(digit):
    freq = {}
    for i in str(digit):
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
        
print(count_digit(120340560789))
            
# Given a list of scores, count how many fall in each grade band: A(90+), B(75–89), C(60–74), D(below 60).
def grade_distribution(marks):
    band = {"A":0, "B":0, "C":0, "D":0}
    for i in marks:
        if i >= 90:
            band["A"] += 1
        elif i >= 75:
            band["B"] += 1
        elif i >= 60:
            band["C"] += 1
        else:
            band["D"] += 1
    return band
print(grade_distribution([95, 82, 67, 45, 89, 74, 100, 59]))

# Find the least frequent element in a list.
def least_frequent(item):
    freq = {}
    for i in item:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return min(freq, key=freq.get)
print(least_frequent([4, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]))

# Given a paragraph, find the top 3 most frequent words.
def top_3_words(paragraph):
    word = paragraph.lower().split()
    freq = {}
    for i in word:
        i = i.strip(".,!?") 
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    top_3 =  sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3]
    return top_3
print(top_3_words("This is a test. This test is only a test, and this test is important."))
        
# Count the frequency of each vowel in a string.
def vowel_count(words):
    vowel = "aeiou"
    count = {j: 0 for j in vowel}
    for i in words.lower():
        if i in vowel:
            count[i] += 1
    return count
print(vowel_count("Hello Universe"))

# Given a list, return a list of elements that appear more than n times.
def more_than_n(lst, n):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return [i for i, count in freq.items() if count > n]
print(more_than_n([1,2,2,3,3,3,4,4,4,4,5], 3))

# Given a list of words, count how many unique first letters exist.
def unique_first_letter(word):
    unique = set()
    for i in word:
        if i:
            unique.add(i[0].lower())
    return len(unique)
print(unique_first_letter(["apple", "banana", "apricot", "cherry", "date", "blueberry"]))

# Count how many times each unique length appears among a list of strings.
def length_count(items):
    result = {}
    for i in items:
        length =  len(i)
        if length in result:
            result[length] += 1
        else:
            result[length] = 1
    return result
print(length_count(["hi", "hey", "hello", "ok", "bye", "world", "no"]))       

# Given a list of numbers, find all numbers that appear an odd number of times.
def odd_frequency(item):
    odd = {}
    for i in item:
        if i in odd:
            odd[i] += 1
        else:
            odd[i] = 1
    return [i for i, count in odd.items() if count % 2 == 1]
print(odd_frequency([1,2,2,3,3,3,4,4,4,4,5,5,5]))

# Given a list of transactions (positive = credit, negative = debit), count how many of each type.
def type_of_transaction(transaction):
    count = {"positive": 0, "negative": 0}
    for i in transaction:
        if i > 0:
            count["positive"] += 1
        else:
            count["negative"] += 1
    return count
print(type_of_transaction([100, -50, 200, -30, 10, 400]))

# Count the frequency of each day name in a list of date strings (format: "YYYY-MM-DD").
import datetime

def day_name_frequency(dates):
    freq = {}
    for i in dates:
        day = datetime.datetime.strptime(i,"%Y-%m-%d").strftime("%A")
        if day in freq:
            freq[day] += 1
        else:
            freq[day] = 1
    return freq
print(day_name_frequency(["2026-08-06", "2026-08-07", "2026-08-06", "2026-08-08"]))
            
# Given a list of numbers, find the second most frequent element.
def second_most_frequent(lst):
    freq = {}
    for i in lst:
        freq[i] = freq.get(i, 0) + 1
    
    # sort by frequency (highest first)
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    if len(sorted_freq) < 2:
        return None   # not enough unique elements
    return sorted_freq[1][0]   # second most frequent element

print(second_most_frequent([1,2,2,3,3,3,4,4,4,4,5]))         

# Count how many elements in a list appear only once (unique elements).
def unique_elements(words):
    unique = {}
    for i in words:
        unique[i] = unique.get(i,0) + 1
    return sum(1 for count in unique.values() if count == 1)
print(unique_elements([1,2,2,3,4,4,5,6,6,7]))

# Given a sentence, count the frequency of each word length (e.g., "3-letter words: 4 times").
def len_word_freq(lst):
    word = lst.split()
    freq = {}
    for i in word:
        length = len(i)
        freq[length] = freq.get(length, 0) + 1
    return freq
print(len_word_freq("This is a simple test sentence with words of different lengths"))

# Given a list of items, detect if any element appears more than half the total count.
def has_majority_element(lst):
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    half = len(lst) // 2
    for value, count in freq.items():
        if count > half:
            return True, value   
    return False, None        
print(has_majority_element([1,2,2,2,2,3,4]))

# Given two lists, count how many elements are common (appear in both), counting frequency.
def common_count(lst1, lst2):
    frequency_1 = {}
    frequency_2 = {}
    for i in lst1:
        frequency_1[i] = frequency_1.get(i,0) + 1
    for i in lst2:
        frequency_2[i] = frequency_2.get(i,0) + 1
    common_total = 0
    for i in frequency_1:
        if i in frequency_2:
            common_total += min(frequency_1[i],frequency_2[i])
    return common_total
print(common_count([1,2,2,3,3,3,4], [2,2,3,3,5,6,3]))
        
# Given a list of numbers, return True if all numbers are positive.
def number_check(lst):
    for i in lst:
        if i <= 0:
            return False
    return True
print(number_check([1, -2, 3, 4]))

# Check if a list is sorted in ascending order.
def is_sorted_ascending(lst):
    if len(lst) <= 1:
        return True
    for i in range(len(lst) -  1):
        if lst[i] > lst[i + 1]:
            return False
    return True
print(is_sorted_ascending([1, 2, 3, 4, 5]))

# Given a list, return True if any two adjacent elements are equal.
def has_adjacent_equal(lst):
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            return True
    return False
print(has_adjacent_equal([1, 2, 3, 5, 4]))

# Given a number n, check if it is a perfect number (sum of its divisors equals itself). e.g., 6 = 1+2+3.
def is_perfect(lst):
    if lst <= 1:
        return False
    divisors_sum = 0
    for i in range(1,lst):
        if lst % i == 0:
            divisors_sum += i
    return divisors_sum == lst
print(is_perfect(6))

# Given two lists of equal length, return True if they are mirror images of each other.
def are_mirror(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1[i] != lst2[-(i+1)]:
            return False
    return True
print(are_mirror([1,2,3], [3,2,0])) 

# Check if a given string is an anagram of another string.
def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if len(str1) != len(str2):
        return False
    freq1 = {}
    freq2 = {}
    for i in str1:
        freq1[i] = freq1.get(i,0) + 1
    for i in str2:
        freq2[i] = freq2.get(i,0) + 1
    return freq1 == freq2
print(is_anagram("listen", "silent"))
            
# Given a list of numbers, return True if there exists a pair that sums to a given target k.
def has_pair_with_sum(lst, k):
    seen = set()
    for i in lst:
        if (k-i) in seen:
            return True
        seen.add(i)
    return False
print(has_pair_with_sum([1,2,4,5],6))

# Given a number, check if it's a Harshad number (divisible by the sum of its own digits).
def is_harshad(num):
    digit_sum = sum(int(i) for i in str(num))
    return num % digit_sum == 0
print(is_harshad(18)) 

# Given a list, return True if it has more even numbers than odd numbers.
def more_even(num):
    even_count = 0
    odd_count = 0
    for i in num:
        if i %2 == 0:
            even_count += 1
        else:
            odd_count += 1
        return even_count > odd_count
print(more_even([2,4,6,7,9]))

# Given a string, check if all characters are unique (no duplicates).
def unique_string(str):
    seen = set()
    for i in str:
        if i in seen:
            return False
        seen.add(i)
    return True
print(unique_string("abcd"))

# Given a list of numbers, check if any number equals the sum of all others.
def has_equal_sum(num):
    total = sum(num)
    for i in num:
        if i == total - i:
            return True
    return False
print(has_equal_sum([6,1,2,3]))

# Given a word, check if it is a pangram sentence — contains every letter of the alphabet at least once.
import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)     
    letters = set(sentence.lower())            
    return alphabet.issubset(letters)
print(is_pangram("The quick brown fox jumps over the lazy dog"))

# Given a list of numbers, return True if the list contains a "peak" — a number greater than all before it and all after it.
def has_peak(lst):
    for i in range(1, len(lst)-1):          # skip first and last
        if lst[i] > max(lst[:i]) and lst[i] > max(lst[i+1:]):
            return True
    return False

print(has_peak([1,3,2,1]))   # True (3 is peak)
print(has_peak([1,2,3,4]))   # False

# Given two strings, check if one is a rotation of the other (e.g., "abcd" and "cdab").
def is_rotation(s1, s2):
    if len(s1) != len(s2): 
        return False
    return s2 in (s1 + s1)   # rotation must appear in doubled string

print(is_rotation("abcd", "cdab"))  # True
print(is_rotation("abcd", "acbd"))  # False

# Given a list, check if it can be split into two halves with equal sums.
def split_equal_sum(lst):
    if len(lst) % 2 != 0: 
        return False
    mid = len(lst)//2
    return sum(lst[:mid]) == sum(lst[mid:])

print(split_equal_sum([1,2,3,6]))   # True (1+2=3, 3+6=9 → False actually)
print(split_equal_sum([2,2,3,3]))   # True (2+2=4, 3+3=6 → False)

# Given a number n, check if it is a Kaprekar number (e.g., 45² = 2025 → 20+25 = 45).
def is_kaprekar(n):
    sq = str(n*n)
    right = int(sq[-len(str(n)):] or 0)
    left = int(sq[:-len(str(n))] or 0)
    return left + right == n

print(is_kaprekar(45))   # True (2025 → 20+25=45)
print(is_kaprekar(10))   # False

# Given a list of booleans, return True if more than half are True.
def majority_true(lst):
    return sum(lst) > len(lst)//2

print(majority_true([True, True, False]))   # True
print(majority_true([True, False, False]))  # False

# Given a list of numbers, check if removing exactly one element can make the list sorted.
def can_be_sorted(lst):
    count = 0
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            count += 1
            if count > 1:
                return False
    return True

print(can_be_sorted([1,2,5,3,4]))   # True (remove 5)
print(can_be_sorted([3,2,1]))       # False

# Given a string, check if the brackets (), [], {} are balanced and properly nested.
def balanced_brackets(s):
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack

print(balanced_brackets("{[()]}"))   # True
print(balanced_brackets("{[(])}"))   # False

# Given a list of numbers, check if any subset of them (contiguous) sums to exactly zero.
def has_zero_sum_subarray(lst):
    seen = set()
    total = 0
    for num in lst:
        total += num
        if total == 0 or total in seen:
            return True
        seen.add(total)
    return False

print(has_zero_sum_subarray([1,2,-3,4]))   # True (1+2-3=0)
print(has_zero_sum_subarray([1,2,3]))      # False

