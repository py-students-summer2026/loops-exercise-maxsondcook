"""
1. Write a program that finds the prime factors of a given number using a for loop. A prime factor is a prime number that divides another number exactly without leaving a remainder, e.g. the prime factors of `12` are `2` and `3`.
2. Write a program that calculates the `n`th term of the Fibonacci sequence using a while loop.
3. Write a program that checks if a given string is an anagram using a for loop.
4. Write a program that prints the first `n` terms of the arithmetic sequence using a while loop. An arithmetic sequence is a sequence of numbers in which each term after the first is found by adding a fixed, non-zero number called the common difference to the previous term, e.g. `2, 4, 6, 8, 10, 12, 14, 16, 18, 20, ...`, where the common difference is `2`.
5. Write a program that finds the median of a given list of numbers using a for loop. The median is the middle value of a list of numbers when they are sorted in ascending order. If the list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements.
6. Write a program that checks if a given number is a perfect number using a while loop. A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself, e.g. `6` is a perfect number because `1 + 2 + 3 = 6`.
7. Write a program that prints the sum of all digits in a given number using a for loop. For example, the sum of the digits in `12345` is `1 + 2 + 3 + 4 + 5 = 15`.
8. Write a program that finds the longest word in a given sentence using a while loop.
9. Write a program that checks if a given string is a pangram using a for loop. A pangram is a sentence that contains every letter of the alphabet at least once, e.g. `The quick brown fox jumps over the lazy dog`.
10. Write a program that prints the prime numbers between 1 and 1000 using a while loop.
"""
def one(number):
    print(f"The prime factors for {number} are: ",end="")
    for i in range(2,number+1):
        while number%i==0:
            print(i, end=" ")
            number=number//i
    print()

def two(n):
    if n==0:
        result=0
    elif n==1:
        result=1
    else:
        second_to_last_number=0
        last_number=1
        count=2
        while count<=n:
            total=last_number+second_to_last_number
            second_to_last_number=last_number
            last_number=total
            count+=1
        result=total
    print(f"The {n}th Fibonacci term is {result}.")

def three():
    text1=input("Enter the first word: ").lower()
    text2=input("Enter the second word: ").lower()

    is_anagram=True
    if len(text1)!=len(text2):
        is_anagram=False
    else:
        letters2=list(text2)
        for l in text1:
            if l in letters2:
                letters2.remove(l)
            else:
                is_anagram=False
    if is_anagram and len(letters2)==0:
        print(f"{text1} and {text2} are anagrams!!!")
    else:
        print(f"{text1} and {text2} are not anagrams.")

def four():
    common_difference=2
    current_number=2
    terms=input("How many terms do you want? ")
    n=int(terms)
    sequence=[]
    term_number=0
    while term_number<n:
        sequence.append(current_number)
        current_number=current_number+common_difference
        term_number+=1
    print(f"The first {n} terms are : {sequence}")

def five():
    user_input=input("Enter a list of numbers (seperated by commas). ")
    numbers=[]
    for i in user_input.split(","):
        numbers.append(int(i))
    for i in range(len(numbers)):
        for j in range(0,len(numbers)-i-1):
            if numbers[j]>numbers[j+1]:
                numbers[j], numbers[j+1]=numbers[j+1],numbers[j]
    if len(numbers)%2!=0:
        median=numbers[len(numbers)//2]
    else:
        mid1=numbers[(len(numbers)//2)-1]
        mid2=numbers[(len(numbers)//2)]
        median=(mid1+mid2)/2
    print(f"The median is {median}.")

def six(number):
    total_sum=0
    divisor=1
    while divisor<number:
        if number%divisor==0:
            total_sum+=divisor
        divisor+=1
    if total_sum==number:
        print(f"{number} is a perfect number!!!")
    else:
        print(f"{number} is not perfect number.")

def seven(number):
    total_sum=0
    for digits in str(number):
        total_sum+=int(digits)
    print(f"The total sum of the digits in {number} is {total_sum}.")

def eight():
    sentence=input("Enter a sentence: ")
    words=sentence.split()
    longest_word=words[0]
    i=0
    while i<len(words):
        if len(words[i])>len(longest_word):
            longest_word=words[i]
        i+=1
    print(f"The longest word in the sentence is {longest_word}.")

def nine():
    sentence=input("Enter a sentence. ")
    alphabet="abcdefghijklmnopqrstuvwxyz"
    is_pangram=True
    for i in alphabet:
        if i not in sentence:
            is_pangram=False
            break
    if is_pangram:
        print(f"{sentence} is a pangram!!!")
    else:
        print(f"{sentence} is not a pangram.")


def ten():
    number=2
    while number<=1000:
        is_prime=True
        divisor=number-1
        while divisor>1:
            if number%divisor==0:
                is_prime=False
                break
            divisor-=1
        if is_prime:
            print(number, end=" ")
        number+=1
    print()