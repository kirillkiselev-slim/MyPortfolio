from time import sleep
from pathlib import Path
import re, csv, os, pytz, send2trash
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime


options = webdriver.ChromeOptions()
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://our_backend")
sleep(20)
wait = WebDriverWait(browser, 25)

lst = []
dir = Path("C:/Users/name/Projects/fun/RulesPriceFilesRUS")

def main():
    for filename in os.listdir(dir):
        match = re.search(r"(\d+\.\d+)[-_](\d+\.\d+)[\s_]([\w].*?)(\d{2}|[1-9])[%]?.xlsx", filename)
        if match:
            number = match.group(4)
            name = match.group(3)
            start_date = match.group(1)
            ending_date = match.group(2)

            MoscowTz = pytz.timezone("Europe/Moscow")
            timeinMoscow = datetime.now(MoscowTz)
            currentTimeInMoscow = timeinMoscow.strftime("%d.%m.%Y %H:%M")
            pricing_rule = f"{start_date}-{ending_date} {name}{number}% RUS"

            priority_number = get_priority(listwithDicts(), str(number))
            filename = returnFilename(ending_date,dir,name, number)
            directory = str(Path(dir))
            current_time = f"{currentTimeInMoscow}"  # change value here
            end_date = f"{ending_date}.2023 23:59"  # change value here

            ElemPlus = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "grid-button")))
            ElemPlus.click()

            sleep(2)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='price-rules-edit-form']/form/div/div[1]/div/div/div[1]/div[2]/div"))).click()
            sleep(2)
            itemslist = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="dx-item dx-list-item"]')))
            itemslist.click()
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                               '//*[@id="price-rules-edit-form"]/form/div/div[1]/div/div/div[1]/div[5]/div/div/span'))).click()
            sleep(1)
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                             '//*[@id="price-rules-edit-form"]/form/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input'))).send_keys(
                "RUS")
            sleep(1)
            wait.until(EC.presence_of_element_located((By.XPATH,
                                                                     '//*[@id="price-rules-edit-form"]/form/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input'))).send_keys(
                Keys.ENTER)
            wait.until(EC.presence_of_element_located((By.XPATH,
                                                       '//*[@id="price-rules-edit-form"]/form/div/div[1]/div/div/div[2]/div[1]/div/div/div/div[1]/input'))).send_keys(
                Keys.TAB)
            sleep(2)

            name = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="price-rules-edit-form"]/form/div/div[1]/div/div/div[2]/div[2]/input')))
            name.send_keys(pricing_rule)
            sleep(2)

            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                     '//*[@id="price-rules-edit-form"]/form/div/div[1]/div/div/div[2]/div[4]/div/div[1]/div/div[1]'))).click()
            sleep(1)
            wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="dx-list-select-all"]'))).click()
            sleep(1)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div/div'))).click()
            sleep(2)
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                              "//*[@id='price-rules-edit-form']/form/div/div[1]/div/div/div[2]/div[5]/div/div/div[1]/input"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                     "//*[@id='price-rules-edit-form']/form/div/div[1]/div/div/div[2]/div[5]/div/div/div[1]/input"))).send_keys(
                priority_number)
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                              "//*[@id='price-rules-edit-form']/form/div/div[1]/div/div/div[2]/div[6]/div/div/div[1]/input"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                     "//*[@id='price-rules-edit-form']/form/div/div[1]/div/div/div[2]/div[6]/div/div/div[1]/input"))).send_keys(
                number)

            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                               '//*[@id="price-rules-edit-form"]/form/div/div[1]/div/div/div[2]/div[7]/div/div/span'))).click()

            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                           "//*[@id='price-rules-edit-form']/form/div/div[1]/div/div/div[3]/div[1]/div/div/div/div[1]/input"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                 "//*[@id='price-rules-edit-form']/form/div/div[1]/div/div/div[3]/div[1]/div/div/div/div[1]/input"))).send_keys(
                current_time)

            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                           "//*[@id='price-rules-edit-form']/form/div/div[1]/div/div/div[3]/div[1]/div/div/div/div[1]/input"))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                  "//*[@id='price-rules-edit-form']/form/div/div[1]/div/div/div[3]/div[2]/div/div/div/div[1]/input"))).send_keys(
                end_date)

            wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="formik-form-submit-button"]'))).click()
            sleep(1)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="price-rule-items-data-grid"]/div/div[4]/div/div/div[3]/div[1]/div'))).click()
            sleep(1)
            fileLoader = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                    '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/input')))
            fileLoader.send_keys(directory + '\\' + filename)
            sleep(1)
            wait.until(EC.presence_of_element_located((By.XPATH,
                                                                     '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div[2]'))).click()
            sleep(1)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[3]/div/div[1]/div/div[3]/div/div/div'))).click()
            sleep(1)
            wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="formik-form-submit-button"]'))).click()
            sleep(12.2)
            wait.until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div'))).click()

            sleep(2.3)
            delete_file = os.path.join(directory, filename)
            send2trash.send2trash(directory, delete_file)
def listwithDicts():
    with open(r"C:\Users\name\Downloads\priority_discount.csv", "r") as csv_file:
        dictReader = csv.DictReader(csv_file, delimiter=";")
        for row in dictReader:
            lst.append(row)
    return lst


def get_priority(list, discount):
    for dictionary in list:
        if discount in dictionary['discount']:
            return dictionary['priority']


def returnFilename(date, directory, rule_name, discount):
    for file in os.listdir(directory):
        if rule_name in file and discount in file and date in file:
            return os.path.basename(file)


if __name__ == "__main__":
    main()
