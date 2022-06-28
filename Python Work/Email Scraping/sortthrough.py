import matplotlib.pyplot as plt
import numpy as np

# sort through a large set of data (over 5000 entries initially) and plot 
def totalGraph(a):
    m = []
    for x in a:
        for y in x.split(","):
            if " " in y and ":" in y and "C" not in y and "W" not in y and "[" not in y and "/" in y and "R" not in y and "G" not in y:
                m.append(y[1])
    n = m[0]
    counter = 1
    ultList = []
    for nums in range(1,len(m)-1):
        if m[nums] == n:
            counter+=1
        else:
            ultList.append(counter)
            n = m[nums]
            counter = 1
    ultList.append(counter)
    monthList = ["jan","feb","march","apr","may", "jun"]
    New_Colors = ['green','blue','purple','brown','teal', 'orange']
    plt.figure(100)
    plt.bar(monthList, ultList, color = New_Colors, edgecolor = "black")
    plt.title('Months vs Phishing Occurrences')
    plt.xlabel('Reports')
    plt.ylabel('Total')
    for index, value in enumerate(ultList):
        plt.text(index, value,
                str(value))
    plt.savefig("MonthsvsPhishing")
    return ultList
def totalRedFlagGraph(a):
    m = []
    for x in a:
        tmpList = x.split(",")
        ind = len(tmpList)-1
        m.append(tmpList[ind])

    m.pop(0)
    valDict = {}
    for flags in m:
        if flags in valDict:
            valDict[flags] += 1
        else:
            valDict[flags] = 1
    valList = list(valDict.values())
    valDict = {k: v for k, v in sorted(valDict.items(), key = lambda item: item[1])}
    totalMissFlagged = 0
    totalThreats = 0
    for keys in valDict: 
        if "N/A" in keys.upper():
            totalMissFlagged += valDict[keys]
        else: 
            totalThreats += valDict[keys]
    totalList = [totalMissFlagged, totalThreats]
    xLabel = ["Non-Threats", "Threats"]
    barColor = ["green", "red"]
    print(totalMissFlagged, totalThreats)
    plt.figure(200)
    plt.bar(xLabel,totalList, color = barColor, edgecolor = "black")
    plt.title('Total Threats vs Non-Threats')
    plt.xlabel('Reports')
    plt.ylabel('Total')
    for index, value in enumerate(totalList):
        plt.text(index, value,
                str(value))
    plt.savefig("totalThreatsvsNonThreats.png")
def monthlyRedFlagGraph(a, monthList):
    m = []
    for x in a:
        tmpList = x.split(",")
        ind = len(tmpList)-1
        m.append(tmpList[ind])
    m.pop(0)
    monthOrder = {}
    monthDict = {}
    i = 0
    for keys in monthList:
        monthOrder[keys] = []
        monthDict[keys] = {}
        for values in m:
            monthOrder[keys].append(values)
            i+=1
            if i == keys:
                print(len(monthOrder[keys]))
                i = 0
                break
        for values in monthOrder[keys]:
            if values in monthDict[keys]:
                monthDict[keys][values] += 1
            else:
                monthDict[keys][values] = 1
    totalMissFlagged = 0
    totalThreats = 0
    flaggedList = []
    threatsList = []
    for keys in monthDict: 
        for vals in monthDict[keys]:
            if "N/A" in vals.upper():
                totalMissFlagged += monthDict[keys][vals]
            else: 
                totalThreats += monthDict[keys][vals]
        flaggedList.append(totalMissFlagged)
        threatsList.append(totalThreats)
        totalMissFlagged = 0
        totalThreats = 0
    print(flaggedList, threatsList)
    months = ["jan", "feb", "march", "apr", "may", "jun"]
    width = 0.25
    n = 6
    r = np.arange(n)
    plt.figure(300)
    plt.bar(r, flaggedList, color = 'green',
            width = width, edgecolor = 'black',
            label='Miss-Flagged')
    plt.bar(r + width, threatsList, color = 'red',
            width = width, edgecolor = 'black',
            label='Threats')
    plt.xlabel("Months")
    plt.ylabel("Total Number Flagged")
    plt.title("Threats vs Non-Threats per Month")
    # plt.grid(linestyle='--')
    plt.xticks(r + width/2,months)
    plt.legend() 
    for index, value in enumerate(flaggedList):
        plt.text(index-0.1, value +0.15,
                str(value))
    for index, value in enumerate(threatsList):
        plt.text(index+0.1, value + 0.15,
                str(value))
    plt.savefig("NonThreatsVSThreats.png")
    topTenVals = []
    topTenNames = []
    for key in monthDict:
        monthDict[key] = {k: v for k, v in sorted(monthDict[key].items(), key = lambda item: item[1])}
        keys = list(monthDict[key].keys())
        keys1 = []
        for vals in keys:
            if "N/A" not in vals:
                keys1.append(vals)
        keys = keys1   
        a = []
        b = []
        for i in range(len(keys)-1, len(keys)-11,-1):
            a.append(monthDict[key][keys[i]])
            if '"' in keys[i]:
                keys[i] = keys[i].replace('"','')
            b.append(keys[i])
        topTenVals.append(a)
        topTenNames.append(b)
    plt.figure(300)
    topTenNames.reverse()
    print(topTenVals[0])
    print(monthDict[295])
    width = 0.5
    month = ["January","February","March","April","May", "June"]
    for i in range(len(topTenVals)):
        plt.figure((i*100)+500)
        plt.barh(topTenNames[i], topTenVals[i], width, color = 'red', edgecolor = 'black' )
        plt.xlabel("Threats")
        plt.ylabel("Threat Name")
        plt.title("Top Ten Threats in " + month[i])        
        for index, value in enumerate(topTenVals[i]):
            plt.text(value + 0.1, index,
                    str(value))
        plt.subplots_adjust(left=0.336)
        saveName = "threats" + month[i] + ".png"
        plt.savefig(saveName,  bbox_inches ="tight")

def main(): 
    # file name here
    f = open("xxxxx", "r")
    a = []
    for x in f:
        for values in x.split("\n"):
            if values != "":
                a.append(values)
    monthList = totalGraph(a)
    totalRedFlagGraph(a)
    monthlyRedFlagGraph(a, monthList)
    
main()