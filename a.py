from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select


# Initialize the Chrome WebDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

url = "https://beta.playo.club/login"

try:
    # Open the URL
    driver.get(url)

    # Select user name, password and login button

    username_input = driver.find_element(By.CSS_SELECTOR, "#TextInputField-1")
    password_input = driver.find_element(By.CSS_SELECTOR, "#TextInputField-2")
    login_button = driver.find_element(By.XPATH,"//button[normalize-space()='Login']")

    # Enter user id and password

    username_input.send_keys("ravi_admin")
    password_input.send_keys("hoodi1")
    time.sleep(50)

    login_button.click()


    # Wait for 5 seconds
    time.sleep(5)

    # Click On calendar
    calendar = driver.find_element(By.CSS_SELECTOR,"#nested-list-label")
    calendar.click()
    time.sleep(2)


    # Select from dropdown
    dropdown = driver.find_element(By.CSS_SELECTOR,"#SelectField-3")
    select = Select(dropdown)

    select.select_by_visible_text("Badminton Standard Synthetic")
    time.sleep(3)


    # loop Through all the slots
    for tr in range(1,35):
        for td in range(1,7):
            button = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/table[1]/tbody[1]/tr[{tr}]/td[{td}]".format(tr = tr,td = td))
            if button.text != "Book":
                button.click()
           
    # Select a slot

    # booking_id = driver.find_element(By.XPATH,"//strong[normalize-space()='341515B72']")

    # court = driver.find_element(By.CSS_SELECTOR,"#RBDDC-A1-type-three-label")

    # date_time = driver.find_element(By.CSS_SELECTOR,"#RBDDC-A1-type-two-label")

    # price = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[5]/div[5]/div[1]/strong[2]")



    # # Print the selected option text

    # print("Booking id:", booking_id.text)
    # print("Court:", court.text)
    # print("Date_time:", date_time.text)
    # print("Price: ", price.text)

except Exception as e:
    print("An error occurred:", str(e))

# finally:
#     # Close the WebDriver
#     driver.quit()