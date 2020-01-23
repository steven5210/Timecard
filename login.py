from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl

timecard = openpyxl.load_workbook('timecard.xlsx')
sheet = timecard.get_sheet_by_name('Sheet1')

baseurl = "https://www.fieldglass.net/login.do" 
username = "Kumar" 
password = "CoolGuy"

elements_by_name = {
 'usernameTxtBox' : "username", 
 'passwordTxtBox' : "password", 
 'submitButton' : "action"
 }

elements_by_css = {
    'loginButton' : '.formLoginButton_new',
    'submitButton' : '.primaryButton'
}

timecard_boxes = {
 1 : "timein00",
 2 : "timein01",
 3 : "timein02",
 4 : "timein03",
 5 : "timein04",
 6 : "timein05",
 7 : "timein06",
 8 : "timein10",
 9 : "timein11",
 10 : "timein12",
 11 : "timein13",
 12 : "timein14",
 13 : "timein15",
 14 : "timein16",
 15 : "timein20",
 16 : "timein21",
 17 : "timein22",
 18 : "timein23",
 19 : "timein24",
 20 : "timein25",
 21 : "timein26",
 22 : "timein30",
 23 : "timein31",
 24 : "timein32",
 25 : "timein33",
 26 : "timein34",
 27: "timein35",
 28: "timein36"
 }

mydriver = webdriver.Chrome() 
mydriver.get(baseurl) 
# mydriver.maximize_window()

# Clear Username TextBox if already allowed "Remember Me"
mydriver.find_element_by_name(elements_by_name['usernameTxtBox']).clear()

# Write Username in Username TextBox
mydriver.find_element_by_name(elements_by_name['usernameTxtBox']).send_keys(username)

# Clear Password TextBox if already allowed "Remember Me"
mydriver.find_element_by_name(elements_by_name['passwordTxtBox']).clear()

#Write Password in password TextBox
mydriver.find_element_by_name(elements_by_name['passwordTxtBox']).send_keys(password)

#Click Login button
mydriver.find_element_by_css_selector(elements_by_css['loginButton']).click()

#enter timesheet page
mydriver.find_element_by_link_text(('Complete Time Sheet')).click()


#keep count of which key you are on in the dictionary
number = 1

#enter hours in from timecard.xlsx
for rowOfCellObjects in sheet['B2':'H5']:
    for cellObj in rowOfCellObjects:
        if cellObj.value is not None:
            mydriver.find_element_by_name(timecard_boxes[number]).send_keys(cellObj.value, Keys.TAB)

        if cellObj.value is None:
            mydriver.find_element_by_name(timecard_boxes[number]).send_keys(Keys.TAB)
        #incrementing by one here as you want the actual value, not which row or column you are on
        number += 1

# If you want it to submit for you
mydriver.find_element_by_css_selector(elements_by_css['submitButton']).click()
