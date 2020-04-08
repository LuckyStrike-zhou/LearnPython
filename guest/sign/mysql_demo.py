from pymysql import cursors, connect

# 连接数据库
conn = connect(host='127.0.0.1',
               user='root',
               password='dance2587',
               db='guest',
               charset='utf8mb4',
               cursorclass=cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        # 创建嘉宾数据
        sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id,' \
              'create_time) VALUES' \
              '("alice", 18808110002,"alice@mail.com",0,1,NOW());'
        cursor.execute(sql)

        # 创建嘉宾数据
        sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id,' \
              'create_time) VALUES' \
              '("Jerry", 18803729002,"Jerry@mail.com",0,2,NOW());'
        cursor.execute(sql)

        # 创建嘉宾数据
        sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id,' \
              'create_time) VALUES' \
              '("Bob", 18800119372,"bob@mail.com",0,3,NOW());'
        cursor.execute(sql)

        # 提交事物
        conn.commit()

    with conn.cursor() as cursor:
        # 查询添加的嘉宾
        sql = "SELECT realname,phone,email,sign From sign_guest WHERE phone =%s"
        cursor.execute(sql, ('18800110002',))
        result = cursor.fetchone()
        print(result)
finally:
    conn.close()
