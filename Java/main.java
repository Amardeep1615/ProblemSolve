

# ----------------------------
# JAVA QUESTIONS WITH FULL CODE
# ----------------------------

// Java problems are listed below. Each class has a main method that can be compiled and executed.

// 1. Reverse a String
class ReverseString {
    public static void main(String[] args) {
        String input = "hello";
        StringBuilder reversed = new StringBuilder(input).reverse();
        System.out.println("Reversed: " + reversed);
    }
}

// 2. Check Prime Number
class PrimeCheck {
    public static void main(String[] args) {
        int num = 17;
        boolean isPrime = true;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                isPrime = false;
                break;
            }
        }
        System.out.println(num + " is prime? " + isPrime);
    }
}

// 3. Fibonacci Series up to N terms
class Fibonacci {
    public static void main(String[] args) {
        int n = 10, a = 0, b = 1;
        for (int i = 0; i < n; i++) {
            System.out.print(a + " ");
            int temp = a + b;
            a = b;
            b = temp;
        }
    }
}

// 4. Factorial of a Number
class Factorial {
    public static void main(String[] args) {
        int n = 5;
        long fact = 1;
        for (int i = 1; i <= n; i++) {
            fact *= i;
        }
        System.out.println("Factorial: " + fact);
    }
}

// 5. Palindrome Check
class PalindromeCheck {
    public static void main(String[] args) {
        String str = "madam";
        String reversed = new StringBuilder(str).reverse().toString();
        System.out.println("Is Palindrome? " + str.equals(reversed));
    }
}

// 6. Armstrong Number
class ArmstrongNumber {
    public static void main(String[] args) {
        int num = 153, sum = 0, original = num;
        while (num > 0) {
            int digit = num % 10;
            sum += Math.pow(digit, 3);
            num /= 10;
        }
        System.out.println(original + " is Armstrong? " + (original == sum));
    }
}

// 7. Swap Two Numbers
class SwapNumbers {
    public static void main(String[] args) {
        int a = 5, b = 10;
        a = a + b;
        b = a - b;
        a = a - b;
        System.out.println("a = " + a + ", b = " + b);
    }
}

// 8. Find Largest of Three Numbers
class LargestOfThree {
    public static void main(String[] args) {
        int a = 5, b = 7, c = 3;
        int largest = Math.max(a, Math.max(b, c));
        System.out.println("Largest: " + largest);
    }
}

// 9. Count Vowels in a String
class VowelCounter {
    public static void main(String[] args) {
        String str = "Hello World";
        int count = 0;
        for (char ch : str.toLowerCase().toCharArray()) {
            if ("aeiou".indexOf(ch) != -1) count++;
        }
        System.out.println("Vowels: " + count);
    }
}

// 10. Check Leap Year
class LeapYearCheck {
    public static void main(String[] args) {
        int year = 2024;
        boolean isLeap = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
        System.out.println("Leap year? " + isLeap);
    }
}

// 11. Reverse an Integer
class ReverseInteger {
    public static void main(String[] args) {
        int num = 12345, reversed = 0;
        while (num != 0) {
            int digit = num % 10;
            reversed = reversed * 10 + digit;
            num /= 10;
        }
        System.out.println("Reversed Integer: " + reversed);
    }
}

// 12. Sum of Digits
class SumOfDigits {
    public static void main(String[] args) {
        int num = 1234, sum = 0;
        while (num != 0) {
            sum += num % 10;
            num /= 10;
        }
        System.out.println("Sum of Digits: " + sum);
    }
}

// 13. Find GCD of Two Numbers
class GCD {
    public static void main(String[] args) {
        int a = 36, b = 60;
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        System.out.println("GCD: " + a);
    }
}

// 14. LCM of Two Numbers
class LCM {
    public static void main(String[] args) {
        int a = 12, b = 15, gcd = a, temp = b;
        while (temp != 0) {
            int t = temp;
            temp = gcd % temp;
            gcd = t;
        }
        int lcm = (a * b) / gcd;
        System.out.println("LCM: " + lcm);
    }
}

// 15. Check Even or Odd
class EvenOdd {
    public static void main(String[] args) {
        int num = 10;
        System.out.println(num + " is " + (num % 2 == 0 ? "Even" : "Odd"));
    }
}

// 16. Print a Pattern
class PatternPrinter {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}

// 17. Calculate Power of a Number
class PowerCalculator {
    public static void main(String[] args) {
        int base = 2, exponent = 5;
        int result = 1;
        for (int i = 0; i < exponent; i++) {
            result *= base;
        }
        System.out.println("Power: " + result);
    }
}

// 18. Find ASCII Value
class ASCIIValue {
    public static void main(String[] args) {
        char ch = 'A';
        int ascii = (int) ch;
        System.out.println("ASCII of " + ch + ": " + ascii);
    }
}

// 19. Sum of Array Elements
class ArraySum {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int sum = 0;
        for (int num : arr) sum += num;
        System.out.println("Sum: " + sum);
    }
}

// 20. Find Min and Max in Array
class MinMaxArray {
    public static void main(String[] args) {
        int[] arr = {5, 1, 9, 3, 7};
        int min = arr[0], max = arr[0];
        for (int num : arr) {
            if (num < min) min = num;
            if (num > max) max = num;
        }
        System.out.println("Min: " + min + ", Max: " + max);
    }
}

// 21. Count Even and Odd Numbers in Array
class EvenOddCounter {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int even = 0, odd = 0;
        for (int num : arr) {
            if (num % 2 == 0) even++;
            else odd++;
        }
        System.out.println("Even: " + even + ", Odd: " + odd);
    }
}

// 22. Find Duplicates in Array
class FindDuplicates {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 2, 4, 1};
        java.util.Set<Integer> seen = new java.util.HashSet<>();
        java.util.Set<Integer> duplicates = new java.util.HashSet<>();
        for (int num : arr) {
            if (!seen.add(num)) duplicates.add(num);
        }
        System.out.println("Duplicates: " + duplicates);
    }
}

// 23. Binary to Decimal
class BinaryToDecimal {
    public static void main(String[] args) {
        String binary = "1010";
        int decimal = Integer.parseInt(binary, 2);
        System.out.println("Decimal: " + decimal);
    }
}

// 24. Decimal to Binary
class DecimalToBinary {
    public static void main(String[] args) {
        int decimal = 10;
        String binary = Integer.toBinaryString(decimal);
        System.out.println("Binary: " + binary);
    }
}

// 25. Count Digits in Integer
class CountDigits {
    public static void main(String[] args) {
        int num = 12345, count = 0;
        while (num != 0) {
            num /= 10;
            count++;
        }
        System.out.println("Digits: " + count);
    }
}

// 26. Print Prime Numbers in Range
class PrimeInRange {
    public static void main(String[] args) {
        for (int i = 2; i <= 50; i++) {
            boolean isPrime = true;
            for (int j = 2; j <= Math.sqrt(i); j++) {
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) System.out.print(i + " ");
        }
    }
}

// 27. Linear Search
class LinearSearch {
    public static void main(String[] args) {
        int[] arr = {5, 3, 7, 2, 8};
        int target = 7;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                System.out.println("Found at index: " + i);
                return;
            }
        }
        System.out.println("Not Found");
    }
}

// 28. Bubble Sort
class BubbleSort {
    public static void main(String[] args) {
        int[] arr = {5, 2, 9, 1, 5, 6};
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
        System.out.print("Sorted: ");
        for (int num : arr) System.out.print(num + " ");
    }
}

// 29. Palindrome Number
class PalindromeNumber {
    public static void main(String[] args) {
        int num = 121, original = num, reversed = 0;
        while (num != 0) {
            int digit = num % 10;
            reversed = reversed * 10 + digit;
            num /= 10;
        }
        System.out.println(original + " is Palindrome? " + (original == reversed));
    }
}

// 30. Sum of First N Natural Numbers
class SumNaturalNumbers {
    public static void main(String[] args) {
        int n = 10;
        int sum = n * (n + 1) / 2;
        System.out.println("Sum: " + sum);
    }
}
