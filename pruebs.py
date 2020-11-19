'''def append_sum(lst):
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    return lst

print(append_sum([1, 1, 2]))'''

def larger_list(lst1, lst2):
    if len(lst1) < len(lst2):
        return lst2

