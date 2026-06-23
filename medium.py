"""
1. Write a program that finds the largest element in a given list using a for loop.
2. Write a program that calculates the average of a list of numbers using a while loop. You are not allowed to use the built-in `sum()` function.
3. Write a program that checks if a given string is a palindrome using a for loop. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, e.g. `radar`, `level`, `12321`, `mom`, `noon`, `civic`, `deified`, `racecar`, `madam`, `refer`, `repaper`, `rotor`, `sagas`, `solos`, `stats`, `tenet`, `wow`, ...
4. Write a program that prints the first _n_ terms of the geometric sequence using a while loop. A geometric sequence is a sequence of numbers in which each term after the first is found by multiplying the previous term by a fixed, non-zero number called the common ratio, e.g. `2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, ...`, where the common ratio is `2`.
5. Write a program that finds the second largest element in a given list using a for loop.
6. Write a program that calculates the factorial of a given number using a while loop.
7. Write a program that checks if a given number is a perfect square using a for loop. A perfect square is a number that can be expressed as the product of two equal integers, e.g. `1`, `4`, `9`, `16`, `25`, `36`, `49`, `64`, `81`, `100`, ...
8. Write a program that prints the sum of all prime numbers between 1 and 100 using a while loop.
9. Write a program that counts the number of words in a given sentence using a for loop. Words can be separated by spaces, commas, periods, exclamation marks, question marks, etc. You may be interested in the built-in `split()` function, which splits a string into a list of words based on a delimiter. The delimiter is a space by default, but you can specify a different delimiter, e.g. `split(',')`, `split('.')`, `split('!')`, `split('?')`, etc. You can even specify multiple delimiters, e.g. `split(',.!?')`.
10. Write a program that prints the common elements between two lists using a while loop.
"""

def one():
    user_input=input("Enter a list of elements (use their atomic number).")
    elements=[]
    for i in user_input.split(","):
        elements.append(int(i))
    largest=0
    for i in elements:
        if i>largest:
            largest=i
    print(f"The largest element is {largest}")
def two():
    user_numbers=input("Enter a list of numbers to find the average: ")
    numbers=[]
    for i in user_numbers.split(","):
        numbers.append(int(i))
    total=0
    i=0
    while i<len(numbers):
        total+=numbers[i]
        i+=1
    average=total/len(numbers)
    print(f"The average of {numbers} is {average}.")

def three():
    text=input("Enter something to see if its a palindrome. ")
    reversed_text=""
    for i in range(len(text) -1, -1, -1):
        reversed_text+=text[i]
    if text==reversed_text:
        print(f"{text} is a palindrome!!!")
    else:
        print(f"{text} is not a palindrome.")

def four():
    common_ratio=2
    current_number=2
    terms=input("How many terms do you want? ")
    n=int(terms)
    sequence=[]
    term_number=0
    while term_number<n:
        sequence.append(current_number)
        current_number=current_number*common_ratio
        term_number+=1
    print(f"The first {n} terms are : ", end="")
    print(*sequence, sep= ", ")

def five():
    user_input=input("Enter a list of elements (use their atomic number).")
    elements=[]
    for i in user_input.split(","):
        elements.append(int(i))
    largest=0
    second_largest=0
    for i in elements:
        if i>largest:
            second_largest=largest
            largest=i
        elif i>second_largest and i!=largest:
            second_largest=i
    print(f"The second largest element is {second_largest}.")

def six(number):
    product=number
    i=number-1
    while i>0:
        product=product*i
        i-=1
    print(f"{number} factorial = {product}")

def seven():
    user_input=input("Enter a number to check if its a perfect square. ")
    number=int(user_input)
    is_perfect_square=False
    for i in range(1, number+1):
        if i * i==number:
            is_perfect_square=True
            break
    if is_perfect_square:
        print(f"{number} is a perfect square!!!")
    else:
        print(f"{number} is not a perfect square.")

def eight():
    total_sum=0
    number=2
    while number<=100:
        is_prime=True
        divisor=number-1
        while divisor>1:
            if number%divisor==0:
                is_prime=False
                break
            divisor-=1
        if is_prime:
            total_sum+=number
        number+=1
    print(f"The total sum of all the prime numbers between 1 and 100 is {total_sum}.")

def nine():
    sentence=input("Enter a sentence: ")
    words=sentence.split()
    count=0
    for i in words:
        count +=1
    print(f"Word count in your sentence is {count}.")

def ten():
    user_input1=input("Enter a list of elements (use their atomic number).")
    user_input2=input("Enter another list of elements (use their atomic number).")
    list1=[]
    for i in user_input1.split(","):
        list1.append(int(i))
    list2=[]
    for i in user_input2.split(","):
        list2.append(int(i))
    common=[]
    i=0
    while i<len(list1):
        if list1[i] in list2:
            common.append(list1[i])
        i+=1
    print("The common elements within the two lists are : ", end="")
    print(*common, sep= ", ")