from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from time import sleep
from src.colors import bcolors

def consentToAds(driver):
  isConsentRootAvailable = False
  try:
    consentRoot = driver.find_element(by=By.CLASS_NAME, value="fc-consent-root")
    isConsentRootAvailable = True
  except:
    isConsentRootAvailable = False
  
  if isConsentRootAvailable:
    consentRoot = driver.find_element(by=By.CLASS_NAME, value="fc-consent-root")
    consentButton = consentRoot.find_element(by=By.CLASS_NAME, value="fc-cta-consent")
    consentButton.click()


def initialize(username, password):
  print(bcolors.OKBLUE + "\n\nInitializing controlled browser window..." + bcolors.ENDC)
  
  chromedriver_autoinstaller.install()
  
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument("--mute-audio")

  driver = webdriver.Chrome(options=chrome_options)
  driver.get("https://en.onlinesoccermanager.com/")
  
  print(bcolors.OKGREEN + "Browser window initialized." + bcolors.ENDC)

  # accept cookies
  while True:
    try: 
      acceptPolicyBtn = driver.find_element(by=By.CLASS_NAME, value="btn-orange")
      acceptPolicyBtn.click()
      break
    except:
      continue

  # go to login page
  while True:
    try:
      registerInformationBlock = driver.find_elements(by=By.CLASS_NAME, value="register-information-block")
      goToLoginButton = registerInformationBlock[1].find_element(by=By.TAG_NAME, value="button")
      goToLoginButton.click()
      break
    except:
      continue

  # enter username & password, press login button
  while True:
    try:
      usernameInput = driver.find_element(by=By.ID, value="manager-name")
      passwordInput = driver.find_element(by=By.ID, value="password")
      loginButton = driver.find_element(by=By.ID, value="login")

      usernameInput.send_keys(username)
      passwordInput.send_keys(password)
      loginButton.click()
      
      print(bcolors.OKGREEN + "Logged in." + bcolors.ENDC)
      break
    except:
      continue
        
  # open store
  while True:
    consentToAds(driver)
    try:
      navbar = driver.find_element(by=By.ID, value="navbar")
      dropdowns = navbar.find_elements(by=By.CLASS_NAME, value="dropdown-toggle")
      shopButton = dropdowns[2]
      shopButton.click()
      break
    except:
      continue

  return driver
  

def openAd(driver):
  tryAgainIn = -1
  
  consentToAds(driver)
  
  while True:
    try:
      freeProducts = driver.find_elements(by=By.CLASS_NAME, value="product-free")
      freeProducts[1].click()
      
      openAdButton = freeProducts[0]
      openAdButton.click()
      
      # use while loop to keep the ad open and when closed open another one
      while True:
        try:
          isModalOpen = driver.find_element(by=By.CLASS_NAME, value="videoAdUi")
          if isModalOpen: continue
        except:
          try:
            sleep(1)
            limitReached = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'You have reached the maximum of videos you can watch here.')]")
            minutesStr = limitReached.text.split("Come back in ")[1].split(" ")[0]
            
            print(bcolors.OKGREEN + "Ad watched." + bcolors.ENDC)
            
            if (minutesStr == "a"):
              tryAgainIn = 1
            else:
              tryAgainIn = int(minutesStr) + 1

            break
          except:
            print(bcolors.OKGREEN + "Ad watched." + bcolors.ENDC)
            tryAgainIn = openAd(driver)
            break
      
      break
    except:
      continue
  
  return tryAgainIn