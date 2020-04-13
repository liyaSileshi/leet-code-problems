
def twelvedays():
    days = ['first', 'second', 'third']
    pointer = 0
    gifts = ["a Partridge in a Pear Tree","two Turtle Doves","three French Hens"]
    gift = ''

    while pointer < len(gifts):
        for i in days:
            gift += gifts[pointer]
            print(f'on the {i} day of Christmas my true love gave to me: {gift}')
            pointer += 1
            print(pointer)


twelvedays()
