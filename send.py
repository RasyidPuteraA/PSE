#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

data_Stream = "Sensor LM35"

channel.basic_publish(exchange='', routing_key='hello', body=data_Stream)
print(" [x] Sent {data_Stream}")
connection.close()