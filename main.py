from selenium import webdriver

firefox = webdriver.Firefox()
firefox.get('http://google.com.br')
# search = firefox.find_element_by_id("input")
search2 = firefox.find_element('name', "q")
search2.send_keys('consegui')
firefox.close()
print('yohoo')