# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/10/10 15:01


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

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    print>>sys.stderr, "Usage: %s [info] [warning] [error]" % \
                         (sys.argv[0],)
    sys.exit(-1)


for severity in severities:
    channel.queue_bind(queue=queue_name,
                       exchange="direct_logs",
                       routing_key=severity)

channel.queue_bind(exchange="direct_logs", queue=queue_name)

print ' [*] Waiting for logs. To exit press CTRL+C'


def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()