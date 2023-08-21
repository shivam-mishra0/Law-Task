from config import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_redirected_page_source(home_url, input_xpath):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        driver.get(home_url)

        # Wait for the input element to be present
        wait = WebDriverWait(driver, 10)
        input_element = wait.until(
            EC.presence_of_element_located((By.XPATH, input_xpath)))

        input_element.click()

        redirected_page_source = driver.page_source

        driver.quit()

        return redirected_page_source
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    home_url = web_url  # Replace with your home URL
    # Replace with the XPath of the navigation link
    link_xpath = "//input[@value='Case Number']"
    redirected_source = get_redirected_page_source(home_url, link_xpath)

    if redirected_source:
        print("Redirected Page Source:")
        print(redirected_source)
    else:
        print("Failed to get redirected page source.")
