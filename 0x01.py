def special_zip(li1,li2):
    try :
        li1 = list(li1)
        li2 = list(li2)
    except:
        return "Please enter list as arguements: "

    if not len(li1)== len(li2):
        return "Both the lists must be of the same length. "

    return [(li1[i],li2[i]) for i in range(len(li1))]


print(special_zip([1,2,3],['x','y','z']))