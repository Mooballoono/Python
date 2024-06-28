def get_rating(name,text):
    for i in text:
        if name.lower() in i.lower(): index = text.index(i)
    nums = text[index+1].split(",")
    del nums[-1:]
    for i,l in enumerate(nums): nums[i] = int(l)
    return(round(sum(nums)/text[index+1].count(","),1))

def add_rating(name,text):
    ans = "0"
    for i in text:
        if name.lower() in i.lower(): index = text.index(i)
    while ans == "0":
        ans = input("Enter your rating of " + ans + " from 1 to 10\n")
        if ans in ['1','2','3','4','5','6','7','8','9','10']:
            text[index+1] = text[index+1].replace("\n","") + ans + ",\n"
        else:
            print(ans + " is not a number from 1 to 10")
            ans = "0"
    return text

def new_rating(name,text):
    text.append(name + "\n")
    ans = "0"
    while ans == "0":
        ans = input("Enter your rating of " + name + " from 1 to 10\n")
        if ans in ['1','2','3','4','5','6','7','8','9','10']:
            text.append(ans + ",\n")
        else:
            print(ans + " is not a number from 1 to 10\n")
            ans = "0"
    return text
    