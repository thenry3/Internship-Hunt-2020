import subprocess
from githubScrape import scrapeGithub
from sendAlert import sendSMS
import schedule
import time


def runCheck():
    scrapeGithub()
    output = subprocess.getoutput(
        'diff internships2020.csv internships2020-1.csv')
    if output != "":
        sendSMS(output)
    subprocess.run(['cp', "internships2020-1.csv", "internships2020.csv"])


schedule.every().hour.do(runCheck)

print("Starting internship search")

while True:
    schedule.run_pending()
    time.sleep(0.5)
