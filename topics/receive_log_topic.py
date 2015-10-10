# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/10/10 15:29

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

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue


binding_keys = sys.argv[1:]
if not binding_keys:
    print >> sys.stderr, "Usage: %s [binding_key]..." % (sys.argv[0],)
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)

print ' [*] Waiting for logs. To exit press CTRL+C'


def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()