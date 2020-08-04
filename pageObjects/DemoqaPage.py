import pytest
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass

class FillForm(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    # firstname = (By.ID, "firstName")
    # lastname = (By.ID, "lastName")
    # emailid = (By.ID, "userEmail")
    # genderm = (By.XPATH, "//*[text()='Male']")
    # sports = (By.XPATH, "//*[text()='Sports']")

    #tap
    firstname = (By.XPATH, "//div[@id='q2']//input[@id='RESULT_TextField-1']")
    lastname = (By.XPATH, "//input[@name='RESULT_TextField-2']")
    genderm = (By.XPATH, "//*[text()='Male']")
    day = (By.XPATH, "//*[text()='Sunday']")
    timec = (By.XPATH, "//*[@class='drop_down']")
    scrollelementclick= (By.XPATH, "/html//input[@id='age']")
    alertbutton= (By.XPATH, "//button[.='Click Me']")
    doubleclick = (By.XPATH, "//*[text()='Copy Text']")
    draggable = (By.XPATH, "//*[text()='Drag me to my target']")
    droppable = (By.XPATH, "//*[text()='Drop here']")
    iframe = (By.XPATH, '//div[@class="post-body entry-content"]/iframe')

    def switchiframe(self):
        BaseClass.switchToFrame(self,self.iframe)

    def enterFirstName(self, firstnametxt):
        BaseClass.clickElement(self,self.firstname)
        # BaseClass.sendkeysExecuter(self,self.firstname,firstnametxt)
        BaseClass.setText(self, self.firstname,firstnametxt)

    def enterLastName(self, lastnametxt):
        BaseClass.setText(self, self.lastname,lastnametxt)

    def enterGender(self):
        BaseClass.select_RadioButtonOnlyWhenItsNotSelected(self, self.genderm)
        BaseClass.wait(self, 5)

    def enterDay(self):
        BaseClass.select_CheckBoxOnlyWhenItsNotSelected(self,self.day)
        BaseClass.wait(self, 5)

    def timedropdown(self):
        BaseClass.enterDropdownValue_usingVisibleText(self,"Morning",self.timec)
        BaseClass.wait(self, 5)

    def alertelement(self):
        BaseClass.alert_accept(self, self.alertbutton)

    def doubleclickelement(self):
        BaseClass.doubleClick(self,self.doubleclick)

    def scrolltillelementfound(self):
        BaseClass.scrolltillelement(self, self.scrollelementclick)
        BaseClass.wait(self, 5)

    def dragdropelements(self):
        BaseClass.dragAndDrop(self,self.draggable, self.droppable)

