from time import sleep
from src.methods import initialize, openAd
from src.colors import bcolors
from datetime import datetime

def main(username, password, headless=False):
  while True:
    driver = initialize(username, password, headless)
    tryAgainIn = openAd(driver)
    
    if (tryAgainIn != -1):
      now = datetime.now()
      nextTry = now.replace(minute=now.minute + tryAgainIn)
      
      print(bcolors.FAIL + "Ad not available. Trying again at " + nextTry.strftime("%H:%M") + " (in " + str(tryAgainIn) + " minute(s)).\n(DON'T CLOSE THIS WINDOW)" + bcolors.ENDC)
      driver.quit()
      sleep(tryAgainIn * 60)
      continue