from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

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
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument("--mute-audio")

  driver = webdriver.Chrome(options=chrome_options)
  driver.get("https://en.onlinesoccermanager.com/")

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
      openAdButton = driver.find_elements(by=By.CLASS_NAME, value="product-free")[0]
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
            
            if (minutesStr == "a"):
              tryAgainIn = 1
            else:
              tryAgainIn = int(minutesStr) + 1

            break
          except:
            print("Ad closed")
            tryAgainIn = openAd(driver)
            break
      
      break
    except:
      continue
  
  return tryAgainIn