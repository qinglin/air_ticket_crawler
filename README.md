# air_ticket_crawler project

## Setting Up
- Install Required Python Package

        pip install selenium
        
- Download Chrome Driver

        https://sites.google.com/a/chromium.org/chromedriver/downloads 
        # Set the executable_path to the installation location of Chrome Driver
        driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")

- Set smtp server info in sending email function