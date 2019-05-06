import pymysql
import time
import re
from slackclient import SlackClient

slack_client = SlackClient("xoxb-594008988529-601016858577-g2OAoih0OLSbSDaAwBuBpcmk")
slack_client.rtm_connect()

while(1):
    print(slack_client.rtm_read())
    time.sleep(3)

#'channel': 'DHHSYFWH0', 'user': 'UHR7XUKGD', 'type': 'message', 'text': 'Hay',