list1 = input('Enter items separated by a comma: ')
list2 = input('Enter items separated by a comma: ')


set1 = set(list1.split(','))
set2 = set(list2.split(',') )


combined_set = set1.union(set2)

sorted_tuple = tuple((combined_set))



# for item in sorted_tuple:
print(f'dad, here is the list:')

j = 0

for i in sorted_tuple:
    print(j, i)
    j += 1



    
# for idx,item in enumerate(sorted_tuple):
    # print(idx, item)
# for item in list1:
    # print(f'{list1} \n')