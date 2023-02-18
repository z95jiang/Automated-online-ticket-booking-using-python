# http://chromedriver.storage.googleapis.com/index.html
import random
import time
from time import sleep

from selenium import webdriver


class get_tickets():
    def __init__(self):
        self.account = 'zijiande@gmail.com'  # Account
        self.password = 'sq121411'  # Password
        self.driver_path = 'D:\Ticket_Booking_Automation\chromedriver'  # Drive path, this is an absolute path, put ur own driver path as need
        print('loading drive')
        try:
            self.bro = webdriver.Chrome('D:\Ticket_Booking_Automation\chromedriver')  # 
            self.bro.implicitly_wait(10)
            print('Successful loaded')
            sleep(1)
        except Exception:
            print('Driver fail loaded, please check:')
            print('1. Driver path correct')
            print('2. Is it Chrome browser')
            print('3. Driver version number should be the same with your Chrome')
            input()
            exit()

    # Login 
    def login(self):
        print('-' * 50)
        print('Directing to login page...')
        self.bro.get('https://my.tomorrowland.com/')
        self.bro.find_element('xpath', '//*[@id="root"]/div[6]/div[2]/div/div[2]/div[1]/div/form/div[1]/div/input').send_keys(self.account)
        print('Your account is', self.account)
        self.bro.find_element('xpath', '//*[@id="root"]/div[6]/div[2]/div/div[2]/div[1]/div/form/div[2]/div/input').send_keys(self.password)
        print('Password：', '*' * len(self.password))
        self.bro.find_element('xpath','//*[@id="root"]/div[6]/div[2]/div/div[2]/div[1]/div/form/div[3]/div[1]/div/button/span').click()
        print('Login succeed!')


    def redirect_url(self):
        print('-' * 20)
        # 跳转festival界面
        print('正在跳转https://www.tomorrowland.com/en/festival/welcome...')
        js = "window.open('{}','_blank');"  # 打开新标签页，打开360
        self.bro.execute_script(js.format('https://www.tomorrowland.com/en/festival/welcome'))

        self.roll_window_to_bottom(self.bro,stop_length=300)

        sleep(3)
        # 跳转tickets界面
        print('正在跳转https://www.tomorrowland.com/en/festival/tickets...')
        self.bro.execute_script(js.format('https://www.tomorrowland.com/en/festival/tickets'))
        self.bro.execute_script("window.scrollBy(0,300)")

    # 后续抢票路径完善后，写在这个函数里就可以了
    def quick_get(self):
        pass

    # 模拟人工滑动页面
    def roll_window_to_bottom(self, browser, stop_length=None, step_length=500):
        """selenium 滚动当前页面，向下滑
        :param browser: selenium的webdriver
        :param stop_length: 滑动的最大值
        :param step_length: 每次滑动的值
        """
        original_top = 0
        while True:  # 循环向下滑动
            if stop_length:
                if stop_length - step_length < 0:
                    browser.execute_script("window.scrollBy(0,{})".format(stop_length))
                    break
                stop_length -= step_length
            browser.execute_script("window.scrollBy(0,{})".format(step_length))
            time.sleep(0.5 + random.random())  # 停顿一下
            check_height = browser.execute_script(
                "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
            if check_height == original_top:  # 判断滑动后距顶部的距离与滑动前距顶部的距离
                break
            original_top = check_height

    # 主函数
    def run(self):
        self.login()
        self.redirect_url()
        self.quick_get()
        input()

if __name__ == '__main__':
    gt=get_tickets()
    gt.run()
