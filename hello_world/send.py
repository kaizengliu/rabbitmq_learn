# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/10/09 19:06

import pika

credentials = pika.PlainCredentials('less', 'asdfjkl;')
conn_params = pika.ConnectionParameters(
    host='10.209.68.178',
    port=5672,
    virtual_host='vn1',
    credentials=credentials
)


connection = pika.BlockingConnection(conn_params)

channel = connection.channel()

channel.queue_declare(queue='hello')

# In RabbitMQ a message can never be sent directly to the queue,
# it always needs to go through an exchange.

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"

# Before exiting the program we need to make sure the network
# buffers were flushed and our message was actually delivered
# to RabbitMQ. We can do it by gently closing the connection.
connection.close()