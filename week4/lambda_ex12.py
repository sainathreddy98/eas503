# lambda_ex12.py
# sort list by value

my_list = [{'value': '34.4'}, {'value': '45.3'}, {'value': '73.4'}]


sort_func = lambda blah: blah['value']

print(sorted(my_list, key=sort_func))