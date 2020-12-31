import json #Importing the json libraryy
from difflib import get_close_matches #Importing the function from the library for the closest word search
data=json.load(open("dictionary.json")) #Converting the json file into a dictionary(Python jargon)
print()
print("Know it All - Smarty Pants :")
print()
respos=["yes","y","yeah","yea","yup","yep"] #Creating a list for Positive responses
resneg=["never","no","n","nope"] #Creating a list for Negative responses
while True:
    print()
    word=input("Enter the word you like to search for : ") #Input the word to search for
    print()
    word=word.lower() #Converting the word to Lower case to simplify the searching in the json file
    if word in data: #Checking if the word searched exists in the Dictionary
        print()
        print(word.capitalize()," :") #Formatting the word to display by making first letter as Upper case
        listToStr = ' '.join([str(elem) for elem in data[word]]) #To remove '' from list
        print(listToStr) 
    elif(len(get_close_matches(word,data.keys()))>0): #If searched word was not found in the Dictionary
                                                      #Checking if there exists atleast one closely related word
        print("Did you mean {} instead ? Y/N".format(get_close_matches(word,data.keys())[0])) #Asking if the first closely related word is the word if meant
        d=input() #Input yes or no
        if d in respos: #Checking if response is in Positive Responses
            word=get_close_matches(word,data.keys())[0] #Finding the first closely related word
            print()
            print(word.capitalize()," :")
            listToStr = ' '.join([str(elem) for elem in data[word]]) 
            print(listToStr) 
            print()
        elif d in resneg: #Checking if response is in Negative Responses
            print()
            print("You have given a word that doesn't list in our Dictionary, or you may have inputted Wrong.")
            continue
        else:
            while d not in respos or resneg: #Looping if the user entered something else other than yes or no 
                                             #or something not in either Positive responses ot Negative responses
                print()
                print("Sorry I didn't get that !")
                print("Please input again ,")
                print("Did you mean {} instead ? Y/N".format(get_close_matches(word,data.keys())[0]))
                d=input() #Input yes or no
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
    r=input() #Input yes or no
    r=r.lower()
    if r in respos:
        continue
    elif r in resneg:
        exit(0)
    else:
        while r not in respos or resneg: #Looping if the user entered something else other than yes or no 
                                         #or something not in either Positive responses ot Negative responses
            print()
            print()
            print("Sorry I didn't get that !")
            print("Please input again ,")
            print("Do you want to continue ? Y/N")
            r=input() #Input yes or no
            r=r.lower()
            if r in respos:
                break
            elif r in resneg:
                exit(0)
    print()



