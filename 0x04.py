def flatten(li):
    if not isinstance(li,list):
        return "[!]Please enter list as an arguement."

    for items in li:
        if isinstance(items,list):
            count = li.index(items)
            print(count)
            for item in items:

                item = ",".join(item)

    return li

(flatten([1,2,[3,4,[5,[6],7]]]))
