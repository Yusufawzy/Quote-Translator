import requests, json as j, sys
def saveToDropbox(arr):
    if (len(arr)==0):
        print("enter your text: ")
        a = input(); arr.append(a)
    print("Enter File Name to be saved in dropbox: ",end="")
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

def GetFiles():
    url = "https://api.dropboxapi.com/2/files/list_folder"
    payload = "{\r\n    \"path\": \"\",\r\n    \"recursive\": false,\r\n    \"include_media_info\": false,\r\n    \"include_deleted\": false,\r\n    \"include_has_explicit_shared_members\": false,\r\n    \"include_mounted_folders\": true\r\n}"
    headers = {
        'Authorization': "Bearer Uc19JCmDglgAAAAAAAAAFrynPR0FtfXSzG3MYmbYXxgC_ZN4IITJ7gIyTMCEX0s-",
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "0824220f-9c82-4233-8d8f-777b19cde82c"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    data = j.loads(response.text)
    print("List of your root files:")
    for e in data["entries"]:
        if e['.tag'] == "file":
            print("{}  {}".format(e['name'], e['id']))

def deleteFile():
    GetFiles()
    url = "https://api.dropboxapi.com/2/files/delete_v2"
    print("Enter file name you want to delete followed by '.txt'")
    a=input()
    payload = "{ \"path\" : \"/"+a+"\"}"
    headers = {
        'Authorization': "Bearer Uc19JCmDglgAAAAAAAAAFrynPR0FtfXSzG3MYmbYXxgC_ZN4IITJ7gIyTMCEX0s-",
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "40e0be50-79e8-4869-b1e5-032f8239d62f"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    if response.ok :
        print("Successfuly Deleted")
    else :
        print("There was a problem")
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
    print("Result is \"{}\"".format(data['text'][0]))

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


def main():

        print("="*100 + "\n"+"Enter the number of the fuction you want to perform ")
        print("1- Search Quotes,Translate Them,Save to Dropbox")
        print("2- Detect the language of text")
        print("3- Translate your text")
        print("4- Save text to DropBox")
        print("5- Get Quote of the day")
        print("6- Get List of your Files in dropbox")
        print("7- Delete file from dropbox ")
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
        elif (n==7):
            deleteFile()

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
