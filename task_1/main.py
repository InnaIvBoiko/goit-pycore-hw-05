# Function to create a caching Fibonacci function

def caching_fibonacci() -> callable:
    cache = {} # Dictionary to store previously computed Fibonacci numbers

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0 # Return 0 for non-positive integers
        elif n == 1:
            return 1 # Base case: Fibonacci(1) = 1
        elif n in cache:
            return cache[n] # Return cached value if it exists
        else:
            # Compute Fibonacci recursively and store in cache
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Example usage:

fib = caching_fibonacci()

print(fib(10))  # 55
print(fib(15))  # 610