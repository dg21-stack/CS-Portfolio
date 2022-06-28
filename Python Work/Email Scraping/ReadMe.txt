Four different functions each having to do with the analysis of over a year's worth of email data in a phishing resource folder:

1) emailcheckandflag.py --> Read through the data in a .csv file created with scroll.py and check if the emails contained with are spam and also identify any fake or false linked

2) scroll.py --> preload around 50 emails at a time and dump the metadata to a .csv file, continously scrolling until reaching the bottom

3) sortthrough.py --> sort through a large set of data and plot the contained information

4) emailflaganddump.py --> use the imap library and selenium to first scrape emails and then check if those emails are spam/hazards