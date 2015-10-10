# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/10/10 14:55


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

channel.exchange_declare(exchange="direct_logs", type="direct")

severity = sys.argv[1] if len(sys.argv) > 1 else "info"
message = ".".join(sys.argv[2:]) or "Hello World!"

channel.basic_publish(exchange="direct_logs",
                      routing_key=severity,
                      body=message)

print " [x] Sent %r:%r" % (severity, message)
connection.close()


