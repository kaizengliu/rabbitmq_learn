# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/10/10 15:27

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

channel.exchange_declare(exchange="topic_logs", type="topic")

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)

print " [x] Sent %r:%r" % (routing_key, message)
connection.close()