import requests
import json

def saveToDropbox():
    print()

def searchTwitter(a):
    print()


def translate (a):
    print("Enter the language code you want to translate to, Found  list of them here:")
    print("https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/#api-overview__languages")
    code = input()
    translated = requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate?"
                              "key=trnsl.1.1.20190222T090754Z.b24e780584a1bd6f.65e695d293fdf3784143b923f6a3378e6d433a19&text="+a+"&lang="+code)
    data = json.loads(translated.text)
    print("Result is "+data['text'][0])

def detect(a):
    detected = requests.post("https://translate.yandex.net/api/v1.5/tr.json/detect?"
                              "key=trnsl.1.1.20190222T090754Z.b24e780584a1bd6f.65e695d293fdf3784143b923f6a3378e6d433a19&text=" + a)
    data = json.loads(detected.text)
    print("The language code of the text is "+data['lang'])

def main():
    print()
    print("Enter the number of the fuction you want to perform ")
    print("1- Detect the language of the text")
    print("2- Translate your own text")
    print("3- Search Tweets by Hashtags")
    print("4- Save your text to DropBox")

    n = int(input())
    if (n==1):
        print("Enter the text you want to Detect its language")
        a = input()
        detect(a)
    elif (n==2):
        print("Enter the text you want to Translate")
        a = input()
        translate(a)
    elif(n==3):
        print("Enter the keyword to search for")
        a = input()
        searchTwitter(a)
    elif(n==4):
        saveToDropbox()

while (True):
    main()
