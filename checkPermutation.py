#Given two strings, write a method to decide
#if one is a permutation of the other

#ask if comparision is case sensetive and whitespace is significant
#using hashtables......
def check(str1, str2):
    flag = True
    str1_index = 0
    str1 = str1.lower() #case insensetive
    str2 = str2.lower() #case insensetive
    if len(str1) == len(str2): #check if the two strings have similar length
        while str1_index < len(str1): #to not be index out of range
            for char2 in str2:
                if str1[str1_index] == char2:
                    flag = True 
                    break
                else: 
                    flag = False
            if flag == True: #first index string matches second string index
                str1_index += 1 #increment to check the next index for the loop
            else: #if flag was false at this point, the string index didn't found a match
                return False
    else:
        return False
    return flag
if __name__ == "__main__":
    print(check('God','dog'))