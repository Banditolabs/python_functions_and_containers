# EX 1
def sum_to(n):
    sum = 0
    #start at 0, travel n+1, step 1 index at a time.
    for num in range(0, n+1, 1): 
        sum = sum + num
    return sum

print(sum_to(10))

# EX 2
def largest(list):
    return max(list)

print(largest([1,6,4,3,7,9]))

# EX 3
starter = input("Enter a sentance you want to search into. ").lower()
term = input("Enter a letter or phrase to look for. ").lower()
def occurances(string, standard):
    count = 0
    for i in string:
        if (i == standard):
            count = count +1
    return count

print(occurances(starter, term))

#EX 4
lst = []
text = int(input("Enter how many numbers the list should contain: "))
for i in range (0,text):
    ele = int(input())
    lst.append(ele)
print(f"This is {lst}")

def product(lst):
    sum = 1
    for num in lst:
        sum = sum * num
    print(sum)
product(lst)


