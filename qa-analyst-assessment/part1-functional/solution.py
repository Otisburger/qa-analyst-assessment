def remove_duplicates(lst):
    # creates a python set
    seen = set()
    newLst = []
    # loops through the list
    for i in range(len(lst)):
        # adds list element to a new list and the python set if it isn't already in the set
        if(lst[i] not in seen):
            newLst.append(lst[i])
            seen.add(lst[i])
    return newLst

def main():
    print(remove_duplicates([1, 2, 3, 2, 4, 1, 5]))
    print(remove_duplicates([1, 1, 1]))
    print(remove_duplicates([]))

main()