from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Test_Sauce:
    def test1(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(1)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(1)
        usernameInput.send_keys()
        passwordInput.send_keys()
        sleep(1)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(1)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
       
        testResult = errorMessage.text == "Epic sadface: Username is required" 
        print(f"TEST SONUCU: {testResult}")
        sleep(1)

    def test2(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(1)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(1)
        usernameInput.send_keys(1)
        passwordInput.send_keys()
        sleep(1)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(1)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
       
        testResult = errorMessage.text == "Epic sadface: Password is required" 
        print(f"TEST SONUCU: {testResult}")
        sleep(1)
    
    def test3(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(1)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(1)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(1)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(1)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
       
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")
        sleep(1)

    def test5and6(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(1)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(1)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(1)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(1)
        loginBtn.click()

        # test 6
        inventoryItem = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Toplam ürün sayısı: {len(inventoryItem)}")
        sleep(1)

    def test4(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(1)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys()
        sleep(1)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys()
        sleep(1)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(1)
        loginBtn.click()

        errorBtn = driver.find_element(By.CLASS_NAME, "error-button")
        sleep(1)
        errorBtn.click()
        sleep(1)


testClass = Test_Sauce()
testClass.test1()
testClass.test2()
testClass.test3()
testClass.test5and6()
testClass.test4()




