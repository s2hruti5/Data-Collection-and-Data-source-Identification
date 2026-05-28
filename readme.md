#DELIVERABLES
UNDERSTAND BY TWO WAYS
1ST WAY:-
What are Lambda functions? 
Lambda functions are small, anonymous functions defined with the lambda keyword. They can take any number of arguments but only one expression. 
Syntax: lambda arguments: expressionUse case: Quick, throwaway functions for things like map, filter, sort where you don’t need a full def
Example: square = lambda x: x _ x

Global vs Local scope? 
1.Local scope: Variables defined inside a function. They only exist while the function runs and can’t be accessed outside.
2.Global scope: Variables defined at the top level of a script/module. They can be accessed anywhere in the file after they’re defined.
3.Key rule:  If you want to modify a global variable inside a function, use the global keyword. Otherwise Python creates a new local variable.


2ND WAY:-
A. What are Lambda functions?
Anonymous = no def and no name neededOne expression only = can’t do if/else blocks, loops inside Used for short, throwaway operationsReturn value is automatic — no return keyword neededWhen not to use: If the logic is complex, use def. Lambdas should be readable at a glance.

B. Global vs Local scope?
Scope = “where can I access this variable?”pythonx = 10 # Global scope - defined in main body of file

def my_func():
    y = 5 # Local scope - only exists inside my_func
    print(x) # Can read global x = 10
    print(y) # Can read local y = 5

my_func()
print(x) # Works, x is global
print(y) # Error! y doesn’t exist outside the functionThe LEGB rule: Python looks for variables in this order → Local → Enclosing → Global → Built-in.To change a global inside a function:pythoncount = 0
def increment():
    global count # Without this line, Python would make a NEW local `count`
    count += 1
