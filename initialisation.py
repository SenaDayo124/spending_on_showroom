from selenium import webdriver


def save_cookies():
    driver = webdriver.Chrome()
    driver.get("https://www.showroom-live.com/")
    # user login
    while input("Press OK when you finish login ") != "ok":
        print("Please enter 'OK'!")
    cookies = driver.get_cookies()
    with open("cookies.txt", "w") as file:
        for cookie in cookies:
            file.write(f"{cookie['name']}:{cookie['value']}\n")
    driver.quit()


save_cookies()