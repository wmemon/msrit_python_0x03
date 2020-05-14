from collections import defaultdict


def birthday_lookup(li):
    result = {}
    if not isinstance(li, list):
        return "[!]The function takes list as the argument."

    for item in li:
        if item[1] in result.keys():
            result[item[1]].append(item[0])

        if item[1] not in result.keys():
            result[item[1]] = [item[0]]
    result = defaultdict(lambda: "No one has a birthday on this day! ", result)
    return result



res =(birthday_lookup([("Bill", "Apr 1"), ("Ron", "Jun 6"), ("Kat", "May 12"), ("Eric", "Jun 6"), ("Que", "Feb 10")]))
print(res["Apr 1"])
print(res["Jun 5"])
print(res["Jun 6"])
