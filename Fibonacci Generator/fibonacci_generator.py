def fibonacci_generator(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

def fibonacci_infinite():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def print_fibonacci(count):
    sequence = fibonacci_generator(count)
    print(f"First {count} Fibonacci numbers:")
    print(sequence)

def print_fibonacci_up_to(limit):
    print(f"Fibonacci numbers up to {limit}:")
    for num in fibonacci_infinite():
        if num > limit:
            break
        print(num, end=" ")
    print()

if __name__ == "__main__":
    print("Fibonacci Sequence Generator")
    print("=" * 30)
    
    print_fibonacci(10)
    print()
    
    print_fibonacci_up_to(100)
    print()
    
    print("First 15 Fibonacci numbers using generator:")
    fib_gen = fibonacci_infinite()
    for i in range(15):
        print(next(fib_gen), end=" ")
    print()
    
    input("\nPress Enter to exit...")
