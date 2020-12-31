import json 
from difflib import get_close_matches
data=json.load(open("dictionary.json"))
print()
print("Know it All - Smarty Pants :")
print()
respos=["yes","y","yeah","yea","yup","yep"]
resneg=["never","no","n","nope"]
while True:
    print()
    word=input("Enter the word you like to search for : ")
    print()
    word=word.lower()
    if word in data:
        print()
        print(word.capitalize()," :")
        listToStr = ' '.join([str(elem) for elem in data[word]]) 
        print(listToStr) 
    elif(len(get_close_matches(word,data.keys()))>0):
        print("Did you mean {} instead ? Y/N".format(get_close_matches(word,data.keys())[0]))
        d=input()
        if d in respos:
            word=get_close_matches(word,data.keys())[0]
            print()
            print(word.capitalize()," :")
            listToStr = ' '.join([str(elem) for elem in data[word]]) 
            print(listToStr) 
            print()
        elif d in resneg:
            print()
            print("You have given a word that doesn't list in our Dictionary, or you may have inputted Wrong.")
            continue
        else:
            while d not in respos or resneg:
                print()
                print("Sorry I didn't get that !")
                print("Please input again ,")
                print("Did you mean {} instead ? Y/N".format(get_close_matches(word,data.keys())[0]))
                d=input()
                d=d.lower()
                if d in respos:
                    word=get_close_matches(word,data.keys())[0]
                    print()
                    print(word.capitalize()," :")
                    listToStr = ' '.join([str(elem) for elem in data[word]]) 
                    print(listToStr) 
                    break
                elif d in resneg:
                    print("Sorry , You have given a word that doesn't list in our Dictionary, or you may have inputted Wrong.")
                    break
    else:
        print("Sorry , You have given a word that doesn't list in our Dictionary, or you may have inputted Wrong.")
    print()
    print("Do you want to Search again ? Y/N")
    r=input()
    r=r.lower()
    if r in respos:
        continue
    elif r in resneg:
        exit(0)
    else:
        while r not in respos or resneg:
            print()
            print("Sorry I didn't get that !")
            print("Please input again ,")
            print("Do you want to continue ? Y/N")
            r=input()
            r=r.lower()
            if r in respos:
                break
            elif r in resneg:
                exit(0)
    print()



