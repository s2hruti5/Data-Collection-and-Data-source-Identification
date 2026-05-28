from typing import List, Any

# 1. Function with return type + *args for reusability
def sum_all(*args: float) -> float:
    """Takes any number of numbers and returns their sum"""
    return sum(args)

# 2. Function with **kwargs to handle named utility options
def create_user(**kwargs: Any) -> dict:
    """Creates user dict from any key-value pairs passed in"""
    user = {"id": 101, "active": True}
    user.update(kwargs) # kwargs is a dict of all named args
    return user

# 3. Lambda functions for quick operations
# Lambda to check if number is even
is_even = lambda x: x % 2 == 0

# Using lambda with built-in functions
def filter_even_numbers(numbers: List[int]) -> List[int]:
    """Uses lambda + filter to keep only even numbers"""
    return list(filter(lambda n: n % 2 == 0, numbers))

# 4. Global vs Local scope demo
global_counter = 0 # Global scope

def increment_counter() -> int:
    global global_counter # Tell Python we want the global var
    local_message = "Incrementing..." # Local scope - only exists here
    global_counter += 1
    print(local_message)
    return global_counter

# Testing everything
if __name__ == "__main__":
    print("Sum of 1,2,3,4:", sum_all(1, 2, 3, 4)) # 10
    
    user1 = create_user(name="Alex", role="intern", team="backend")
    print("User created:", user1)
    
    nums = [1, 2, 3, 4, 5, 6]
    print("Evens from list:", filter_even_numbers(nums)) # [2, 4, 6]
    print("Is 8 even?", is_even(8)) # True
    
    increment_counter()
    print("Global counter:", global_counter) # 1