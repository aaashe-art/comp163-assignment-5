#Chat gpt was used on lines 6 and 13 to help print in the correct format.

current_number = int(input("Enter starting number: "))
step_count = 0

print(f"Sequence: {current_number}", end=" ")

while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = (current_number * 3) + 1
    print(current_number, end=" ")
    step_count += 1
print(f'\nSteps: {step_count}')

prime_num = int(input("Enter number: "))

while prime_num > 1:
    print(f"Testing divisors from 2 to {prime_num - 1}...")
    for prime_range in range(2, (prime_num)):
        if (prime_num % prime_range) == 0:
            print(f"{prime_num} is not a prime number.")
            break
    else:
        print(f"{prime_num} is a prime number.")
        break