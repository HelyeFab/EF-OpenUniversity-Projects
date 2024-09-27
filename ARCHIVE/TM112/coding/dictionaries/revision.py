a_list=[2,5,1]

print(a_list[0])    #first element
print(a_list[1:3])  #second to third element
print(a_list[:])    #all elements
print(a_list[-1])   #last element
print(a_list[-2])   #second to last element
print(len(a_list))   #number of elements
print(a_list.__contains__(5))

a_list.append(0)
print(a_list)