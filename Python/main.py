# 50 Problem Solving Questions and Answers in Python

# 1. Reverse a String
def reverse_string(s):
    return s[::-1]

# 2. Check if a Number is Prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 3. Palindrome Check
def is_palindrome(s):
    return s == s[::-1]

# 4. First Non-Repeating Character
def first_non_repeating(s):
    for c in s:
        if s.count(c) == 1:
            return c
    return None

# 5. Find Duplicates in List
def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

# 6. Missing Number in Array
def missing_number(arr, n):
    return n * (n + 1) // 2 - sum(arr)

# 7. Factorial (Recursive)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 8. Fibonacci Series (List)
def fibonacci(n):
    a, b = 0, 1
    fib_series = []
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# 9. Count Vowels in String
def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')

# 10. Sum of Digits of Number
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

# 11. Armstrong Number Check
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == n

# 12. Anagram Check
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# 13. Find Maximum and Minimum in List
def find_max_min(lst):
    return max(lst), min(lst)

# 14. Count Words in Sentence
def count_words(sentence):
    return len(sentence.split())

# 15. Remove Duplicates from List
def remove_duplicates(lst):
    return list(set(lst))

# 16. Check Leap Year
def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

# 17. Reverse Integer Number
def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n_abs = abs(n)
    rev = int(str(n_abs)[::-1])
    return sign * rev

# 18. Count Even and Odd Numbers in List
def count_even_odd(lst):
    even = sum(1 for x in lst if x % 2 == 0)
    odd = len(lst) - even
    return even, odd

# 19. Greatest Common Divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 20. Least Common Multiple (LCM)
def lcm(a, b):
    return abs(a*b) // gcd(a, b)

# 21. Perfect Number Check
def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

# 22. Binary to Decimal Conversion
def binary_to_decimal(b):
    return int(b, 2)

# 23. Decimal to Binary Conversion
def decimal_to_binary(n):
    return bin(n)[2:]

# 24. Valid Palindrome (ignore non-alphanumeric)
import re
def is_valid_palindrome(s):
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

# 25. Merge Two Sorted Lists
def merge_sorted_lists(a, b):
    return sorted(a + b)

# 26. Count Characters Frequency in String
from collections import Counter
def count_characters(s):
    return dict(Counter(s))

# 27. Intersection of Two Lists
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# 28. Check if List is Sorted
def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

# 29. Remove Vowels from String
def remove_vowels(s):
    return ''.join(c for c in s if c.lower() not in 'aeiou')

# 30. Find Second Largest Number in List
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2] if len(unique) > 1 else None

# 31. Word Frequency Count
def word_frequency(sentence):
    words = sentence.lower().split()
    return dict(Counter(words))

# 32. Check if Number is Power of Two
def is_power_of_two(n):
    return n > 0 and (n & (n-1)) == 0

# 33. Sum of First N Natural Numbers
def sum_natural(n):
    return n*(n+1)//2

# 34. Find Duplicate Characters in String
def duplicate_characters(s):
    counts = Counter(s)
    return [ch for ch, cnt in counts.items() if cnt > 1]

# 35. Find Missing Elements Between Two Lists
def missing_elements(lst1, lst2):
    return list(set(lst1) - set(lst2))

# 36. Find Longest Word in Sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# 37. Remove Spaces from String
def remove_spaces(s):
    return s.replace(' ', '')

# 38. Check if Two Strings are Rotations of Each Other
def are_rotations(s1, s2):
    return len(s1) == len(s2) and s2 in s1 + s1

# 39. Factorial (Iterative)
def factorial_iter(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# 40. Sum of Even Numbers in List
def sum_even(lst):
    return sum(x for x in lst if x % 2 == 0)

# 41. Count Digits in Number
def count_digits(n):
    return len(str(abs(n)))

# 42. Find Most Frequent Element in List
def most_frequent(lst):
    counts = Counter(lst)
    return counts.most_common(1)[0][0]

# 43. Check if Number is Palindrome
def is_palindrome_number(n):
    s = str(n)
    return s == s[::-1]

# 44. Find All Primes up to N
def primes_upto_n(n):
    return [x for x in range(2, n+1) if is_prime(x)]

# 45. Calculate Power (Iterative)
def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

# 46. Find Index of Element in List
def find_index(lst, target):
    for i, val in enumerate(lst):
        if val == target:
            return i
    return -1

# 47. Flatten Nested List
def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

# 48. Count Words Starting with Specific Letter
def count_words_starting_with(sentence, letter):
    return sum(1 for word in sentence.split() if word.lower().startswith(letter.lower()))

# 49. Celsius to Fahrenheit Conversion
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# 50. Length of Longest Substring Without Repeating Characters
def length_of_longest_substring(s):
    start = max_len = 0
    used = {}
    for i, ch in enumerate(s):
        if ch in used and start <= used[ch]:
            start = used[ch] + 1
        else:
            max_len = max(max_len, i - start + 1)
        used[ch] = i
    return max_len


# ------------ Test all functions with examples -------------

if __name__ == "__main__":
    print("1.", reverse_string("hello"))
    print("2.", is_prime(7))
    print("3.", is_palindrome("madam"))
    print("4.", first_non_repeating("aabbcde"))
    print("5.", find_duplicates([1,2,3,2,4,1]))
    print("6.", missing_number([1,2,4,5], 5))
    print("7.", factorial(5))
    print("8.", fibonacci(7))
    print("9.", count_vowels("Hello World"))
    print("10.", sum_of_digits(1234))
    print("11.", is_armstrong(153))
    print("12.", is_anagram("listen", "silent"))
    print("13.", find_max_min([3,6,1,9]))
    print("14.", count_words("Hello from the other side"))
    print("15.", remove_duplicates([1,2,2,3,4,4,5]))
    print("16.", is_leap_year(2024))
    print("17.", reverse_integer(-1234))
    print("18.", count_even_odd([1,2,3,4,5]))
    print("19.", gcd(36, 60))
    print("20.", lcm(12, 15))
    print("21.", is_perfect(28))
    print("22.", binary_to_decimal("1010"))
    print("23.", decimal_to_binary(10))
    print("24.", is_valid_palindrome("A man, a plan, a canal: Panama"))
    print("25.", merge_sorted_lists([1,3,5], [2,4,6]))
    print("26.", count_characters("hello"))
    print("27.", intersection([1,2,3], [2,3,4]))
    print("28.", is_sorted([1,2,3,4]))
    print("29.", remove_vowels("hello world"))
    print("30.", second_largest([5,3,9,1]))
    print("31.", word_frequency("hello hello world"))
    print("32.", is_power_of_two(16))
    print("33.", sum_natural(10))
    print("34.", duplicate_characters("programming"))
    print("35.", missing_elements([1,2,3], [2,3]))
    print("36.", longest_word("hello from the world"))
    print("37.", remove_spaces("hello world"))
    print("38.", are_rotations("abcde", "deabc"))
    print("39.", factorial_iter(5))
    print("40.", sum_even([1,2,3,4,5,6]))
    print("41.", count_digits(-12345))
    print("42.", most_frequent([1,2,2,3,3,3]))
    print("43.", is_palindrome_number(121))
    print("44.", primes_upto_n(20))
    print("45.", power(2, 5))
    print("46.", find_index([1,2,3,4], 3))
    print("47.", flatten([1, [2, 3], [4, [5]]]))
    print("48.", count_words_starting_with("hello hi how", 'h'))
    print("49.", celsius_to_fahrenheit(0))
    print("50.", length_of_longest_substring("abcabcbb"))
