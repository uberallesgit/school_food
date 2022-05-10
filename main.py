from selenium import webdriver
from time import sleep
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
from datetime import datetime as dt
from datetime import timedelta as td
import os.path
import warnings
import getpass
import pywhatkit
print("v.1.0")


warnings.filterwarnings("ignore")#отключение предупреждений об устаревшем стиле


options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36")
driver = webdriver.Firefox(executable_path=r"F:\PyTHON\School_food\geckodriver.exe")

username = getpass.getuser()


def send_message(phone,message):
    pywhatkit.sendwhatmsg_instantly(phone_no=phone,message=message)


def schedule():
    pass
def time_now():
    today_is = dt.today()
    return today_is.strftime("%d.%m.%Y")
    print(time_now())




def food_file_exists():
    if os.path.exists(rf"C:\Users\{username}\Downloads\2021-ММ-ДД-sm на {time_now()}— копия.xlsx"):
        print("[INFO] Нужный файл найден  в папке 'Загрузки', поэтому переходим сразу к школьному сайту")
        school_login()
        school_upload()
        driver.close()
        driver.quit()
    else:
        mail_login()
        mail_download()
        if os.path.exists(rf"C:\Users\{username}\Downloads\2021-ММ-ДД-sm на {time_now()}— копия.xlsx"):
            school_login()
            school_upload()
            driver.close()
            driver.quit()
        else:
            print("[INFO] Файл еще не отправлен!")
            send_message("+79787229510","[INFO] Файл еще не отправлен")
            driver.close()
            driver.quit()





def mail_login():
    print("[INFO] Авторизуемся  на почте")

    driver.get("https://auth.mail.ru/cgi-bin/auth?from=portal")
    driver.implicitly_wait(20)
    try:
        input_name = driver.find_element_by_tag_name("input")
        sleep(2)
        input_name.send_keys("alex.martyn0284")
        sleep(1)
        input_name.send_keys(Keys.ENTER)
        sleep(2)
        input_password_field = driver.find_element_by_name("password")
        input_password_field.send_keys("Reremedy1")
        sleep(2)
        input_password_field.send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
    except selenium.common.exceptions.NoSuchElementException:
        input_name = driver.find_element_by_id("login")
        driver.implicitly_wait(20)
        input_name.send_keys("alex.martyn0284")
        driver.implicitly_wait(20)
        input_password_field = driver.find_element_by_id("password")
        driver.implicitly_wait(20)
        input_password_field.send_keys("Reremedy1")
        driver.implicitly_wait(20)
        accept_credentials_button = driver.find_element_by_id("EnterBtn")
        accept_credentials_button.click()
        driver.implicitly_wait(20)



def mail_download():
    print("[INFO] Ищем файл")
    antibanner = driver.find_element_by_class_name("nav__folder-name__txt").click()
    driver.implicitly_wait(20)
    links = driver.find_elements_by_class_name("llc")
    href_list = []
    for link in links:
        href = link.get_attribute("href")
        href_list.append(href)
        count = 0
    for href in href_list:
        driver.get(href)
        driver.implicitly_wait(20)
        sender = driver.find_element_by_class_name("letter-contact.letter-contact_pony-mode")
        sleep(2)
        try:
            reveal_the_small = driver.find_element_by_class_name("_1rxuLJo77v4lUrVe4mnNM6")
        except Exception as ex:
            print("[INFO] Вложений нет - идём дальше...")
            continue
        reveal_the_small = driver.find_element_by_class_name("_1rxuLJo77v4lUrVe4mnNM6")


        searched_file = driver.find_element_by_xpath(
            "/html/body/div[5]/div/div[1]/div[1]/div/div[2]/span/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[3]/div/div[1]/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/small")
        sleep(2)



        if sender.text == "Al Martyn":
            if searched_file.text == f"2021-ММ-ДД-sm на {time_now()}— копия.xlsx":
                action = ActionChains(driver)
                action.move_to_element(reveal_the_small).perform()
                download_file = driver.find_element_by_link_text("Скачать")
                action.move_to_element(download_file).click(download_file).perform()
                sleep(2)
                print("[INFO] Качаем файл")
                print("[INFO] Файл найден и успешно сохранен!")
                break
            else:
                print("[INFO] В письме отсутствует файл на нужную дату!")
                continue
        else:
            continue



def school_login():
    print("[INFO] Авторизуемся на школьном сайте")

    driver.get("https://school-perv.educrimea.ru/user/login")
    driver.implicitly_wait(20)
    login_field = driver.find_element_by_id("loginform-email")
    login_field.send_keys("uber0284@gmail.com")
    sleep(2)
    password_field = driver.find_element_by_id("loginform-password")
    password_field.send_keys("Reremedy1")
    sleep(2)
    enter_button = driver.find_element_by_name("login-button")
    enter_button.click()
    sleep(3)

def school_upload():
    print("[INFO] Загружаем скачанный с почты файл на школьный сайт")
    action = ActionChains(driver)
    sleep(1)
    conditions_link = driver.find_element_by_link_text("Условия")
    conditions_link.click()
    sleep(5)
    food_link = driver.find_element_by_link_text("Мониторинг горячего питания Минпросвещением РФ").click()
    sleep(5)
    edit_link = driver.find_element_by_link_text("Редактировать").click()
    sleep(5)
    add_files = driver.find_element_by_link_text("Добавить файлы").click()
    driver.switch_to.frame(4)
    sleep(2)
    activation = driver.find_element_by_id("nav-l1_Lw")
    action.move_to_element(activation).perform()
    sleep(3)
    upload_files = driver.find_element_by_xpath("/html/body/div/div[1]/div[4]/div[3]/span[1]")
    upload_files.click()
    sleep(5)
    hover = driver.find_element_by_css_selector("div.ui-button:nth-child(3)")
    sleep(4)

    action.move_to_element(hover).perform()
    sleep(3)
    choose_file = driver.find_element_by_xpath("//input[@type='file']")
    choose_file.send_keys(rf"C:\Users\{username}\Downloads\2021-ММ-ДД-sm на {time_now()}— копия.xlsx")
    sleep(5)
    arrow_button = driver.find_element_by_css_selector("div.elfinder-buttonset:nth-child(3) > div:nth-child(1)")
    action.move_to_element(arrow_button).perform()
    sleep(5)
    arrow_button = driver.find_element_by_class_name("ui-state-default.elfinder-button.ui-state-hover")
    arrow_button.click()
    print("[INFO] Файл загружен на школьный сайт!")
    print("[INFO] Для проверки перейдите по ссылке: https://school-perv.educrimea.ru/food")
    sleep(10)

def file_delete():
    print("[INFO] Удаляем загруженный файл")
    pass







def main():
    # schedule()
    time_now()
    food_file_exists()



if __name__ == "__main__":
    main()