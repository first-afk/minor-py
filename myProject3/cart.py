list_of_items = {'toothbrush':2000, 'indomie': 200, 'spaghetti': 500, 'tomato': 1000}
preview = []

a = list_of_items.keys()
for i in a:
    key = i.split(',')
    preview.append(key[0])
# print(preview)
def cart():
    bag = []    
    while True:
        print('what would you like to add to cart?')
        print('1. toothbrush')
        print('2. indomie')
        print('3. spaghetti')
        print('4. tomato')
        choice = input('__ ')
        print(choice)

        if choice == '1':
            bag.append(preview[0])
            # print(preview[0])
        elif choice == '2':
            bag.append(preview[1])
            # print(preview[1])
        elif choice == '3':
            bag.append(preview[2])
            # print(preview[2])
        else:
            bag.append(preview[3])
            # print(preview[3])     
        break     
    print(bag)
cart()