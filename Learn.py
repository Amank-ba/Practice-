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