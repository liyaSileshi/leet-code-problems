#Implement an algorithm to determine if a string has all unique
#characters. What if you cannot use additional data structures?
def unique(word):
    new_str = ''
    for i in word:
        if i in new_str:
            return False
        else:
            new_str += i
    return True

if __name__ == "__main__":
    print(unique('aple'))