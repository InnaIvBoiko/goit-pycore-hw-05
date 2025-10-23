"""Module for creating a caching Fibonacci function using closures."""

def caching_fibonacci() -> callable:
    """Create a caching Fibonacci function using closure.
    
    Creates and returns a Fibonacci function that uses memoization
    to cache previously computed values for improved performance.
    
    Returns:
        callable: A Fibonacci function with built-in caching
    """
    cache = {}

    def fibonacci(n: int) -> int:
        """Calculate the nth Fibonacci number with caching.
        
        Args:
            n (int): The position in the Fibonacci sequence
            
        Returns:
            int: The nth Fibonacci number
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Example usage:

fib = caching_fibonacci()

print(fib(10))
print(fib(15))