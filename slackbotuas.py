import pymysql
import time
from slackclient import SlackClient

slack_client = SlackClient("xoxb-594008988529-601016858577-g2OAoih0OLSbSDaAwBuBpcmk")

RTM_READ_DELAY = 1

def parse_bot_commands(slack_events):
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            message = event["text"]
            channel = event["channel"]
            # user = event["user"]
            insert = """INSERT INTO tb_inbox(id_chat, message, tanggal) VALUES(%s, %s, NOW())"""
            cur.execute(insert, (channel, message))
            conn.commit()

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            conn = pymysql.connect(host='localhost', user='root', passwd='', db='db_bot1020')
            cur = conn.cursor()
            parse_bot_commands(slack_client.rtm_read())
            conn.close()
            time.sleep(1)
    else:
        print("Connection failed. Exception traceback printed above.")