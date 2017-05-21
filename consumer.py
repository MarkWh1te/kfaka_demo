# -*- coding: utf-8 -*-
from kafka import KafkaConsumer


def show_all_msg():
    consumer = KafkaConsumer(bootstrap_servers='kfk0:11199')
    consumer.subscribe(['test6','test9'])
    for message in consumer:
        if message is not None:
            print(message.offset, message.value)

if __name__ == '__main__':
    show_all_msg()
