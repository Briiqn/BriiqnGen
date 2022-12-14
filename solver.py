import asyncio
import os
import traceback
import zipfile
from random import Random, random
from time import sleep

import random

import random_name_generator as rng
import selenium.webdriver.chrome.webdriver
import whisper
from selenium.webdriver import Keys
from selenium import webdriver
from sys import platform
from os.path import exists
import urllib.request
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.proxy import ProxyType, Proxy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

import Recognize

file_Win = "chromedriver.exe"
file_Tux = "chromedriver"
file_exists_Win = exists("chromedriver.exe")
file_exists_Tux = exists("chromedriver")


def init():
    try:
        yes = int(input("Enter Amount to Generate: "))
        if (yes >= 1):
            return yes

    except ValueError:
        print("Please Choose An Integer")
        print("Defaulting to 1")
        return 1


def postinit():
    yes = input("Do Asynchronously? [Y/N]: ")
    if yes == "Y":
        return True
    elif (yes == "N"):
        return False
    else:
        postinit()


def chooseip():
    choicefile = open("proxies.txt", "r")
    linelist = []
    for line in choicefile:
        linelist.append(line)
    choice = random.choice(linelist)
    return choice


def getChromeDriverWin():
    os.system('pip install -r requirements.txt')
    os.system('cls')
    if platform == "windows":
        if not file_exists_Win:
            print("Downloading For Windows")
            urllib.request.urlretrieve(
                "https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_win32.zip",
                'chromedriver_win32.zip')
            with zipfile.ZipFile("chromedriver_win32.zip", "r") as zip_ref:
                zip_ref.extractall("")

    else:
        print("Already Downloaded ChromeDriver For Windows")


def getChromeDriverLinux():
    os.system('clear')
    if platform == "linux":
        if not file_exists_Tux:
            print("Downloading For Linux")
            urllib.request.urlretrieve(
                "https://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_linux64.zip",
                'chromedriver_linux64.zip')
            with zipfile.ZipFile("chromedriver_linux64.zip", "r") as zip_ref:
                zip_ref.extractall("")
            os.system('chmod ugo+rwx chromedriver')
        else:
            os.system('chmod ugo+rwx chromedriver')


            print("Already Downloaded ChromeDriver For Linux")


if (platform == "windows"):
    if (exists("chromedriver_win32.zip")):
        os.remove("chromedriver_win32.zip")

    getChromeDriverWin()

if (platform == "linux"):
    if (exists("chromedriver_linux64.zip")):
        os.remove("chromedriver_linux64.zip")

    getChromeDriverLinux()

def getchromedriverfile():
    if platform == "windows":
        return file_Win
    elif platform == "linux":
        return file_Tux

async def dostuff():
    # ignore if statement, before it was a while loop but i wanted to do shit asynchronsly and im to lazy too indent atm
    if 1 == 1:
        try:
            options = webdriver.ChromeOptions()
            prefs = {"download.default_directory": os.getcwd() + "/audio",
                     "directory_upgrade": True}
            options.add_experimental_option("prefs", prefs)
            options.add_argument("--headless")

            b = chooseip()
            if b != ("null" or "127.0.0.1" or "0.0.0.0" or ""):
                print("Using Proxy " + b)
                prox = Proxy()
                prox.proxy_type = ProxyType.MANUAL
                prox.http_proxy = ""
                prox.socks_proxy = ""
                prox.ssl_proxy = b
                capabilities = webdriver.DesiredCapabilities.CHROME
                prox.add_to_capabilities(capabilities)
            else:
                capabilities = webdriver.DesiredCapabilities.CHROME
            if(platform=="win32"):
              service = Service(os.getcwd() + 'chromedriver.exe')
            else:
               service = Service(os.getcwd() + 'chromedriver')

            driver = webdriver.Chrome(service=service, options=options, desired_capabilities=capabilities)

            driver.get(
                "http://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&rver=7.3.6963.0&wp=MBI_SSL&wreply=https:%2f%2faccount.xbox.com%2fen-us%2faccountcreation%3freturnUrl%3dhttps%253a%252f%252fwww.xbox.com%252fen-US%252f%26ru%3dhttps%253a%252f%252fwww.xbox.com%252fen-US%252f%26rtc%3d1%26csrf%3d4NvumwFeIxkduv685k-" + os.urandom(
                    6).hex() + "-rLc7tcmQvG-U4A8cSbDeu4BdJD4b6mbybZ4qQTJsk1&id=292543&nopa=2&aadredir=1&contextid=20967FDBB12B6547&bk=1665004140&uiflavor=web&lic=1&mkt=EN-US&lc=1033&uaid=097f1096b47942eaac87bae7fb551145")

            await asyncio.sleep(2)
            element = WebDriverWait(driver, 75).until(EC.presence_of_element_located((By.ID, "liveSwitch")))
            element.click()
            element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, "LiveDomainBoxList")))
            element.click()
            element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "MemberName")))
            element.click()
            random = os.urandom(5).hex()
            randompass = os.urandom(6).hex()
            print("Trying To Generate BriiqnGen" + random + "@outlook.com" + " : " + randompass)

            element.send_keys("BriiqnGen" + random)
            element.send_keys(Keys.ENTER)
            await asyncio.sleep(.7)
            element = WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.ID, "PasswordInput")))
            element.click()
            element.send_keys(randompass)
            element.send_keys(Keys.ENTER)
            await asyncio.sleep(.7)

            element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "FirstName")))
            element.click()
            element.send_keys(rng.generate(descent=rng.Descent.ENGLISH, sex=rng.Sex.UNISEX, limit=1))
            element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "LastName")))
            element.click()
            element.send_keys(rng.generate(descent=rng.Descent.ENGLISH, sex=rng.Sex.UNISEX, limit=1))
            element.send_keys(Keys.ENTER)
            await asyncio.sleep(.7)

            element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "Country")))
            element.click()
            element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "BirthMonth")))
            element.click()
            element.send_keys(Keys.TAB)
            element.send_keys(Keys.DOWN)
            element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "BirthDay")))
            element.click()
            element.send_keys(Keys.TAB)
            element.send_keys(Keys.DOWN)
            element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "BirthYear")))
            element.click()
            element.send_keys(Keys.TAB)
            element.send_keys(Keys.DOWN)
            element.send_keys(Keys.ENTER)
            await asyncio.sleep(3)
            element = WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.ID, "enforcementFrame")))
            element.click()
            driver.switch_to.frame("enforcementFrame")
            driver.switch_to.frame("fc-iframe-wrap")

            element = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "fc_meta_audio_btn")))
            element.click()
            driver.switch_to.default_content()
            await asyncio.sleep(2)

            driver.switch_to.frame("enforcementFrame")
            e = str(driver.execute_script("return document.documentElement.outerHTML"))

            # download audio
            f = e.split('name="verification-token" value="')
            g = f[1].split('|')

            urllib.request.urlretrieve(
                "http://client-api.arkoselabs.com/fc/get_audio/?session_token=" + g[
                    0] + "&analytics_tier=40&r=us-west-2&d=1&game=0&language=en-gb",
                'audio/challenge' + g[0] + ".wav")
            driver.switch_to.default_content()
            element = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "enforcementFrame")))

            print(" ↳Listening To Captcha for BriiqnGen" + random + "@outlook.com")

            element.send_keys(Keys.TAB)
            element.send_keys(Keys.TAB)
            element.send_keys(Keys.TAB)

            h = Recognize.transcribe('audio/challenge' + g[0] + ".wav", "base").replace(",", "").replace(" ",
                                                                                                          "").replace(
                "One", "1").replace("Two", "2").replace("Three", "3").replace("Four", "4").replace("Five", "5").replace(
                "Six", "6").replace("Seven", "7").replace("Eight", "8").replace("Nine", "9").replace("Zero",
                                                                                                     "0").replace(
                ".", "").replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace(
                "five", "5").replace(
                "six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9").replace("zero",
                                                                                                     "0").replace(
                ".", "").replace("Run", "1").replace("Thanks", "2").replace("for", "4").replace("watching",
                                                                                                "1").replace("!",
                                                                                                             "").replace(
                "or", "4").replace("-", "").replace("run", "1")
            print("     ↳understood captcha (" + h + ")")
            actions = ActionChains(driver)

            actions.send_keys(h)
            actions.perform()
            os.remove('audio/challenge' + g[0] + ".wav")

            element.send_keys(Keys.TAB)
            element.send_keys(Keys.ENTER)
            await asyncio.sleep(7)
            driver.get(
                "http://account.xbox.com/")
            element = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='xbox-accountcreation-va053wj']/div/div[4]")))
            await asyncio.sleep(2)

            element = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.ID, "Accept")))
            element.click()
            await asyncio.sleep(9)

            f = open("accounts.txt", "a")
            f.write("BriiqnGen" + random + "@outlook.com" + " : " + randompass + "\n")
            f.close()
            print(
                "         ↳BriiqnGen" + random + "@outlook.com" + " : " + randompass + " was sucessfully generated!\n")
            driver.close()
        except:

            print("Something went wrong, (bad proxy?),(Timed Out??)" + "\n________________________")
            traceback.print_exc()
            await dostuff()


async def execasync():
    j = init()

    if (postinit()):
        await asyncio.gather(*(dostuff() for i in range(j)))
    else:
        h = 1
        if h <= j:
            h = h + 1
            await asyncio.gather(*(dostuff() for i in range(1)))
        else:
            print("Done")
            return 0

asyncio.run(execasync())
