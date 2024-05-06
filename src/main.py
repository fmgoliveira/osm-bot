from time import sleep
from src.methods import initialize, openAd
from src.colors import bcolors

def main(username, password):
  while True:
    driver = initialize(username, password)
    tryAgainIn = openAd(driver)
    
    if (tryAgainIn != -1):
      print(bcolors.FAIL + "Ad not available. Trying again in " + str(tryAgainIn) + " minute(s).\n(DON'T CLOSE THIS WINDOW)" + bcolors.ENDC)
      driver.quit()
      sleep(tryAgainIn * 60)
      continue