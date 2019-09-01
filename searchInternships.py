import subprocess
from githubScrape import scrapeGithub
from sendAlert import sendSMS
import schedule
import time

schedule.every().day.at("06:00").do(scrapeGithub)

while True:
    schedule.run_pending()
    if subprocess.getoutput('diff internships2020.csv internships2020-1.csv') != "":
        sendSMS()
    subprocess.run(['cp', "internships2020-1.csv", "internships2020.csv"])
