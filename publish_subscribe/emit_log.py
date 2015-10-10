# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/10/10 14:08

import pika
import sys

credentials = pika.PlainCredentials('less', 'asdfjkl;')
conn_params = pika.ConnectionParameters(
    host='10.209.68.178',
    port=5672,
    virtual_host='vn1',
    credentials=credentials
)

connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.exchange_declare(exchange="logs", type="fanout")


message = ".".join(sys.argv[1:]) or "Hello Word"
channel.basic_publish(exchange="logs", routing_key="", body=message)

print " [x] Sent %r" % (message,)
connection.close()