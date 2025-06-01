# 1. Two Sum
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# 2. Reverse a String
def reverse_string(s):
    return s[::-1]

# 3. Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# 4. Palindrome Check
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# 5. FizzBuzz
def fizzbuzz(n):
    for i in range(1, n+1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        print(output or i)

# 6. Anagram Check
from collections import defaultdict

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = defaultdict(int)
    for c in s1:
        freq[c] += 1
    for c in s2:
        freq[c] -= 1
        if freq[c] < 0:
            return False
    return True

# 7. Maximum Subarray (Kadane's Algorithm)
def max_subarray(nums):
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

# 8. Merge Two Sorted Lists
def merge_sorted_lists(l1, l2):
    merged = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
    merged.extend(l1[i:])
    merged.extend(l2[j:])
    return merged

# 9. Binary Search
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 10. Linked List Cycle Detection
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# --- TEST CASES ---
if __name__ == "__main__":
    # Test Two Sum
    print("1. Two Sum:", two_sum([2, 7, 11, 15], 9))  # [0, 1]

    # Test Reverse String
    print("2. Reverse String:", reverse_string("hello"))  # "olleh"

    # Test Fibonacci
    print("3. Fibonacci:", fibonacci(10))  # 55

    # Test Palindrome
    print("4. Is Palindrome:", is_palindrome("A man, a plan, a canal: Panama"))  # True

    # Test FizzBuzz (prints to console)
    print("5. FizzBuzz (1-15):")
    fizzbuzz(15)

    # Test Anagram
    print("6. Is Anagram:", is_anagram("listen", "silent"))  # True

    # Test Maximum Subarray
    print("7. Maximum Subarray:", max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6

    # Test Merge Sorted Lists
    print("8. Merge Sorted Lists:", merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]

    # Test Binary Search
    print("9. Binary Search:", binary_search([1, 2, 3, 4, 5], 3))  # 2

    # Test Linked List Cycle
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle
    print("10. Has Cycle:", has_cycle(node1))  # True