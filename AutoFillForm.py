from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.keys import Keys

Form_url= 'https://docs.google.com/forms/d/e/1FAIpQLSf3iNS3mL2jErW1Gjtqp8CbbMNpb57M4GnkLNTYG8w0qrRPKw/formResponse'

data= ""
data= data.split("?")
userName=  data[0]
password=  data[1]
params=    data[2]
date=      data[3]

params= params.split(';')
date= date.split(';')
userName= userName.split(',')
password= password.split(',')
successEmail=[]

for i in range(0,len(userName)):
    params[i]= params[i].split(',')
    date[i]= date[i].split(',')

ro=0
def Login(driver):
    driver.find_element_by_id('identifierId').send_keys(userName[ro])
    driver.find_element_by_id('identifierId').send_keys(Keys.ENTER)
    sleep(3)
                
    driver.find_element_by_xpath("//*[@jsname = 'YPqjbf']").send_keys(password[ro])
    driver.find_element_by_xpath("//*[@jsname = 'YPqjbf']").send_keys(Keys.ENTER)

def FillForm(driver):
    global ro
    try:
        Head= driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[1]/div/div[2]/div').text
        if Head=="嘉中圖書館自修室線上報名":
            element= driver.find_element_by_tag_name("input")
            element.send_keys(userName[ro])
            driver.find_element_by_xpath("//*[@jsname = 'OCpkoe']").click()
            sleep(1.5)
       
            driver.find_element_by_xpath("//*[@jsname = 'OCpkoe']").click()
            sleep(1)
      
            for i in range(3,8):
                String= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[' + str(i) + ']/div/div/div[2]/div/div[1]/div/div[1]/input'
                driver.find_element_by_xpath(String).send_keys(params[ro][i-3])
            for i in range(1,8):
                if int(date[ro][i-1]):
                    String= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[' + str(i*2) + ']/span/div[2]/div'
                    driver.find_element_by_xpath(String).click()
            for i in range(1,3):
                String= '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div['+str(i*2)+']/span/div[3]/div'
                driver.find_element_by_xpath(String).click()
                            
            driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]').click()
            driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span').click()
            sleep(3)
            if ro:
                successEmail.append(userName[ro])
            ro+=1
    except:
        String= driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]').text
        if String=="您已經提交過回覆":
            ro+=1
        else:
            sleep(60)
            driver.refresh()
            FillForm(driver)

while ro<len(userName):
    # 基本設定
    options = Options()
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-gpu')
    #options.add_argument('--disable-dev-shm-usage')
    # Chrome 位置
    #"/bin/google-chrome"
    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    # webdriver 位置
    #'/home/uu/chromedriver'
    webdriver_path = "C:\\Users\\Weng  john\\Downloads\\chromedriver_win32\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=webdriver_path, options=options)
    try:
        try:
            driver.get(Form_url)
            sleep(1)
            Login(driver)
            sleep(5)
            FillForm(driver)
        except:
            driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")
            sleep(2)
            Login(driver)
            sleep(5)
            driver.get(Form_url)
            sleep(3)
            FillForm(driver)
    except:
        ro+=1
    finally:
        driver.close()

for i in successEmail:
    userName.remove(i)

if len(successEmail):
    # 基本設定
    options = Options()
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-gpu')
    #options.add_argument('--disable-dev-shm-usage')
    # Chrome 位置
    #"/bin/google-chrome"
    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    # webdriver 位置
    #'/home/uu/chromedriver'
    webdriver_path = "C:\\Users\\Weng  john\\Downloads\\chromedriver_win32\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=webdriver_path, options=options)
    driver.get("https://mail.google.com/mail/u/0/#inbox")
    driver.find_element_by_id('identifierId').send_keys("john4303210")
    driver.find_element_by_id('identifierId').send_keys(Keys.ENTER)
    sleep(3)
                
    driver.find_element_by_xpath("//*[@jsname = 'YPqjbf']").send_keys("john4303210")
    driver.find_element_by_xpath("//*[@jsname = 'YPqjbf']").send_keys(Keys.ENTER)
    sleep(6)
    driver.find_element_by_xpath('//*[@id=":l9"]/div/div').click()
    sleep(5)
    Str= " ".join(successEmail)
    Str+=" "
    driver.find_element_by_xpath('/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/textarea').send_keys(Str)
    driver.find_element_by_xpath('/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[3]/div/input').send_keys("圖書館自修室自動填表程式")
    driver.find_element_by_xpath('/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div').send_keys("自修室已填報成功！！！")
    driver.find_element_by_xpath('/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]').click()
    sleep(5)
    driver.close()
    if len(userName):
        print(userName)
