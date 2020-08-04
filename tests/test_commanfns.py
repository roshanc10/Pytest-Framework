import time
from selenium import webdriver
from utilities.BaseClass import BaseClass
from pageObjects.DemoqaPage import FillForm


class Test_DemoQA(BaseClass):

    def test_form(self):
        testform=FillForm(self.driver)
        print("fill form")
        
        testform.alertelement()
        
        testform.doubleclickelement()
        
        testform.dragdropelements()
        time.sleep(5)
        testform.scrolltillelementfound()
        
        testform.switchiframe()
       
        print ("frame switched")
        
        #testform.enterFirstName("john")
        #time.sleep(5)
        #testform.enterLastName("smith")
        #testform.wait(5)
        testform.enterGender()
        
        testform.enterDay()
        
        testform.timedropdown()
        
        testform.switchToFrameDefault()
        


'''
    c1.scrollDownWindow("2500",driver1)
    time.sleep(15)
    c1.scrollDownPage(driver1)

    elementOption = driver.find_element_by_xpath('//div[@class="category-cards"]/div')
    c1.clickElement(elementOption)

    datewidget = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[4]')
    c1.scrolltillelement(datewidget, driver)
    time.sleep(5)
    c1.clickElement(datewidget)
    # datewidgetclick=driver.find_element_by_xpath("//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']//div[@class='accordion']/div[4]/div/ul[@class='menu-list']/li[3]/span[@class='text']")
    datewidgetclick = driver.find_element_by_xpath("//*[text()='Date Picker']")
    c1.clickElement(datewidgetclick)
    dateclick = driver.find_element_by_xpath("//*[contains(@id,'datePickerMonthYearInput')]")
    c1.clickElement(dateclick)
    yearselct = driver.find_element_by_xpath("//select[@class='react-datepicker__year-select']")
    c1.enterDropdownValue_usingVisibleText(yearselct, "1996")
    monthselct = driver.find_element_by_xpath("//select[@class='react-datepicker__month-select']")
    c1.enterDropdownValue_usingVisibleText(monthselct, "August")
    dateselct = driver.find_element_by_xpath("//*[text()='17']")
    c1.clickElement(dateselct)



    udOption = driver.find_element_by_xpath('//*[@id="item-6"]/span')
    c1.scrolltillelement(udOption,driver)
    time.sleep(5)
    c1.clickElement(udOption)
    download = driver.find_element_by_xpath("/html//a[@id='downloadButton']")
    c1.clickElement(download)
    fileupload=driver.find_element_by_xpath('//*[@class="form-control-file"]')
    fileupload.send_keys(r"C:\Users\Abhishek\Desktop\1roshan\amz.png")


    # check box
    # elementCheckBox = driver.find_element_by_xpath('(//*[@id="item-1"])[1]')
    # c1.clickElement(elementCheckBox)
    # homecheckBox = driver.find_element_by_xpath('//*[@id="tree-node"]/ol/li/span/label/span[1]')
    # print(c1.check_elementisCheckBoxOrNot(homecheckBox))
    # c1.select_CheckBoxOnlyWhenItsNotSelected(homecheckBox)

    # radio button
    elementRadioButton = driver.find_element_by_xpath('(//*[@id="item-2"])[1]')
    c1.clickElement(elementRadioButton)
    checkBox = driver.find_element_by_xpath('//*[@id="impressiveRadio"]')
    # c1.select_RadioButtonOnlyWhenItsNotSelected(checkBox)
    c1.ClickByJavaExecuter(checkBox, driver)
    # checkBox2 = driver.find_element_by_xpath('//*[@id="yesRadio"]')
    # c1.select_RadioButtonOnlyWhenItsNotSelected(checkBox2)

    # # double click
    # elementbtn = driver.find_element_by_xpath('(//*[@id="item-4"])[1]')
    # c1.clickElement(elementbtn)
    # elementDoubleClick = driver.find_element_by_xpath('//*[@id="doubleClickBtn"]')
    # c1.rightClick(elementDoubleClick, driver)
    #
    # # Right click
    # elementbtn = driver.find_element_by_xpath('(//*[@id="item-4"])[1]')
    # c1.clickElement(elementbtn)
    # elementDoubleClick = driver.find_element_by_xpath('//*[@id="rightClickBtn"]')
    # c1.rightClick(elementDoubleClick, driver)
    #
    # # switch window
    # elementWindowsAndFrame = driver.find_element_by_xpath(
    #     '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[3]/span/div')
    # c1.ClickByJavaExecuter(elementWindowsAndFrame, driver)
    #
    # elementbrowser = driver.find_element_by_xpath('(//*[@id="item-0"]/span)[3]')
    # c1.clickElement(elementbrowser)
    #
    # newTab = driver.find_element_by_xpath('//*[@id="tabButton"]')
    # c1.clickElement(newTab)
    # c1.switchToWindow(1, driver)
    # newBrowserElement = driver.find_element_by_xpath('//*[@id="sampleHeading"]')
    # c1.assertElements(newBrowserElement.text, "This is a sample page")
    # c1.switchToWindow(0, driver)
    #
    # newWindow = driver.find_element_by_xpath('//*[@id="windowButton"]')
    # c1.clickElement(newWindow)
    # c1.switchToWindow(1, driver)
    # newBrowserElement = driver.find_element_by_xpath('//*[@id="sampleHeading"]')
    # c1.assertElements(newBrowserElement.text, "This is a sample page")
    # c1.switchToWindow(0, driver)


    # iframe
    elementWindowsAndFrame = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[3]/span/div')
    c1.ClickByJavaExecuter(elementWindowsAndFrame, driver)
    # elementIFrame = driver.find_element_by_xpath('(//*[@id="item-2"]/span)[2]')
    # c1.clickElement(elementIFrame)
    # frame = driver.find_element_by_xpath('//*[@id="frame1"]')
    # c1.switchToFrame(frame, driver)
    # textName = driver.find_element_by_xpath('//*[@id="sampleHeading"]')
    # c1.assertElements(textName.text, "This is a sample page")
    time.sleep(3)
    
    
    #alerts
    alertwindow=driver.find_element_by_xpath("//div[@ class ='accordion']/div[3]/div/ul[@class='menu-list']/li[2]")
    c1.ClickByJavaExecuter(alertwindow,driver)
    time.sleep(3)
    alertclick=driver.find_element_by_xpath("/html//button[@id='alertButton']")
    c1.clickElement(alertclick)
    time.sleep(1)
    c1.alert_accept(driver)
    time.sleep(5)
    alertclick5sec=driver.find_element_by_xpath("//button[@id='timerAlertButton']")
    c1.clickElement(alertclick5sec)
    time.sleep(10)
    c1.alert_accept(driver)
    alertconfirm = driver.find_element_by_xpath("//button[@id='confirmButton']")
    c1.clickElement(alertconfirm)
    time.sleep(3)
    c1.alert_dismiss(driver)
    alertconfirmtextbox = driver.find_element_by_xpath("//button[@id='promtButton']")
    c1.clickElement(alertconfirmtextbox)
    time.sleep(3)
    c1.alert_sendkey(driver,"ok")
    time.sleep(3)
    c1.alert_accept(driver)


    # drag drop
    # elementInteraction = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[5]/span/div')
    # c1.ClickByJavaExecuter(elementInteraction, driver)
    # elementDragDrop = driver.find_element_by_xpath('(//*[@id="item-3"])[4]')
    # c1.ClickByJavaExecuter(elementDragDrop, driver)
    # elementsource = driver.find_element_by_xpath('//*[@id="draggable"]')
    # elementdestination = driver.find_element_by_xpath('//*[@id="droppable"]')
    # c1.dragAndDrop(elementsource, elementdestination, driver)

'''