# # Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    number_list.sort()
    odd_nums = []
    for eachchar in number_list:
        if eachchar % 2 != 0:
            odd_nums.append(eachchar)
    return odd_nums

print "Odd numbers: ", all_odd(number_list)

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    number_list.sort()
    even_nums = []

    for eachchar in number_list:
        if eachchar % 2 == 0:
            even_nums.append(eachchar)

    return even_nums

print "Even numbers: ", all_even(number_list)

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    #sort words in place by ord value
    word_list.sort()
    #convert list to string separated by space
    join = " ".join(word_list)
    #set variable to new list of lower case elements then convert string to new list
    lower_list = join.lower().split(" ")

    #if eachchar is greaterthanorequalto 4, set value to eachchar
    length4ormore = []
    for eachchar in lower_list:
        if len(eachchar) >= 4:
            length4ormore.append(eachchar)

    count = 0
    if lower_list[i]         

    return length4ormore

    #multiple occurances of "spam"
    #write a loop that checks for multiple occurences of an item, then makes a placeholder for that item. 
    #or use the method 'count' to see if there are multiple occurences of an item


print "Strings length 4 and greater: ", long_words(word_list)


# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    number_list.sort()
    return number_list[0]

    # number_list.sort()
    # smallest_num = 0

    # for i in range(len(number_list)-1):
    #     if number_list[i] < smallest_num:
    #         smallest_num = number_list[i]
            
    # return smallest_num

print "The smallest number: ", smallest(number_list)


# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    number_list.sort()
    return number_list[-1]

print "The largest number: ", largest(number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):

    halved = []
    for eachdig in number_list:
        halved.append(eachdig/ 2.0)
    return halved

print "Halves: ", halvesies(number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):

    lengths = []
    for eachchar in word_list:
        lengths.append(len(eachchar))
    return lengths

print "Word lengths: ", word_lengths(word_list)

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    sum = 0
    for i in range(len(number_list)):
        sum = sum + number_list[i]
    return sum

print "Sum of numbers: ", sum_numbers(number_list)


# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):

    multiplied = 1
    for i in range(len(number_list)):
        multiplied = multiplied * number_list[i]
    return multiplied

print "Multiplied numbers: ", mult_numbers(number_list)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    word_list.reverse()
    popped = ""

    for i in range(len(word_list)):
        popped += word_list.pop()

    return popped

print "Strings joined without spaces: ", join_strings(word_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    sum = 0
    for i in range(len(number_list)):
        sum = sum + number_list[i]
    avg = sum/len(number_list)

    return avg

print "The average of the numbers is: ", average(number_list)



