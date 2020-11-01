from selenium import webdriver
import time

username = ""
password = ""

def login():
    print(">>>>>>>>>>>>>>> Python TO Download E-Lab Reports <<<<<<<<<<<<<<")
    print("Enter the Username:",end=" ")
    username = input()
    print("Enter the Password:",end=" ")
    password = input()

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://care.srmist.edu.in/srmncrppsoops/student/home")
    driver.find_element_by_xpath("//app-root/div[@class='container']/app-login[@class='ng-star-inserted']//mat-card//form/mat-form-field[1]//input[@name='username']").send_keys(username)
    driver.find_element_by_xpath("//app-root/div[@class='container']/app-login[@class='ng-star-inserted']//mat-card//form/mat-form-field[2]//input[@name='password']").send_keys(password)
    driver.find_element_by_xpath("//app-root//app-login[@class='ng-star-inserted']//mat-card//form/button[@type='submit']").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/app-root/div/app-student-home/div/mat-card/div/div/app-student-home-card/mat-card/p").click()
    flowchart(driver)
def flowchart(driver):
    time.sleep(5)
    driver.get("https://care.srmist.edu.in/srmncrppsoops/student/solve/2411111")
    print("Questions which are not 100 percent completed: ")
    for i in range(1,101,1):
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div/div[2]/mat-card/div[3]/button[2]").click()
        time.sleep(5)
        a = driver.find_elements_by_xpath("/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div/div[2]/mat-card/div[4]/a[2]")
        
        if len(a)>0:
            driver.find_element_by_xpath("/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div/div[2]/mat-card/div[4]/a[2]").click()
        else:
            print("Question %d is not complete"%(i))
        driver.find_element_by_xpath("/html/body/app-root/div/app-student-solve/div[1]/button[2]").click()
        #time.sleep(3)
login()
