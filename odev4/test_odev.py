from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path 
from datetime import date
import openpyxl
from constants import globalConstants

class Test_Sauce:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(globalConstants.URL)
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
    
    def waitForElementVisible(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
    
    def teardown_method(self):
        self.driver.quit()
    
    @pytest.mark.parametrize("username, password", [("","1")])
    def test1(self, username, password):

        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        
        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput, username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()
        
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
       
        self.driver.save_screenshot(f"{self.folderPath}/test1{username}-{password}.png")

        assert errorMessage.text == "Epic sadface: Username is required"

    @pytest.mark.parametrize("username, password", [("a","")])
    def test2(self, username, password):
        
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput, username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        
        self.driver.save_screenshot(f"{self.folderPath}/test2{username}-{password}.png")

        assert errorMessage.text == "Epic sadface: Password is required" 

    @pytest.mark.parametrize("username, password", [("locked_out_user","secret_sauce")])
    def test3(self, username, password):
        
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput, username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
       
        self.driver.save_screenshot(f"{self.folderPath}/test3{username}-{password}.png")
    
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    @pytest.mark.parametrize("username, password", [("standard_user","secret_sauce")])
    def test5and6(self, username, password):
        
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput, username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        self.driver.save_screenshot(f"{self.folderPath}/test5and6{username}-{password}.png")

        # test 6
        inventoryItem = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Toplam ürün sayısı: {len(inventoryItem)}")

    @pytest.mark.parametrize("username, password", [("","")])
    def test4(self, username, password):
        
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        
        action = ActionChains(self.driver)
        action.send_keys_to_element(usernameInput, username)
        action.send_keys_to_element(passwordInput,password)
        action.perform()

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test4{username}-{password}.png")

        errorBtn = self.driver.find_element(By.CLASS_NAME, "error-button")
        errorBtn.click()


