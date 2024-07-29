# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

def verbing(s):
    if len(s)<3:
        return s 
    elif s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'

# first line defines verbing with one parameter (s). This parameter is a placeholder that I will pass into the function when I call it.
# the if statement says that if the word is less than 3 letters, then we will just return the word with no changes.
# elif or else if statement uses the .endswith function to say that if the word already ends with ing than we will end ly to the end. 
# else statement just states that ing will be added to it. 


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

def not_bad(s):
    
    not_word = s.find('not')
    bad_word = s.find('bad')

    if not_word != -1 and bad_word != -1 and bad_word > not_word:
        return s[:not_word] + 'good' + s[bad_word + len('bad'):]
    
    return s

# first line defines the not_bad function with s as the parameter that I will pass through it.
# I created the not_word variable and use the .find function to look for 'not' in the string.
# I created the bad_word variable and use the .find function to look for 'bad' in the string.
# in the if statement 'not_word != -1 and bad_word != -1' checks to see if 'not' and 'bad' are present in the string. And 'bad_word > not_word' makes sure that 'bad' comes after 'not' in the string. 
# if the if statement is true the 'return s[:not_word] + 'good' + s[bad_word + len('bad'):]' is passed through. 's[:not_word] gives the part of the string before 'not'. 'Good' is the replacement word. s[bad_word + len('bad'):] gives the part of the string before 'bad'.
# return s will return the original string if the conditions in the if statement are not met. 


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

def front_back(a, b):
    def halves(s):
        word_length = len(s)
        middle = (word_length + 1) // 2
        return s[:middle], s[middle:]
    
    a_front, a_back = halves(a)
    b_front, b_back = halves(b)

    return a_front + b_front + a_back + b_back

# first line defines the front_back function with two parameters (a,b)
# second line nests another defined function called 'halves' with one parameter (s)
# 'word_length' variable is used to determine the length of the s string. 
# 'middle' variable is used to find the middle of the string. '(word_length + 1) // 2' ensures that if the string length is odd, then the middle letter will go with the front half of the string. 
# s[:middle] will slice the string from the beginning of the word to the predetermined 'middle' letter/character. s[middle:] slices the string from the middle character to the end of the string. 
# a_front, a_back = halves(a) gets the front and back halves of string a.
# b_front, b_back = halves(b) gets the front and back halves of string b.
# 'return a_front + b_front + a_back + b_back' combines the strings a and b.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    main()
