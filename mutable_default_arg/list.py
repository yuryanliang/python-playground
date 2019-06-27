def append_to(element, to=[]):
    to.append(element)
    return to

my_list = append_to(12)
print(my_list)

my_other_list = append_to(42)
print(my_other_list)

event=[]
for i in range(5, 11):
    new_dict= {
        'ID': '000'+str(i),
    }
    event.append(new_dict)

print(event)