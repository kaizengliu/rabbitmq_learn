# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/10/10 11:20

import pika
import sys

credentials = pika.PlainCredentials('less', 'asdfjkl;')
conn_params = pika.ConnectionParameters(
    host='10.209.68.178',
    port=5672,
    virtual_host='vn1',
    credentials=credentials)


connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = '.'.join(sys.argv[1:]) or "Hello World"
channel.basic_publish(
    exchange="",
    routing_key="task_queue",
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2  # make message durable
    ))


print " [x] Sent %r" % (message,)
connection.close()
