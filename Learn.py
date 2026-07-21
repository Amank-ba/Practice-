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
def avg_odd_num(num):
    odds = [i for i in num if i % 2 != 0]
    if not odds:
        return None
    return sum(odds) / len(odds)

print(avg_odd_num([1, 2, 3, 4, 5]))

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
# Count how many strings in a list have more than 5 characters.
# Given a sentence, count how many words start with a vowel (a, e, i, o, u).
# Count how many even numbers exist in a list.
# Count how many times the digit 3 appears across all numbers in a list.
# Given a list of temperatures, count how many days were above 35°C.
# Count how many negative numbers are in a list.
# Given a list of words, count how many are palindromes.
# Count how many numbers in a list are divisible by both 3 and 5.
# Given a list of student scores, count how many students passed (score >= 40).
# Count how many characters in a string are uppercase letters.
# Given a list of lists, count how many inner lists have more than 3 elements.
# Count how many numbers in a list are perfect squares.
# Given a list of emails, count how many contain the word "gmail".
# Count how many numbers in a list are between 10 and 50 (inclusive).
# Given a string, count how many words have exactly 4 letters.
# Count how many elements in a list appear more than once.
# Given a list of prices, count how many items cost less than ₹500.
# Count how many numbers in a list are prime.
# Given a list of dates (as strings "YYYY-MM-DD"), count how many fall in the year 2023.