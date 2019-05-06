import pymysql
import time
from slackclient import SlackClient

slack_client = SlackClient("xoxb-594008988529-601016858577-g2OAoih0OLSbSDaAwBuBpcmk")

sql = "SELECT COUNT(*) FROM tb_outbox WHERE flag=0"
query = "SELECT * FROM tb_outbox WHERE flag=0"

while(1):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_bot1020')
    cur = conn.cursor()

    cur.execute(sql)
    flag = cur.fetchone()
    if flag[0] > 0:
        cur.execute(query)
        data = cur.fetchone()
        slack_client.api_call(
                "chat.postMessage",
                channel=data[1],
                text=data[2]
            )
        cur.execute("UPDATE tb_outbox SET flag=1 WHERE id=%s", data[0])
        conn.commit()
        print("dataterhasil dikirim")
        print(flag)
    else:
        print("tidak ada data yg dikirim")
        print(flag)
    time.sleep(1)
    conn.close()