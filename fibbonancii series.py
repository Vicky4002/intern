def generate_fibonacci_up_to(limit):
    fibonacci_sequence = []
    a, b = 0, 1
    
    while a <= limit:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    return fibonacci_sequence

def main():
    try:
        limit = int(input("Enter the limit for the Fibonacci sequence: "))
        if limit < 0:
            raise ValueError("The limit must be a non-negative integer.")
        
        fibonacci_sequence = generate_fibonacci_up_to(limit)
        print("Fibonacci sequence up to", limit, ":", fibonacci_sequence)
    
    except ValueError as e:
        print("Invalid input:", e)

if __name__ == "__main__":
    main()
