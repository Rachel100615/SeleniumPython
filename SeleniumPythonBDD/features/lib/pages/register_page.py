#coding=utf-8
from features.lib.pages.base_page import BasePage
from selenium.webdriver.common.by import By
class RegisterPage(BasePage):
    def __init__(self,context):
        super(RegisterPage,self).__init__(context.driver)

    def send_useremail(slef,useremail):
        slef.find_element(By.ID,'register_email').send_keys(useremail)

    def send_username(slef,username):
        slef.find_element(By.ID,'register_nickname').send_keys(username)

    def send_password(slef,password):
        slef.find_element(By.ID,'register_password').send_keys(password)

    def send_code(self,code):
        self.find_element(By.ID,'captcha_code').send_keys(code)

    def click_register_button(self):
        self.find_element(By.ID,'register_btn').click()

    def get_code_text(self):
        return self.find_element(By.ID,'captcha_code-error').text()




