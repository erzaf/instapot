from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from colorama import Fore, Style

class Automate:

    def __init__(self, username, password, target):
        self.username = username
        self.password = password
        self.target = target

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        engine = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
        engine.minimize_window()
        try:
            print("Login with: "+self.username)
            engine.get("https://instagram.com")
            WebDriverWait(engine,30).until(EC.element_to_be_clickable((By.NAME, 'username'))).send_keys(self.username)
            WebDriverWait(engine,30).until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys(self.password)
            WebDriverWait(engine,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button'))).click()

            WebDriverWait(engine,30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input')))
            print("Processing the report.....(The speed depends on your internet connection)")
            engine.get("https://www.instagram.com/"+self.target)
            WebDriverWait(engine,60).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[2]/button'))).click()
            WebDriverWait(engine,60).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[text()="Report"]'))).click()
            WebDriverWait(engine,60).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/button[2]/div/div[text()="Report Account"]'))).click()
            WebDriverWait(engine,60).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[1]'))).click()
            WebDriverWait(engine,60).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/button[6]/div/div[text()="Hate speech or symbols"]'))).click()
            WebDriverWait(engine,60).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/button[text()="Submit report"]'))).click()
            WebDriverWait(engine,60).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[1]/h4[text()="Thank you, we received your report"]')))
            WebDriverWait(engine,60).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div[4]/button[text()="Close"]'))).click()
            engine.close()
            print("Target account ("+self.target+") has been reported => "+ Fore.GREEN +"[OK]" + Style.RESET_ALL)
            print("Waiting few seconds to avoid rate limits....")
            print("#####################")
            time.sleep(4)
        except Exception:
            engine.close()
            print(Fore.RED +"An error has occured, probably you have incorrect username/password, your Insta account not been verified, or your IP has blocked"+ Style.RESET_ALL)
            print("#####################")