import imapclient
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# to list helper function 

def toList(d):
    return str(dict(d)).split(',')

# helper function to clean up the string 

def clean(str):
        str = str.replace("b","")
        str = str.replace(")","")
        return str

# append data from web helper function 

def appendData(a,browser,ind,x):
    for index in range(1,x+1):
        for i in range(4,10):
            a[ind].append(WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"/html/body/main/div[1]/div[2]/noindex/div/div/table/tbody/tr["+ str(index)+"]/td[" + str(i)+"]"))).text)
        a.append([])
        ind+=1
   
# use IMAP to gather the metadata from emails from a set date 

def emailscrape(conn, num):
    a = [[],[]]
    j=1
    template = ['File Name', 'Subject', 'From', 'To', 'Date', 'CC','BCC']
    for i in range(0, len(num)):
        rawMessage = conn.fetch(num[i],['BODYSTRUCTURE','FLAGS'])
        rawHeader = conn.fetch(num[i], ['BODY[HEADER.FIELDS (SUBJECT FROM TO SUBJECT DATE CC BCC)]','FLAGS'])
        rawMessage = toList(rawMessage)
        fileName = ""
        for words in range(0,len(rawMessage)):
            if " (b'name'" in rawMessage[words]:
                fileName = rawMessage[words+1]
        fileName = clean(fileName)
        n = dict(rawHeader)[num[i]][b'BODY[HEADER.FIELDS (SUBJECT FROM TO SUBJECT DATE CC BCC)]']
        n = str(n).replace("b'",'').split('\\r\\n')
        for values in range(0,len(n)):
            n[values] = n[values].split(':')
        for values in range(0,len(n)):
            for indexes in n[values]:
                if 'Date' in indexes:
                    n[values][1] = ":".join(n[values][1:])
                    n[values][2:] = []                    
        n[1:] = n[0:]
        n[0] = ['File Name', fileName]
        if i == 0:
            for sublists in n:
                if len(sublists)>1:
                    a[0].append(sublists[0])
                    a[1].append(sublists[1])
            a.append([])
            a.append([])
        else:
            for sublists in n:
                if len(sublists)>1:
                    a[j+1].append(sublists[0])   
                    a[j+2].append(sublists[1])
            j+=2
            a.append([])
            a.append([])       
    totaleven = []
    totalodd = [] 
    for lists in range(1,len(a),2):
        totaleven.append(a[lists-1])
        totalodd.append(a[lists])   
    a = []
    a.append(totaleven)
    a.append(totalodd)
    return a

# sort the meta data in order for it to be in the templated form below, then check if emails are fraudlent, then dump data to .csv file

def sortandwrite(n):
    template = ['File Name', 'Subject', 'From', 'To', 'Date', 'CC','BCC']
    keys = ['# of attacked sites','Blacklisted','Real email',"Purpose of use",'Disposable email','Last update']
    headers = n[0][0:]
    values = n[1][0:]
    print(headers,len(headers))
    print(values[0])
    int1 = 1
    for vals in range(0, len(template)):
        for i in range(0,len(headers)):
            if template[vals] in headers[i] and vals != headers[i].index(template[vals]) and vals<len(headers[i]):
                c = headers[i].index(template[vals])
                print(int1)
                int1+=1
                tmp = headers[i][vals]
                headers[i][vals] = headers[i][c]
                headers[i][c] = tmp
                tmp = values[i][vals]
                values[i][vals] = values[i][c]
                values[i][c] = tmp           
    print(values[0:3])
    headers[1:] = []
    print(len(headers))
    websearcher = []
    checker = []
    valuesdup = []
    for i in range(0,len(values)):
        if len(values[i])>2:
            if "@" in values[i][2]:
                print(values[i][2])
                if "<" in values[i][2]:
                    ind1 = values[i][2].index("<")
                    ind2 = values[i][2].index(">")
                    string = values[i][2][ind1+1:ind2]
                else:
                    string = values[i][2]
                if string not in checker:
                    websearcher.append(string)
                    checker.append(string)
                    valuesdup.append(values[i])
            else:
                continue  
    flags = []
    flags = websearch(websearcher,keys)
    finlist = []
    values = valuesdup
    for index in range(0,len(values)):
        finlist.append(values[index] + flags[index])
        # location of file to dump to/name of file
    with open('xxxxxxx', 'w', encoding='UTF8') as f:
        writer = csv.writer(f, lineterminator = '\n')
        writer.writerow(headers[0]+keys)
        for value in finlist:
            writer.writerow(value)

# use selenium to run emails above through a website that checks if email is fake 
         
def websearch(vals,keys):
    ind=0
    # location of gecko driver(executable path)
    browser = webdriver.Firefox(executable_path = 'xxxxxx')
    # use API to check if email is fraudlent
    browser.get('https://cleantalk.org/my/session')
    a = browser.find_element(By.ID, "login")
    # email entry 
    a.send_keys('xxxxx')
    b = browser.find_element(By.ID, "xxxxx")
    # password entry 
    b.send_keys('HySUsUjututyPEvE')
    xPath= '/html/body/div[2]/div[2]/div[2]/form/div/div[2]/div[3]/button'
    c = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xPath)))
    c.click()
    browser.get('https://cleantalk.org/spambots-check')
    infoKeys = [[]]
    st = ''
    for i in range(0, len(vals)):
        st += vals[i] + ','
    textArea = browser.find_element(By.XPATH, '//*[@id="list_form"]')
    textArea.send_keys(st)
    click =  browser.find_element(By.XPATH,'/html/body/main/div[1]/form')
    click.submit()
    appendData(infoKeys,browser,ind,len(vals))
    browser.quit()
    return infoKeys

# main function 

def main():
    # server used (certain differences must be made in code to apply to other platforms such as google)
    conn = imapclient.IMAPClient('outlook.office365.com',ssl=True)
    # enter (email, password)
    conn.login('xxxxxx','xxxxx')
    conn.select_folder('INBOX', readonly=True)
    # get all the data since june 6 2022
    num = conn.search('(SINCE 6-Jun-2022)')
    n = emailscrape(conn,num)
    sortandwrite(n)

main()
