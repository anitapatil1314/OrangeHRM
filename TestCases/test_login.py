import time

from PageObjects.LoginPage import OrangeHRM_Login
from utilities.Logger import LogGenerator


class Test_Login:
    log = LogGenerator.loggen()

    def test_page_title_001(self, setup):
        self.log.info("Testcase test_page_title_001 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.log.info("Page Title is " + self.driver.title)
        if self.driver.title == "OrangeHRM":
            self.log.info("Taking screenshot")
            self.driver.save_screenshot("C:\\Users\\anita\\PycharmProjects\\OrangeHRM\\ScreenShots"
                                        "\\test_page_title_001_pass.PNG")
            self.driver.close()
            self.log.info("Testcase test_page_title_001 is passed")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\anita\\PycharmProjects\\OrangeHRM\\ScreenShots"
                                        "\\test_page_title_001_fail.PNG")
            self.driver.close()
            self.log.info("Testcase test_page_title_001 is failed")
            assert False

    def test_login_002(self, setup):
        self.log.info("Testcase test_login_002 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lp = OrangeHRM_Login(self.driver)
        self.log.info("Entering Username")
        self.lp.Enter_Username("Admin")
        self.log.info("Entering password")
        self.lp.Enter_Password("admin123")
        self.log.info("Clicking login button")
        self.lp.Click_Login()
        print(self.lp.Login_Status())
        self.log.info("Checking login status")
        if self.lp.Login_Status():
            self.log.info("taking screenshot")
            self.driver.save_screenshot("C:\\Users\\anita\\PycharmProjects\\OrangeHRM\\ScreenShots"
                                        "\\test_login_002_pass.PNG")
            self.log.info("Clicking on Menu button")
            self.lp.Click_Menu()
            self.log.info("Clicking on logout button")
            self.lp.Click_Logout()
            self.driver.close()
            self.log.info("Testcase test_login_002 is passed")
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\anita\\PycharmProjects\\OrangeHRM\\ScreenShots"
                                        "\\test_login_002_fail.PNG")
            self.driver.close()
            self.log.info("Testcase test_login_002 is failed")
            assert False
