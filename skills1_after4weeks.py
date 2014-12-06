# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):

    odd_nums = []

    for i in number_list:
        if i % 2 != 0:
            odd_nums.append(i)

    return odd_nums

print "all_odd", all_odd(number_list)

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):

    even_nums = []

    for i in number_list:
        if i%2==0:
            even_nums.append(i)
    return even_nums

print "even nums: ", all_even(number_list)

# Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.
def long_words(word_list):

    four_or_more = []

    for word in word_list:
        if len(word) >= 4:
            four_or_more.append(word)

    return four_or_more

print "long words", long_words(word_list)

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):

    number_list.sort()
    return number_list[0]

#with a loop

    # min_num = number_list[0]

    # for num in number_list:
    #     if num < min_num:
    #         min_num = num

    # return min_num

print "smallest number", smallest(number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):

    number_list.sort()
    return number_list[-1]

#with loop

    # biggest_num = number_list[-1]

    # for num in number_list:
    #     if num > biggest_num:
    #         biggest_num = num

    # return biggest_num

print "biggest number", largest(number_list)


# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):

    halved = []

    for num in number_list:
        halved.append(num/2.0)

    return halved

print "halved", halvesies(number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):

    word_lengths = []

    for word in word_list:
        word_lengths.append(len(word))

    return word_lengths

print "word lengths", word_lengths(word_list) 

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):

    sums = 0
    for num in number_list:
        sums += num 

    return sums

print "sum numbers", sum_numbers(number_list) 

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):

    mult_total = 1

    for num in number_list:
        mult_total = mult_total * num
    
    return mult_total

print "mult numbers", mult_numbers(number_list) 

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):

    single_str = ''
    for word in word_list:
        single_str = single_str + word

    return single_str

print "join strings", join_strings(word_list) 

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):

    total = 0

    for num in number_list:
        total += num 

    average = float(total)/len(number_list)

    return average

print "average", average(number_list) 
