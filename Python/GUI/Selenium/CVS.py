from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = Firefox()

browser.get('https://www.cvs.com/minuteclinic/covid-19-testing?icid=cvs-home-hero1-link1-coronavirus-testing')

browser.maximize_window()

def no_thanks_popup():
    try:
        nothanks = browser.find_element_by_css_selector('a.acsInviteButton:nth-child(6)')
        nothanksclick = ActionChains(browser).click(nothanks).perform()
    except:
        pass

no_thanks_popup()

statelabel = browser.find_element_by_id('state-label')
no_thanks_popup()
statelabel.send_keys('07621')
no_thanks_popup()
statelabelsubmit = browser.find_element_by_css_selector('.redbutton')
no_thanks_popup()
statelabelsubmitaction = ActionChains(browser).click(statelabelsubmit).perform()

no_thanks_popup()
browser.implicitly_wait(3)
dob = browser.find_element_by_id('dateOfBirth')
no_thanks_popup()
dob.send_keys('09041982')

no_thanks_popup()

browser.execute_script('window.scrollBy(0, 1200)')

healthcare = browser.find_element_by_id('healthcare-no')
healthcareclick = ActionChains(browser).click(healthcare).perform()

exposure = browser.find_element_by_id('exposure-no')
exposureclick = ActionChains(browser).click(exposure).perform()

workrisk = browser.find_element_by_id('workrisk-no')
workriskclick = ActionChains(browser).click(workrisk).perform()

residentrisk = browser.find_element_by_id('residentrisk-no')
residentriskclick = ActionChains(browser).click(residentrisk).perform()

priority = browser.find_element_by_id('priority-no')
priorityclick = ActionChains(browser).click(priority).perform()


firsttime = browser.find_element_by_id('firsttime-yes')
firsttimeclick = ActionChains(browser).click(firsttime).perform()

acknowledgement = browser.find_element_by_id('acknowledgement')
acknowledgementclick = ActionChains(browser).click(acknowledgement).perform()

pagetwosubmit = browser.find_element_by_id('submit-button')
pagetwosubmitclick = ActionChains(browser).click(pagetwosubmit).perform()