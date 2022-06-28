from selenium import webdriver
import time
import mouse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import csv
# In this version of the email scraper, instead of using imaps I had to manually use selenium. This is b/c IMAP is disabled on shard folders.
# the code below goes through and scrolls through around 10,000 emails. When the email loads up, it grabs the data in said email and dumps to .csv file 
# this is for outlook
# executable path in xxx
browser=webdriver.Firefox(executable_path = 'xxxx')
browser.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1655299584&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d7638e1be-da22-68f1-4bae-429585f2bb02&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld")
a = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "i0116")))
# email input xxx
a.send_keys("xxxxx")
b = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
b.click()
a = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "passwordInput")))
# password input xxx
a.send_keys("xxxx")
b = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "submitButton")))
b.click()
b = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
b.click()
b = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]")))
b.click()
b = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID , "mectrl_OwaOpenTargetMailboxLink")))
b.click()
time.sleep(1)
a = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/form/div[1]/div/div/div/div/div[1]/div/div/input")))
# resource folder name xxx
a.send_keys("xxxx")
time.sleep(2)
a.send_keys(Keys.ENTER)
time.sleep(1)
b = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/form/div[2]/div/span[1]/button")))
b.click()
chwd = browser.window_handles[0]
browser.switch_to.window(window_name=chwd)
browser.close()
browser.switch_to.window(window_name = browser.window_handles[0])
time.sleep(2)
mouse.drag(0, 0, 636,725, absolute = True, duration = 0.1)
counter = 0
j = 51
emails = [[]]
connector = 0
timer = 0
browser.maximize_window()
attachcount = 0
# metadata values that were extracted by xpath below; I found that every time i scrolled for around 0.5 seconds, around 50 emails would load with some margin of error.
# this margin of error would be fixed for with the try and except; if the for loop went past the amount loaded, it would have a counter to tell the code to go back that amount in the next rotation and 
# continue scraping 
while (True):
    try:
        for i in range(j-50, j):
            try:
                date ="/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/div["+str(i)+"]/div/div/div[1]/div[2]/div[2]/span"
                a = browser.find_element(By.XPATH,date)
                Subject = "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/div[" + str(i) + "]/div/div/div[1]/div[2]/div[2]/div/span"
                b = browser.find_element(By.XPATH, Subject)
                body = "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/div["+str(i)+"]/div/div/div[1]/div[2]/div[3]/div/div/span"
                c = browser.find_element(By.XPATH, body)
                recepient = "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/div["+str(i)+"]/div/div/div[1]/div[2]/div[1]/div[1]/span"
                d = browser.find_element(By.XPATH, recepient)
                emails[timer].append(a.text)
                emails[timer].append(b.text)
                emails[timer].append(c.text)
                emails[timer].append(d.text)
                for ind in range(0,5):
                    try:
                        attachment = "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/div/div[1]/div[2]/div/div/div/div/div/div["+str(i)+"]/div/div/div[1]/div[2]/div[4]/div/div["+str(ind)+"]"
                        e = browser.find_element(By.XPATH, attachment)
                        attachcount+=1
                    except:
                        continue
                    
                emails[timer].append(attachcount)
                attachcount = 0
                timer+=1
                emails.append([])
            except:
                connector+=1
        if counter >=1:
            mouse.drag(645, 725, 636,727, absolute = True, duration = 0.1)
        mouse.press(button = 'left')
        time.sleep(0.6)
        mouse.drag(636, 725, 645,725, absolute = True, duration = 0.1)
        counter+=1
        if j > 205:
            j+=49-connector
        else:
            j+=50-connector
        connector = 0
        if counter == 400:
            mouse.release(button = 'left')
            print(counter)
            print(j)
            print(timer)
            break
    except:
        break
headers = ["date","Subject","Body","Recepient","# of Attachments"]
# name of file in xxx
with open('xxxxx', 'w', encoding='UTF8') as f:
    writer = csv.writer(f, lineterminator = '\n')
    writer.writerow(headers)
    for value in emails:
        writer.writerow(value)
