import os
from os.path import join
import webbrowser as wb
import zipfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def computer_search(lookfor):
    path = 'Empty'
    for root, dirs, files in os.walk('C://'):
        print("searching",root)
        #print("root/dirs/files",root,'   ',dirs,'   ',files)
        if lookfor in files:
            path = join(root,lookfor)
            print ("found: %s" % path)
            break
    return path
path = computer_search('chromedriver.exe')
if id(path) == id('Empty'):
    browser_version = driver.capabilities['browserVersion']
    url = 'https://chromedriver.storage.googleapis.com/'+browser_version+'/chromedriver_win32.zip'
    wb.open(url)
    time.sleep(10)
    path = computer_search('chromedriver_win32.zip')
    os.mkdir('C://ChromeDriver')
    print(path)
    with zipfile.ZipFile(path,"r") as zip_ref:
        zip_ref.extractall('C://ChromeDriver/')
print("Hello.. Angry?? Frustrated?? Tense nhi lene ka apnu hai na.\n You study. Apply mein krta hu. SAVE YOUR TIME!! :-O")
print("Just Answer some of my question and watch me out.. ;-D")
print('Give me your Email ID/Username of Naukri.com')
emailId_username = input()
print('Need password too..')
password = input()
print('Please enter here Job profile/Specialization/Company name  and please separate each it with "," ')
specialization = input()
print('Job Location/Locality or just press enter if open for all locations')
location = input() 
print('Year of Experience eg: 1 , 2 .... 31')
year_of_experience = int(input())
switcher = {0:'//*[@id="ul_expDroope-experience"]/ul/li[2]/a',
            1:'//*[@id="ul_expDroope-experience"]/ul/li[3]/a',
            2:'//*[@id="ul_expDroope-experience"]/ul/li[4]/a',
            3:'//*[@id="ul_expDroope-experience"]/ul/li[5]/a',
            4:'//*[@id="ul_expDroope-experience"]/ul/li[6]/a',
            5:'//*[@id="ul_expDroope-experience"]/ul/li[7]/a',
            6:'//*[@id="ul_expDroope-experience"]/ul/li[8]/a',
            7:'//*[@id="ul_expDroope-experience"]/ul/li[9]/a',
            8:'//*[@id="ul_expDroope-experience"]/ul/li[10]/a',
            9:'//*[@id="ul_expDroope-experience"]/ul/li[11]/a',
            10:'//*[@id="ul_expDroope-experience"]/ul/li[12]/a',
            11:'//*[@id="ul_expDroope-experience"]/ul/li[13]/a',
            12:'//*[@id="ul_expDroope-experience"]/ul/li[14]/a',
            13:'//*[@id="ul_expDroope-experience"]/ul/li[15]/a',
            14:'//*[@id="ul_expDroope-experience"]/ul/li[16]/a',
            15:'//*[@id="ul_expDroope-experience"]/ul/li[17]/a',
            16:'//*[@id="ul_expDroope-experience"]/ul/li[18]/a',
            17:'//*[@id="ul_expDroope-experience"]/ul/li[19]/a',
            18:'//*[@id="ul_expDroope-experience"]/ul/li[20]/a',
            19:'//*[@id="ul_expDroope-experience"]/ul/li[21]/a',
            20:'//*[@id="ul_expDroope-experience"]/ul/li[22]/a',
            21:'//*[@id="ul_expDroope-experience"]/ul/li[23]/a',
            22:'//*[@id="ul_expDroope-experience"]/ul/li[24]/a',
            23:'//*[@id="ul_expDroope-experience"]/ul/li[25]/a',
            24:'//*[@id="ul_expDroope-experience"]/ul/li[26]/a',
            25:'//*[@id="ul_expDroope-experience"]/ul/li[27]/a',
            26:'//*[@id="ul_expDroope-experience"]/ul/li[28]/a',
            27:'//*[@id="ul_expDroope-experience"]/ul/li[29]/a',
            28:'//*[@id="ul_expDroope-experience"]/ul/li[30]/a',
            29:'//*[@id="ul_expDroope-experience"]/ul/li[31]/a',
            30:'//*[@id="ul_expDroope-experience"]/ul/li[32]/a'}
'''
print('Expected Salary Press 0 for <1 , 1 for 1 , 2 for 2 soon .... 20 for 20 LPA Or you can leave it blank too ?')
salary_switch = {
                 0:'//*[@id="ul_salaryDroope-salary"]/ul/li[2]/a',
                 1:'//*[@id="ul_salaryDroope-salary"]/ul/li[3]/a',
                 2:'//*[@id="ul_salaryDroope-salary"]/ul/li[4]/a',
                 3:'//*[@id="ul_salaryDroope-salary"]/ul/li[5]/a',
                 4:'//*[@id="ul_salaryDroope-salary"]/ul/li[6]/a',
                 5:'//*[@id="ul_salaryDroope-salary"]/ul/li[7]/a',
                 6:'//*[@id="ul_salaryDroope-salary"]/ul/li[8]/a',
                 7:'//*[@id="ul_salaryDroope-salary"]/ul/li[9]/a',
                 8:'//*[@id="ul_salaryDroope-salary"]/ul/li[10]/a',
                 9:'//*[@id="ul_salaryDroope-salary"]/ul/li[11]/a',
                 10:'//*[@id="ul_salaryDroope-salary"]/ul/li[12]/a',
                 11:'//*[@id="ul_salaryDroope-salary"]/ul/li[13]/a',
                 12:'//*[@id="ul_salaryDroope-salary"]/ul/li[14]/a',
                 13:'//*[@id="ul_salaryDroope-salary"]/ul/li[15]/a',
                 14:'//*[@id="ul_salaryDroope-salary"]/ul/li[16]/a',
                 15:'//*[@id="ul_salaryDroope-salary"]/ul/li[17]/a',
                 16:'//*[@id="ul_salaryDroope-salary"]/ul/li[18]/a',
                 17:'//*[@id="ul_salaryDroope-salary"]/ul/li[19]/a',
                 18:'//*[@id="ul_salaryDroope-salary"]/ul/li[20]/a',
                 19:'//*[@id="ul_salaryDroope-salary"]/ul/li[21]/a',
                 20:'//*[@id="ul_salaryDroope-salary"]/ul/li[22]/a'
                }
salary = int(input())
'''
print('How many application do you want to file today (Max 50)')
no_of_application = int(input())
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(12)
driver.maximize_window()
driver.get("https://www.naukri.com/nlogin/login")
driver.find_element_by_id('usernameField').send_keys(emailId_username)
driver.find_element_by_id('passwordField').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginForm"]/div[5]/div/button').click()
driver.find_element_by_id('qsb-keyskill-sugg').send_keys(specialization)
driver.find_element_by_id('qsb-location-sugg').send_keys(location)
driver.find_element_by_id('expDroope-experienceFor').click()
driver.find_element_by_xpath(switcher[year_of_experience]).click()
#driver.find_element_by_id('salaryDroope-salaryFor').click()
#driver.find_element_by_xpath(salary_switch[salary]).click()
driver.find_element_by_xpath('//*[@id="search-jobs"]/button').click()
driver.find_element_by_xpath('//*[@id="fresh_dd"]/div[1]/input[1]').click()
element = driver.find_element_by_xpath('//*[@id="#2"]')
driver.execute_script("arguments[0].click();", element)
current_application = 0
while (current_application < no_of_application and no_of_application < 50 and no_of_application > 0):
    OriginalWindow = driver.window_handles[0]
    driver.find_element_by_id('jdUrl').click()
    NewWindow = driver.window_handles[1]
    driver.switch_to.window(NewWindow)
    #driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[2]/section[1]/div[1]/div[3]/div/button[2]').click()
    try:
        element = WebDriverWait(driver, 25).until(
        EC.presence_of_element_located((By.CLASS_NAME, "apply-message"))
        )
    except TimeoutException:
        driver.close()
    finally:
        driver.close()
        driver.switch_to.window(OriginalWindow)
        driver.refresh()
        current_application+=1;
driver.find_element_by_xpath('/html/body/div[1]/div/div/ul[2]/li[2]/div/ul[2]/li[5]/a').click()
