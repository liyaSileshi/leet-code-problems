l1= 'lamamba'

def find_duplicates(list_param):
    d1 = {}
    duplicates = []
    for num in list_param:
        # print(d1.keys())
        
        if num in d1:
            # print(num)
            d1[num] = False

        else:
            d1[num] = True
            # print(d1[num])
            
    for key, values in d1.items():
        if values == False: 
            duplicates.append(key)
        
    return duplicates

print(find_duplicates(l1))
