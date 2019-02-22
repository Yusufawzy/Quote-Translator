import requests
import json
import sys
def saveToDropbox():
    print()

def searchQuotes():
    print("Enter a number: 1-Search by Author   2-Search by keyword")
    n = int(input())
    if (n==1):
        print("Author: ", end="")
        a= input()
    elif (n==2):
        print("Keyword: " ,end="")
        a=input()
def translate (a):
    print("Enter the language code you want to translate to, Found  list of them here:")
    print("https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/#api-overview__languages")
    code = input()
    # The use of GET request
    translated = requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate?"
                              "key=trnsl.1.1.20190222T090754Z.b24e780584a1bd6f.65e695d293fdf3784143b923f6a3378e6d433a19&text="+a+"&lang="+code)
    data = json.loads(translated.text)
    print("Result is "+data['text'][0])

def detect(a):
    #The use of POST request
    detected = requests.post("https://translate.yandex.net/api/v1.5/tr.json/detect?"
                              "key=trnsl.1.1.20190222T090754Z.b24e780584a1bd6f.65e695d293fdf3784143b923f6a3378e6d433a19&text=" + a)
    data = json.loads(detected.text)
    print("The language code of the text is "+data['lang'])

def main():
    try:
        print("="*100 + "\n"+"Enter the number of the fuction you want to perform ")
        print("1- Search Quotes")
        print("2- Detect the language of the text")
        print("3- Translate your own text")
        print("4- Save your text to DropBox")
        print("5- Exit")

        n = int(input())
        if (n==2):
            print("Enter the text you want to Detect its language")
            a = input()
            detect(a)
        elif (n==3):
            print("Enter the text you want to Translate")
            a = input()
            translate(a)
        elif(n==1):
            searchQuotes()
        elif(n==4):
            saveToDropbox()
        elif (n==5):
            sys.exit()
    except:
        print("BAD CONNECTION.")
while(True):
    main()
