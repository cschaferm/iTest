from selenium import webdriver

def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_login():
    driver.get("https://biblegateway.com")
    driver.find_element_by_name("quicksearch").send_keys("Math 3:16")

def test_teardown():
    driver.close()
    driver.quit()
    print("Test Complete")
