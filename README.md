# air_ticket_crawler project

## Setting Up
- Install Required Python Package

        pip install selenium
        
- Download Chrome Driver

        https://sites.google.com/a/chromium.org/chromedriver/downloads 
        # Set the executable_path to the installation location of Chrome Driver
        driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")

- Set smtp server info in sending email function
        
    if using QQ mails
    
        1. Open smtp service in your qq service
        2. Get Authorization code of your mail address
        3. Set qq mail configuration 
           host_server = 'smtp.qq.com'
           #用户名
           mail_user="qq mail address"
           # 授权码
           mail_pass = "authorization code"

        