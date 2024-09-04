from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:
    """ This class allows us to bypass 'Please Verify You Are a Human' using Selenium. """

    def __init__(self, chrome_path=ChromeDriverManager().install(), headless=True):
        # Define the Options object
        self.__options = Options()
        if headless:
            self.__options.add_argument("--headless")  # Headless mode

        # Define the Service object with the local path to ChromeDriver if it exists otherwise install it
        self.__service = Service(chrome_path)

        # Define the WebDriver object
        self.__driver = webdriver.Chrome(service=self.__service, options=self.__options)

    def open_website(self, url):
        # Open a website
        self.__driver.get(url)

    def find_element_by_class_name(self, class_name):
        # Get element by HTML class name
        element = self.__driver.find_element(By.CLASS_NAME, class_name)
        return element

    def find_element_by_tag_name(self, tag_name):
        # Get element by HTML tag name
        element = self.__driver.find_element(By.TAG_NAME, tag_name)
        return element

    def find_element_by_class_name_in_bloc(self, bloc_name, class_name):
        # Get element by HTML class name in specific bloc
        element = bloc_name.find_element(By.CLASS_NAME, class_name)
        return element

    def find_element_by_tag_name_in_bloc(self, bloc_name, tag_name):
        # Get element by HTML tag name in specific bloc
        element = bloc_name.find_element(By.TAG_NAME, tag_name)
        return element

    def find_elements_by_class_name(self, class_name):
        # Get element by HTML class name
        elements = self.__driver.find_elements(By.CLASS_NAME, class_name)
        return elements

    def find_elements_by_tag_name(self, tag_name):
        # Get element by HTML tag name
        elements = self.__driver.find_elements(By.TAG_NAME, tag_name)
        return elements

    def quit_driver(self):
        # Quit the driver
        self.__driver.quit()
