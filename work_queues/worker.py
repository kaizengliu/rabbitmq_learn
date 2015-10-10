# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/10/10 11:26

import pika
import time

credentials = pika.PlainCredentials('less', 'asdfjkl;')
conn_params = pika.ConnectionParameters(
    host='10.209.68.178',
    port=5672,
    virtual_host='vn1',
    credentials=credentials)


connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

print ' [*] Waiting for messages. To exit press CTRL+C'


def callback(ch, method, properties, body):
    print "[x] Received %r" % (body,)
    time.sleep(body.count("."))
    print "[x] Done"
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue="task_queue")
channel.start_consuming()