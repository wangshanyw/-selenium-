import time

# 图像处理标准库
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait


class Login(object):
    def __init__(self):
        # self.display = Display(visible=0, size=(800, 800))
        # self.display.start()
        # 创建一个参数对象，用来控制chrome以无界面模式打开
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')  # # 浏览器不提供可视化页面
        chrome_options.add_argument('--disable-gpu')  # 禁用GPU加速,GPU加速可能会导致Chrome出现黑屏，且CPU占用率高达80%以上
        chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        # self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.url = "http://www.dangdang.com/"
        # self.sli = Code()
        # 重试次数
        self.count = 3

    def login(self):
        # 请求网址
        self.browser.get(self.url)
        # 点击请登录
        button_login1 = self.browser.find_element_by_xpath("//span[@id='nickname']/a[@class='login_link']")
        button_login1.click()
        print('成功点击请登录')
        time.sleep(1)

        # 点击知道了
        close_button = self.browser.find_element_by_id("J_loginMaskClose")
        close_button.click()
        print('成功点击知道了')

        # 第三方登录
        three_party_login_qq = self.browser.find_element_by_id("qqShare")
        three_party_login_qq.click()
        
        windows = self.browser.window_handles  # 此行代码用来新窗口
        self.browser.switch_to.window(windows[1])

        # self.browser.find_element_by_id('ptlogin_iframe').click()
        # self.browser.maximize_window()
        # 切换至账户密码框
        self.browser.switch_to.frame('ptlogin_iframe')

        id_pwd_login = self.browser.find_element_by_xpath('//*[@id="switcher_plogin"]')
        # ActionChains(browser).move_to_element(id_pwd_login).perform()
        id_pwd_login.click()

        print('输入用户名和密码')
        self.browser.find_element_by_id('u').send_keys('977738078')
        time.sleep(3)
        self.browser.find_element_by_id('p').send_keys('wangshan0918')
        time.sleep(3)
        print('点击授权并登录按钮')
        self.browser.find_element_by_id('login_button').click()
        self.browser.switch_to.default_content() 
        time.sleep(2)
        print('已提交授权登录')

    def run(self):
        # 1.输入账号密码
        self.login()


login = Login()
login.run()