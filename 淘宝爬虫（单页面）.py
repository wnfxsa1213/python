import selenium
from selenium import webdriver
import time
import csv
#模块导入
url = 'https://www.taobao.com/'

def search_product(key):
    driver.find_element_by_id('q').send_keys(key)#搜索框的关键字
    driver.find_element_by_class_name('btn-search').click()#搜索
    driver.maximize_window()#最大化全屏
    driver.find_element_by_class_name('icon-qrcode').click()
    time.sleep(15)#10秒用来扫码登陆


def get_product():#解析数据
    divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    #print(divs)
    for div in divs:
        info = div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text#商品名称   
        price = div.find_element_by_xpath('.//strong').text + '元'#商品价格
        people = div.find_element_by_xpath('.//div[@class="deal-cnt"]').text#付款人数
        name = div.find_element_by_xpath('.//div[@class="shop"]/a').text
        print(info, price, people, name)
        file = open('d:/bbbb.csv','a')
        file.write(info + price + people + name +' \r')
        with open('date.csv', mode='a',newline='') as filecsv:
            csvwirter = csv.writer(filecsv, delimiter=',')
            csvwirter.writerow([info, price, people, name])


def main():
    search_product(keyword)
    get_product()

if __name__ == "__main__":
    keyword = input('输入要搜索的关键字：')
    driver = webdriver.Chrome(r'd:\chromedriver.exe')
    driver.get(url)
    main()

