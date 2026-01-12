# Parameter -  is the value we provide to a function when we make(define) it.
# Argument - is the value we provide to a function when we call(invoke) it.


# Default Parameters
def greet(name='Sumayla'):
    print(f'Hii {name}, How are You!')

greet(name='Dev')


# --------------------------

def employee_info(name, position):
    print(f"Hello {name} !You are {position}")

# employee_info('Dev', 'CEO')
# employee_info('Sanjay', 'CTO')

# name and position are parameters while Dev, sanjay, CEO, CTO are the arguments.

# --------------------------

# Keyword args
def say_something(name='Dev', msg='Good'):
    print(f'Hii {name}, You are {msg}')
    
say_something( 'good', 'Dev')
say_something('dev')   
say_something(msg='bad', name='Krish')
