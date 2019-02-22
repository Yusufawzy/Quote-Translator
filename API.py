import requests, json as j, sys
def saveToDropbox():
    print()
def translateCode (a,code):
    translated = requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate?"
                              "key=trnsl.1.1.20190222T090754Z.b24e780584a1bd6f.65e695d293fdf3784143b923f6a3378e6d433a19&text="+a+"&lang="+code)
    data = j.loads(translated.text)
    print("Result is "+data['text'][0])

def translate (a):
    print("Enter the language code you want to translate to, Found  list of them here:")
    print("https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/#api-overview__languages")
    code = input()
    # The use of GET request
    translated = requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate?"
                              "key=trnsl.1.1.20190222T090754Z.b24e780584a1bd6f.65e695d293fdf3784143b923f6a3378e6d433a19&text="+a+"&lang="+code)
    data = j.loads(translated.text)
    print(data['text'][0])

def detect(a):
    #The use of POST request
    detected = requests.post("https://translate.yandex.net/api/v1.5/tr.json/detect?"
                              "key=trnsl.1.1.20190222T090754Z.b24e780584a1bd6f.65e695d293fdf3784143b923f6a3378e6d433a19&text=" + a)
    data = j.loads(detected.text)
    print("The language code of the given text is \""+data['lang']+"\"")

def quoteOfTheDay():
    a = requests.get('https://favqs.com/api/qotd')
    data = j.loads(a.text)
    print(data["quote"]["body"])
    print("The Author is "+data["quote"]["author"])
    print("Do you want to translate? Y/N")
    a = input()
    if (a=="Y" or a=="y"):
        translate(data["quote"]["body"])

def searchQuotes():
    print("Enter a number: 1-Search by Author   2-Search by keyword")
    n = int(input())
    if (n==1):#for example "Mark Twain"
        print("Author: ", end="")
        a= input()
        r = requests.get(
            'https://favqs.com/api/quotes/?filter=' + a + '&type=author&auth_token=238a98be00ce8dd27256e7142658822e',
            headers={'Authorization': 'Bearer 238a98be00ce8dd27256e7142658822e'})
    elif (n==2):#for example "Funny"
        print("Keyword: " ,end="")
        a=input()
        r = requests.get('https://favqs.com/api/quotes/?filter='+a+'&type=tag&auth_token=238a98be00ce8dd27256e7142658822e', headers={'Authorization': 'Bearer 238a98be00ce8dd27256e7142658822e'})

    arr=[]
    data = j.loads(r.text)['quotes']
    for  i in range(len(data)):
        try:
            print("* "+data[i]['body'])
            arr.append("* "+data[i]['body'])
        except:
            continue

    print("Do you want to translate? Y/N")
    a = input()
    if (a == "Y" or a == "y"):
        print("Enter the language code you want to translate to, Found  list of them here:")
        print("https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/#api-overview__languages")
        code = input()
        for e in arr:
            translateCode(e,code)

def main():

        print("="*100 + "\n"+"Enter the number of the fuction you want to perform ")
        print("1- Search Quotes")
        print("2- Detect the language of the text")
        print("3- Translate your own text")
        print("4- Save your text to DropBox")
        print("5- Get the quote of the day")
        print("10- Exit")

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
        elif(n==5):
            quoteOfTheDay()
        elif (n==10):
            sys.exit()

while(True):
    main()
"""
en - English ( default )
be - Bengali
fr - French
hi - Hindi
de - German
it - Italian
pl - Polish
pt - Portuguese
ru - Russian
es - Spanish
tr - Turkish
uk - Ukrainian
he - Hebrew
ar - Arabic
te - Telug"""
