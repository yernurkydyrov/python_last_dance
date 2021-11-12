from flask import Flask, request, render_template
import tableforass4
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from sqlalchemy.sql import text

app = tableforass4.app
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'


@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template("login.html")


@app.route("/index", methods=['POST'])
def main():
    username = request.form.get("username")
    password = request.form.get("password")
    userid = 1
    tableforass4.Usser.tablefunc(userid)
    if username == tableforass4.loginn and password == tableforass4.passwordd:
        return render_template("main.html")
    return "Something went wrong"


@app.route("/form")
def form_page():
    return render_template("find.html")


@app.route('/form', methods=['POST'])
def form_answer():
    coin_name = request.form.get("coin_name")
    news_counter = request.form.get("news_count")

    url = 'https://coinmarketcap.com/currencies/' + coin_name + '/news/'

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=r'C:\Users\HP\Downloads\chromedriver.exe', options=options)
    driver.get(url)
    button = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[3]/div/div/main/button')
    for i in range(3):
        button.click()
        time.sleep(8)

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    divs = soup.find('div', {'class': 'wav26n-1 gWmJSZ'})
    tags = divs.find_all('a')

    newsList = []
    counter = 0
    for i in tags:
        newsList.append(i.text)
        counter = counter + 1
        if counter == news_counter:
            break

    driver.close()

    new_info = tableforass4.News(1, 'bitcoin', 'hello1', 'hello2', 'hello3', 'hello4', 'hello5', 'hello6', 'hello7',
                                 'hello8', 'hello9', 'hello10', 'hello11', 'hello12', 'hello13', 'hello14', 'hello15',
                                 'hello16', 'hello17', 'hello18', 'hello19', 'hello20')
    tableforass4.db.session.add(new_info)
    tableforass4.db.session.commit()

    count_for_table = 1
    list_index = 0
    for i in newsList:
        with tableforass4.engine.connect() as connection:
            result = connection.execute(text(
                "update News set news{0} = $${1}$$ where News.coin_name = '{2}'".format(str(count_for_table), newsList[
                    list_index], str(coin_name))))
        connection.close()
        if count_for_table == newsList:
            break
        count_for_table = count_for_table + 1
        list_index = list_index + 1

    return render_template("form.html", len=len(newsList), listofnews=newsList, amount=int(news_counter))


@app.route('/display')
def table_display():
    pass


@app.route('/scraper')
def scraper():
    url = 'https://coinmarketcap.com/currencies/bitcoin/news/'

    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=r'C:\Users\HP\Downloads\chromedriver.exe', options=option)
    driver.get(url)
    button = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[3]/div/div/main/button')
    for i in range(4):
        button.click()
        time.sleep(5)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('div', {'class': 'wav26n-1 gWmJSZ'})
    tags = divs.find_all('a')

    hello = ''
    counter = 0
    for i in tags:
        f"{hello}{str(i)}\n--------------------------------------------------\n"
        counter = counter + 1
        if counter == 20:
            break

    driver.close()

    return hello


if __name__ == '__main__':
    app.run(debug=True)
