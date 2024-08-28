# import pymysql


# conn = pymysql.connect(host='localhost',
#                        user = 'root',
#                        password = 'root',
#                        db = 'ShopDB',
#                        charset= 'utf8')

# # 데이터베이스에 SQL 문을 실행하거나 실행된 결과를 돌려받는 통로
# # 앞에서 만든 연결자에 cursor() 함수를 연결하여 생성
# curs = conn.cursor()

# # SQL 실행
# sql = "SELECT * FROM Product"
# curs.execute(sql)

# # fethchone() cursor에 저장된 데이터를 한 행씩 추출
# # fetchmany(size) cursor에 저장된 데이터를 size 개의 행 추출
# # fetchall() cursor에 저장된 데이터를 모두 추출

# # # 모든 데이터 가져오기
# # result = curs.fetchall()

# # # result 타입 확인
# # print(type(result))

# # # 출력
# # for data in result:
# #     print(data)

# # # 2줄의 데이터만 가져오기
# # result = curs.fetchmany(2)

# # # 출력
# # for data in result:
# #     print(data)

# # result = curs.fetchone()

# # print(result)

# # result = curs.fetchall()
# # print("데이터 출력:", result)

# # result = curs.fetchone()
# # print("데이터 출력:", result)

# # result = curs.fetchall()
# # print("데이터 출력:", result)

# # result = curs.fetchall()
# # print("데이터 출력:", result)


# # 데이터베이스 연결 종료
# # 데이터베이스의 사용이 끝난 경우, 연결한 데이터베이스를 닫아 주어야 함
# # conn.close()

# # # SQL 문 실행
# # sql = "INSERT INTO Product(PCODE, PNAME, PRICE, AMOUNT) VALUES('P0005','핸드폰','800000,5)"
# # curs.execute(sql)

# # # commit 실행
# # conn.commit()


# # # SQL문실행
# # sql = "UPDATE Product SET price=50000 WHERE pCode='p0003'"
# # curs.execute(sql)

# # SQL 문 실행
# # sql = "DELETE FROM Product WHERE pCode='p0005'"
# # curs.execute(sql)

# # commit 실행
# # conn.commit()

# # conn.close()

# # sql = "SELECT * FROM Product WHERE pCode = %s"
# # curs.execute(sql,('p0002'))

# # result = curs.fetchall()
# # print("데이터 출력:", result)

# # sql = "SELECT * FROM Product Where price between 500000 and 1000000"
# # curs.execute(sql)

# # result = curs.fetchall()
# # print("데이터 출력:", result)

# sql = "SELECT AVG(PRICE), SUM(amount) FROM Product Where price < 100000"
# curs.execute(sql)
# print("데이터 출력:", sql)


import pymysql

conn = pymysql.connect(host='localhost',
                        user = 'root',
                        password = 'root',
                        db = 'FRUITDB',
                        charset= 'utf8')

curs = conn.cursor()

sql = "SELECT * FROM fruitmarket"


# product = [
#       {"pcode":"P0001", "name":'딸기', "price":15000, "quantity":10}
# ]

# fm = {}
# fm['pcode'] = 'P0001'
# fm['name'] = '딸기'
# fm['price'] = 15000
# fm["quantity"] = 10

# product.append(fm)

def allmenu():
    sql = "SELECT * FROM fruitmarket"  
    curs.execute(sql)
    result = curs.fetchall()
    for data in result:
        print(data[0],data[1],data[2],data[3])


def search():
    user_input = input("과일을 입력하세요 : ")
    sql = "SELECT * FROM fruitmarket Where 제품명 = %s" 
    curs.execute(sql,(user_input))
    data = curs.fetchone()
    # print(data[0],data[1],data[2],data[3])
    print(data)
   
def  addmenu():
    code = input("코드를 추가하세요 :")
    product = input("제품을 추가하세요 :")
    price = input("가격을 추가하세요 :")
    quantity = input("수량을 추가하세요 :")
    sql = "Insert into fruitmarket values(%s,%s,%s,%s)"
    curs.execute(sql,(code, product, price, quantity))
    conn.commit()
    print("입력 성공!")
    
    
def updatemenu():
    
    code = input("코드를 수정하세요 :")
    product = input("제품을 수정하세요 :")
    price = input("가격을 수정하세요 :")
    quantity = input("수량을 수정하세요 :")
    sql = "UPDATE fruitmarket SET (%s,%s,%s,%s)"
    curs.execute(sql,(code, product, price, quantity))
    conn.commit()
    print("수정 성공!") 


while True:
    user_input = input("메뉴를 선택하세요 : ")
    if user_input == "1":
        allmenu()
    elif user_input == "2":
         search()
    elif user_input == '3':
         addmenu()
    elif user_input == '4':
        updatemenu()         




        



