# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/10/09 19:06

import pika

credentials = pika.PlainCredentials('less', 'asdfjkl;')
connection_params = pika.ConnectionParameters(
    host='10.209.68.178',
    port=5672,
    virtual_host='vn1',
    credentials=credentials
)

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()