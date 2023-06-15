# 1. Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, find the sum of digits in all numbers from 1 to n.
#Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

def sum (n):
    end_result = 0
    for x in range (n + 1):
        end_result = end_result + x
    return end_result

test_data = 5
test_result = sum(test_data)
print(test_result)

#2.Find the max number from 3 values.
#Example: 124, 21, 32. Result = 124.

def max(a, b, c):
    if a > b and b > c:
        return a
    if b > a and b > c:
        return b
    else:
        return c

result = max(5, 10, 20)
print(result)


#3. Count odd and even numbers. Count odd and even digits of the whole number.
#Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

def count_odds_even(num):
    odds = 0
    evens = 0

    while num != 0:
        current_digit = num % 10
        if current_digit % 2:
            odds += 1
        else:
            evens +=1
        num = num //10
    print(f"Evens: {evens}, Odds: {odds}")

test_number = 14570
count_odds_even(test_number)

