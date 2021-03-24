from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = Firefox()

browser.get('http://orteil.dashnet.org/cookieclicker/')

browser.implicitly_wait(5)

bigcookie = browser.find_element_by_id('bigCookie')
cookiecounts = browser.find_element_by_id('cookies')

cookieclick = ActionChains(browser)
cookieclick.click(bigcookie)

upgrades = [browser.find_element_by_id('productPrice' + str(num)) for num in range(1, -1, -1)]

try:
    while True:
        cookieclick.perform()
        cookiecount = int(cookiecounts.text.split(' ')[0])
        for upgrade in upgrades:
            cost = int(upgrade.text)
            if cookiecount >= cost:
                upgradeclick = ActionChains(browser)
                upgradeclick.move_to_element(upgrade)
                upgradeclick.click(upgrade)
                upgradeclick.perform()
except:
    print('Done')