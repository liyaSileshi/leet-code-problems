def two_fer(name=None):
    if name == None:
        return f'One for you, one for me'
    else:
        return f'one for {name}, one for me'

if __name__ == '__main__':
    print(two_fer())
    print(two_fer('liya'))