from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# WITH VISIBLE CHROME WINDOW
# driver = webdriver.Chrome()

# HEADLESS
options = webdriver.ChromeOptions()
options.add_argument('window-size=1366x768')
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

driver.get('http://www.python.org')

# PRINT PAGE SOURCE
# print(driver.page_source)

# LIST MAIN NAV LINKS
print('MENU ITEMS:')
for menuitem in driver.find_elements_by_css_selector('#mainnav ul li.tier-1'):
    print(menuitem.find_element_by_css_selector('a').text)
print()

# NAVIGATE TO ABOUT PAGE
driver.find_element_by_css_selector('#mainnav ul li.tier-1').click()

# SEARCH FOR "python release"
searchbox = driver.find_element_by_css_selector('#id-search-field')
searchbox.send_keys('python release')
searchbox.send_keys(Keys.RETURN)

print('SEARCH RESULTS:')
for result in driver.find_elements_by_css_selector('ul.list-recent-events li h3 a'):
    print(result.text)
print()

driver.close()
