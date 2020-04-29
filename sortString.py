# Given a string s. You should re-order the string using the following algorithm:
# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.

def sortString(string):
    #change it to a list
    string = list(string)
    sorted_list = []
    mini = '~'
    last_append = min(string)
    # while string is not None:
    while mini > last_append:
        mini = min(string)
        sorted_list.append(mini)
        min_index = string.index(min(string))
        #delete once appended
        last_append = string.pop(min_index)
        #reassign min to new min
        mini = min(string)
    print(sorted_list)

sortString('baba')
