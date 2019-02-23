import requests, json as j, sys
def saveToDropbox(arr):
    if (len(arr)==0):
        print("joe")
    print("Enter File Name: ",end="")
    name = input()
    with open(name+".txt", "w") as text_file:
        text_file.write('\n'.join(arr))
    url = "https://content.dropboxapi.com/2/files/upload"
    data = open('./'+name+'.txt', 'rb').read()
    headers = {
        'Authorization': "Bearer Uc19JCmDglgAAAAAAAAAFrynPR0FtfXSzG3MYmbYXxgC_ZN4IITJ7gIyTMCEX0s-",
        'Dropbox-API-Arg': "{\"path\": \"/"+name+".txt\"}",
        'Content-Type': "application/octet-stream",
        'cache-control': "no-cache",
        'Postman-Token': "b58707c7-dee7-4545-ac83-a8644ae88069"
    }

    response = requests.request("POST", url, data=data, headers=headers)

    print(response.text)


def translateCode (a,code):
    translated = requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate?"
                              "key=trnsl.1.1.20190222T090754Z.b24e780584a1bd6f.65e695d293fdf3784143b923f6a3378e6d433a19&text="+a+"&lang="+code)
    data = j.loads(translated.text)
    print(data['text'][0])

def translate (a):
    print("Enter the language code you want to translate to, Found  list of them here:")
    print("https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/#api-overview__languages")
    code = input()
    # The use of GET request
    translated = requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate?"
                              "key=trnsl.1.1.20190222T090754Z.b24e780584a1bd6f.65e695d293fdf3784143b923f6a3378e6d433a19&text="+a+"&lang="+code)
    data = j.loads(translated.text)
    print("Result is "+data['text'][0])

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
    print("Enter a number: 1- Search by Author   2- Search by keyword")
    n = int(input())
    if (n==1):#for example "Mark Twain"
        print("Author: ", end="")
        a= input()
        r = requests.get(
            'https://favqs.com/api/quotes/?filter=' + a + '&type=author&auth_token=238a98be00ce8dd27256e7142658822e',
            headers={'Authorization': 'Bearer 238a98be00ce8dd27256e7142658822e'})
    elif (n==2):#for example "funny"
        print("Keyword: " ,end="")
        a=input()
        r = requests.get('https://favqs.com/api/quotes/?filter='+a+'&type=tag&auth_token=238a98be00ce8dd27256e7142658822e', headers={'Authorization': 'Bearer 238a98be00ce8dd27256e7142658822e'})

    orig,translated = [],[]
    data = j.loads(r.text)['quotes']
    for  i in range(len(data)):
        try:
            print("* "+data[i]['body'] + " Author is: "+ data[i]['author'] )
            orig.append("* "+data[i]['body'])
        except:
            continue

    print("Do you want to translate? Y/N")
    a = input()
    if (a == "Y" or a == "y"):
        print("Enter the language code you want to translate to, Found  list of them here:")
        print("https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/#api-overview__languages")
        code = input()
        for e in orig:
            t = translateCode(e,code)
            translated.append(t)
        print("Do you want to save to Dropbox? Y/N")
        a = input()
        if (a == "Y" or a == "y"):
            saveToDropbox(translated)

def addQuote():
    print()
def deleteUserActivity():
    print("Enter your user name")
    a = input()
    url = "https://favqs.com/api/activities/"
    querystring = {"type": "user", "filter": a, "auth_token": "238a98be00ce8dd27256e7142658822e"}
    payload = ""
    headers = {
        'Authorization': "Bearer 238a98be00ce8dd27256e7142658822e",
        'cache-control': "no-cache",
        'Postman-Token': "10b85633-46dc-4bc8-b74c-8f4901ad0062"
    }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data = j.loads(response.text)
    for e in data['activities']:
        print("activity_id is {} , message is {} ".format(e['activity_id'],e['message']))
    print("Enter the activity_id you want to delete: ",end="")
def main():

        print("="*100 + "\n"+"Enter the number of the fuction you want to perform ")
        print("1- Search Quotes,Translate Them,Save to Dropbox")
        print("2- Detect the language of text")
        print("3- Translate your text")
        print("4- Save text to DropBox")
        print("5- Get the quote of the day")
        print("6- Get List of your Files in dropbox")
        print("7- Add your own Quote")
        print("8- Delete your activity of adding quotes ")
        print("10- Exit")

        n = int(input())
        if (n == 1):
            searchQuotes()
        if (n==2):
            print("Enter the text you want to Detect its language")
            a = input()
            detect(a)
        elif (n==3):
            print("Enter the text you want to Translate")
            a = input()
            translate(a)

        elif(n==4):
            saveToDropbox([])
        elif(n==5):
            quoteOfTheDay()
        elif (n==6):
            GetFiles()
        elif (n==6):
            addQuote()
        elif(n==9):
            deleteUserActivity()
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
te - Telug
"""
