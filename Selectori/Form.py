from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Form:
    #chrome = webdriver.Chrome(ChromeDriverManager().install())
    chrome= webdriver.Chrome()
    def __init__(self):
        self.chrome.get('https://formy-project.herokuapp.com/form')
        self.chrome.maximize_window()

    def elementByID(self, ID):
        firstName = self.chrome.find_element(By.ID, f'{ID}')
        firstName.send_keys('Marius')
        sleep(3)
#linkTEXT
    def elementByLinkText(self,linkText):
        self.chrome.get('https://formy-project.herokuapp.com/')
        self.chrome.find_element(By.PARTIAL_LINK_TEXT,f'{linkText}').click()
        sleep(2)
#Name
    def ElementByName(self,Name):
        self.chrome.get('https://www.seleniumframework.com/Practiceform/')
        self.chrome.find_element(By.NAME,f'{Name}').send_keys('Romania')
        sleep(3)
#CSS
    def ElementByCSS(self, css):
        self.chrome.get('https://formy-project.herokuapp.com/form')
        return self.chrome.find_element(By.CSS_SELECTOR, f'{css}')

test = Form()
test.elementByID('first-name')
#test.elementByLinkText('Auto')
#test.ElementByName('country')
cssSelector = test.ElementByCSS('input#first-name')
sleep(2)
print(cssSelector.location)
cssSelector2 = test.ElementByCSS('input.form-control')
print(cssSelector2.location)
ex = test.ElementByCSS('input[placeholder="Enter last name"]').send_keys('Ciobanu')
sleep(3)