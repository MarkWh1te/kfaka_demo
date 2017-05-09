# -*- coding: utf-8 -*-
from pykafka import KafkaClient

client = KafkaClient('kfk0:11199')
topic = client.topics['test9']

def send_demo_msg(n):
    with topic.get_producer() as producer:
        counter = 0
        while counter <= n:
            producer.produce('this is message {} from mark'.format(counter), partition_key='{}'.format(counter))
            counter += 1
            # try:
            #     msg, exc = producer.get_delivery_report(block=False)
            #     if exc is not None:
            #         print 'Failed to deliver msg {}: {}'.format(
            #             msg.partition_key, repr(exc))
            #     else:
            #         print 'Successfully delivered msg {}'.format(
            #             msg.partition_key)
            # except Exception as e:
            #     print(e)
            #     break

if __name__ == '__main__':
    send_demo_msg(500)
