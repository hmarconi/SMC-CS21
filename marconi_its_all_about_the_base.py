# Haley Marconi
# CS 21 Fall 2018
# It's All About The Base

# This file contains three functions; prepare_words(in_string),
# word_to_base4(new_string), and base10_to_words(num). First, it takes an
# input of in_string, which is a string,  and runs it through
# prepare_words(in_string) and word_to_base4(new_string) in that order
# to convert the string into a base 4 number using the given code words. It
# then prints the equivalent base 4 number into the string. Secondly, it takes
# an input of num, which is a non negative integer, and runs it through
# base10_to_words(num) to convert it from base 10 notation into its
# corresponding code words and prints them.

def main():
    
    # Here in_string is assigned as an input from the user, which is assumed
    # to be a string. It is then run through prepare_words and words_to_base4
    # and the output given to the user is the result of in_string in words_
    # to_base4.
    
    in_string = input("Please enter a string to convert to base 4: ")
    in_string = prepare_words(in_string)
    base4_str = words_to_base4(in_string)
    print(base4_str)
    
    # Here, exception handling takes care of all requirements needed for the
    # user input of num. It is asserted that the user's input will be an
    # integer and then the exception handling takes care of anything from
    # the user that is not a postive integer and will continue asking the
    # user for a non-negative integer until the user's input meets those
    # requirements.
    
    try:
        num = int(input("Please enter a number: "))
    except ValueError:
        num = int(input("Please enter a non-negative integer: "))
    value = False
    while value == False:
        if type(num) != int:
            value = False
            try:
                num = int(input("Please enter a non-negative integer: "))
            except ValueError:
                num = int(input("Please enter a non-negative integer: "))
        elif num < 0:
            value = False
            try:
                num = int(input("Please enter a non-negative integer: "))
            except ValueError:
                num = int(input("Please enter a non-negative integer: "))
                
        # Here the value is made "True" if it meets all of the requirements
        # and then the output that is returned to the user is equal to the value
        # of "num" as it is run through the recursive function base10_to_words.
        
        else:
            value = True
    base10_str = base10_to_words(num)
    print(base10_str)
    
# This function will take the parameter called "in_string" and remove any
# non-alphanumeric characters from words and presenting them in a list.
# This list will then be compared to our given code words, and the words
# within the list match with code words will be made into a string for use
# in words_to_base4.

def prepare_words(in_string):
    
    # Here the four code words are presented as a list and the given in_string
    # is converted into a list by splitting it. Two lists called newlist and
    # outlist are also given to be used later within the function.
    
    code_words = ["the","quick","fox","dog"]
    mylist = in_string.split()
    newlist = " "
    outlist = []
    
    # The following for loop will only keep alpha-numeric characters,
    # removing anything that does not meet those requirements. It
    # will then add those words to newlist.
    
    for word in mylist:
        newlist += " "
        for character in word:
            if "a" <= character <= "z":
                newlist += character
            if "A" <= character <= "Z":
               newlist += character
            if "0" <= character <= "9":
                newlist += character
                
    # A new list is created, called goodlist, which is made by splitting
    # the words given from newlist.
    
    goodlist = newlist.split()
    # The following for loop will add the words from goodlist that are
    # also present in code_words and add them to the empty list "outlist."
    
    for goodword in goodlist:
        if goodword in code_words:
            outlist.append(goodword)
            
    # Newstring is created by joining the list of words and also separating
    # them by spaces. This value is then stored within the function but not
    # presented to the user.
    
    newstring = ' '.join(outlist)
    return newstring

# This function will also take the parameter called "in_string" that has been
# prepared by the previous function. It will find the base 4 number equivalent
# of each word and present those words in one list to the user.The function is
# implemented as a recursive function.

def words_to_base4(in_string):
    
    # Here, the string is made into a list by splitting the string.
    
    newlist = in_string.split()
    
    # The function's restriction for the recursive step will be that
    # if/when the length of the list is equal to zero, nothing will be
    # returned and the function will stop running.
    
    if len(newlist) == 0:
        return ""

    # Otherwise, the function will go through "in_string" which will be made
    # equal to the list in reverse order. As it evaluates each word, the
    # function will run through if-statements that tell the function what
    # each word's assigned base 4 value is. When returned, it will call the
    # function again, creating recursion, while also adding the previously
    # found base 4 values. A string of these values will then be presented
    # to the user.
    
    else:
        in_string = " ".join(newlist[:-1])
        if newlist[-1] == "the":
            return words_to_base4(in_string) + "0"
        elif newlist[-1] == "quick":
            return words_to_base4(in_string) + "1"
        elif newlist[-1] == "fox":
            return words_to_base4(in_string) + "2"
        elif newlist[-1] == "dog":
            return words_to_base4(in_string) + "3"

# This function will take a parameter called “num” from the user, which
# will be a non-negative base-10 integer. The function will run through the
# integer and return its base-4 code word equivalent as a string. The
# function is implemented as a recursive function.

def base10_to_words(num):
    code_words = ["the", "quick", "fox", "dog"]
    
    # The function's restriction for the recursive step will be that
    # if/when the num is less than four, it will return the base 4 equivalent
    # of the word plus a space, so that the words are separated. Num%4 will
    # represent the place of the code word within code_words.
    
    if num < 4:
        return str(code_words[num%4]) + " "
    
    # Otherwise, num will be "integer divided" by 4, meaning the exact number
    # of times it is divisible by 4 with no remainder. This number will be less
    # than four and represents the base 4 equivalent. The corresponding code
    # word will be added to the list. Until num is less than 4, the function
    # will be recalled, creating recursion. Once the restriction is met, the
    # final string of words will presented to the user.
    
    else:
        return base10_to_words(num//4) + str(code_words[num%4]) + " "

main()
 
    

