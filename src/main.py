from time import sleep
from src.methods import initialize, openAd

def main(username, password):
  while True:
    driver = initialize(username, password)
    tryAgainIn = openAd(driver)
    
    if (tryAgainIn != -1):
      print(f"Trying again in {tryAgainIn} minute(s)")
      driver.quit()
      sleep(tryAgainIn * 60)
      continue