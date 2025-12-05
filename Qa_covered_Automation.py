# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Enables incognito mode

# Launch browser in incognito mode
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://demoqa.com/")
driver.maximize_window()
driver.execute_script("document.body.style.zoom='70%'")
time.sleep(1)


def element_icon():
    # This is Javascript used to scroll the webpage
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.25);")
    time.sleep(1)

    driver.find_element(By.XPATH, "//h5[contains(text(),'Element')]").click()
    time.sleep(2)


def text_box():
    # Fill the form
    driver.find_element(By.XPATH, '//*[@id="item-0"]').click()
    driver.find_element(By.XPATH, '//*[@id="userName"]').send_keys("Jayarathna")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="userEmail"]').send_keys("jayarathna@example.com")
    driver.find_element(By.XPATH, '//*[@id="currentAddress"]').send_keys("Bommanahalli, begur road, Bangalore, 560068")
    driver.find_element(By.XPATH, '//*[@id="permanentAddress"]').send_keys(
        "Bommanahalli, begur road, Bangalore, 560068")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.25);")
    driver.find_element(By.XPATH, '//*[@id="submit"]').click()
    time.sleep(2)
    text_element = driver.find_element(By.XPATH, '//*[@id="output"]/div')
    details = text_element.text.strip()
    print(details)
    time.sleep(2)


def check_box():
    driver.find_element(By.XPATH, '//*[@id="item-1"]').click()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.25);")
    driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/span[1]').click()
    find = driver.find_element(By.XPATH, '//*[@id="result"]/span[1]')
    find_text = find.text.strip()
    print(find_text, "Check Box")
    assert find_text == "You have selected :"


def radio_button():
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="item-2"]').click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.25);")
    driver.find_element(By.XPATH, "//*[contains(text(),'Impressive')]").click()
    radio_yes = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/p')
    radio = radio_yes.text.strip()
    print("Radio button is selected", radio)
    assert radio == "You have selected Impressive"
    time.sleep(2)


def web_box():
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="item-3"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="addNewRecordButton"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys('Jayarathna')
    driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys('muthusamy')
    driver.find_element(By.XPATH, '//*[@id="userEmail"]').send_keys('jrathna@gmail.com')
    driver.find_element(By.XPATH, '//*[@id="age"]').send_keys('22')
    driver.find_element(By.XPATH, '//*[@id="salary"]').send_keys('250000')
    driver.find_element(By.XPATH, '//*[@id="department"]').send_keys('BCA')
    driver.find_element(By.XPATH, '//*[@id="submit"]').click()
    check_lg = driver.find_elements(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div')
    check_count = len(check_lg)
    print("check_count", check_count)
    find_name = []
    for i in range(1, 5):
        check = driver.find_element(By.XPATH,
                                    f'//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[{i}]/div/div')
        time.sleep(2)
        check_name = check.text.strip()
        find_name = check_name
    print("check name", find_name)


def buttons():
    actions = ActionChains(driver)
    driver.find_element(By.XPATH, '//*[@id="item-4"]').click()
    time.sleep(3)
    element = driver.find_element(By.XPATH, '//*[contains(text(),"Double Click Me")]')
    actions.double_click(element).perform()
    element1 = driver.find_element(By.XPATH, '//*[contains(text(),"Right Click Me")]')
    actions.context_click(element1).perform()
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.25);")
    time.sleep(2)
    click = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/button')
    click.click()
    time.sleep(5)
    for i in range(1, 4):
        data = driver.find_element(By.XPATH, f'//*[@id="app"]/div/div/div/div[2]/div[2]/p[{i}]')
        find_text = data.text.strip()
        print(find_text)


def alert_handle():
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[3]/span/div/div[1]').click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight / 2);")
    driver.find_element(By.XPATH, '//span[contains(text(),"Alerts")]').click()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight / 2);")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="javascriptAlertsWrapper"]/div/div[2]/button').click()
    time.sleep(3)
    driver.switch_to.alert.accept()
    print("Alert box Accepted")
    driver.find_element(By.XPATH, '//*[@id="promtButton"]').click()
    time.sleep(2)
    stro = driver.switch_to.alert
    time.sleep(2)
    stro.send_keys("Hello from Selenium")
    stro.accept()
    time.sleep(2)


element_icon()
text_box()
check_box()
radio_button()
web_box()
buttons()
alert_handle()