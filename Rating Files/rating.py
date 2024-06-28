from ratingfuncs import get_rating, add_rating, new_rating
import pathlib
import os
class rating:
    path = pathlib.Path(__file__).parent / 'ratings.txt'
    while True:
        os.system('cls')
        with open(path,"r") as f:
            text = f.readlines()
        ans = str(input("Do you want to see the ratings(1) or rate someone(2)?\n"))
        if(ans == "1"):
            if input("would you like to see who has ratings?(y/n)\n") == 'y':
                for i in range(0,len(text),2):
                    print(text[i][:-1])
            ans = input("Whose rating would you like to see?\n")
            if ans.lower() in str(text).lower():
                print(ans + "'s rating is " + str(get_rating(ans,text)))
            else:
                if input("thats not a person, would you like to add them and give them a rating?(y/n)\n") == "y":
                    with open(path,"w") as f:
                        f.writelines(new_rating(ans,text))
        elif(ans == "2"):
            if input("would you like to see who has ratings?(y/n)\n") == 'y':
                for i in range(0,len(text),2):
                    print(text[i][:-1])
            ans = input("Who would you like to rate?\n")
            if ans.lower() in str(text).lower():
                with open(path,"w") as f:
                    f.writelines(add_rating(ans,text))
            else:
                if input("thats not a person, would you like to add them and give them a rating?(y/n)\n") == "y":
                    with open(path,"w") as f:
                        f.writelines(new_rating(ans,text))
        else:
            print("sorry thats not an answer\n")
        if input("want to restart?(y/n)\n") != "y":
            break