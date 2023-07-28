# pip install mysql-connector-python : mysql python연동 라이브러리
# import mysql.connector
# try: 
#     connector = mysql.connector.connect(host="localhost", port="3406", user="root", password="1234", database="board")
#     # 커서 객체는 데이터베이스에서 쿼리의 결과를 검색하고 순회하는데 사용되는 객체 
#     cursor = connector.cursor()
# except mysql.connector.Error as err:
#     print(err)
# add_data = "insert into author(name, email) values(%s, %s)"
# data = ("John","hello2@naver.com") #변수화
# try:
#     cursor.execute(add_data,data) #add_data에 data추가 
#     connector.commit() #insert후 확정
# except mysql.connector.Error as err:
#     print(err)
# cursor.close() #객체 그만 사용하겠다.는 뜻 
# connector.close()

# 코인시세 10초에 한번씩 db insert
# ex.
    # import time
    # while True:
    #     print("hello world")
    #     time.sleep(10) #10초에 한번씩 time.sleep
import mysql.connector
import requests
import json
import time

while True:
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data_json = json.loads(response.text)
    for a in data_json:
        if a["symbol"] == 'BTCUSDT':
            try: 
                connector = mysql.connector.connect(host="localhost", port="3406", user="root", password="1234", database="practice")
                cursor = connector.cursor()
            except mysql.connector.Error as err:
                print(err)
            add_data = "insert into coin_price(coin_name, last_price) values(%s, %s)"
            data = ("BTCUSDT",a["lastPrice"])
            try:
                cursor.execute(add_data,data) 
                connector.commit() 
            except mysql.connector.Error as err:
                print(err)
            cursor.close()
            connector.close()
    time.sleep(10)