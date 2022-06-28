import csv
import re
import matplotlib.pyplot as plt

# from a file that already exists, read through the data, send to website and check if email is fake/spam 

# import the file and optomize

def importFiles():
    # file name HERE
    file = open('xxxxxx','r',encoding="utf8")
    csvreader = csv.reader(file)
    rows = []
    header = next(csvreader)
    header = header[0:5]
    emails = [[]]
    counter = 0
    finrows = []
    for row in csvreader:
        rows.append(row[2])
        finrows.append(row[0:5])
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    re_equ = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    links = [[]]
    for values in rows:
        for each in values.split(" "):
            # check for specific info, replace xxxx
            if re.fullmatch(regex, each) and 'xxxxx' not in each.lower():
                emails[counter].append(re.match(regex,each).group(0))
        
        ck_url = re.findall(re_equ,values)
        # check for specific info, replace xxxx
        if 'xxxxx' not in [i[0] for i in ck_url]:
            links.append([i[0] for i in ck_url])
        counter+=1
        emails.append([])
        links.append([])
    for ind in range(0,len(finrows)):
        if len(emails[ind]) >=1 and len(links[ind]) == 0:
            finrows[ind] = finrows[ind] + emails[ind]
            finrows[ind].append("-")
        elif len(links[ind]) >= 1 and len(emails[ind]) == 0: 
            finrows[ind].append("-")
            finrows[ind] = finrows[ind] + links[ind]
        elif len(emails[ind]) >=1 and len(links[ind]) >=1:
            finrows[ind] = finrows[ind] + emails[ind]
            finrows[ind] = finrows[ind] + links[ind]
        else:
            finrows[ind].append("-")
            finrows[ind].append("-")        
    header.append("Suspicious Emails")
    header.append("Suspsicious Links")
    counter = 0
    emailchecker =[]
    Linkchecker = []
    emailcounter = []
    for lists in emails:
        for values in lists:
            emailchecker.append(values)
            counter+=1
        emailcounter.append(counter)
        counter = 0
    for lists in links:
        for values in lists:
            Linkchecker.append(values)
    linkdict = {}
    emaildict = {}
    for i in emailchecker:
        if i not in emaildict:
            emaildict[i] = 1
        else:
            emaildict[i] += 1
    for i in Linkchecker:
        if i not in linkdict:
            linkdict[i] = 1
        else:
            linkdict[i] +=1
    emaildict = {k:v for k,v in sorted(emaildict.items(), key=lambda item: item[1])}
    linkdict = {k:v for k,v in sorted(linkdict.items(), key=lambda item: item[1])}
    keys = []
    values = []
    for i in emaildict:
        keys.append(i)
        values.append(emaildict[i])
    plt.figure(100)
    reversed(keys)
    reversed(values)
    len1 = len(keys)
    len2 = len(values) 
    # plot to bar and save 
    plt.barh(keys[len1-10:len1], values[len2-10:len2], height = 0.5, color = "red", edgecolor = "black")
    plt.title("Ten Most Common Suspicious Emails")
    plt.xlabel("Total")
    plt.ylabel("Names")
    for index,value in enumerate(values[len2-10:len2]):
        plt.text(value + 0.1, index - 0.1, str(value))
    plt.savefig("SuspiciousEmails.png", bbox_inches = "tight")
    keys = []
    values = []
    for i in linkdict:
       
        keys.append(i)
        values.append(linkdict[i])
    a = []
    b = []
    for vals in keys:
        # rinse through list for specific words, replace xxxx
        if 'xxxxx' not in vals or 'xxxxx' not in vals:
            a.append(vals)
            b.append(values[keys.index(vals)])
    keys = a
    values = b
    plt.figure(200)
    reversed(keys)
    reversed(values)
    print(keys)
    len1 = len(keys)
    len2 = len(values) 
    plt.barh(keys[len1-10:len1], values[len2-10:len2], height = 0.5, color = "red", edgecolor = "black")
    plt.title("Ten Most Common Suspicious Links")
    plt.xlabel("Total")
    plt.ylabel("Names")
    for index,value in enumerate(values[len2-10:len2]):
        plt.text(value + 0.1, index - 0.1, str(value))
    plt.savefig("SuspiciousLinks.png", bbox_inches = "tight")
    file.close()
    # replace xxx with file name
    with open('xxxxx', 'w', encoding='UTF8') as f:
        write = csv.writer(f, lineterminator = '\n')
        write.writerow(header)
        for value in finrows:
            write.writerow(value)
def main():
    importFiles()

main()