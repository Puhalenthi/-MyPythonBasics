from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains

browser = Firefox()
browser.get('https://www.clickspeedtester.com/')

browser.implicitly_wait(5)

clickbox = browser.find_element_by_css_selector('#page > button')

clickboxclick = ActionChains(browser)
clickboxclick.click(clickbox)


try:
    while True:
        clickboxclick.perform()
except:
    print('Done')

browser.quit()