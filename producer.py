# -*- coding: utf-8 -*-
from kafka import KafkaProducer

def send_demo_msg(n):
    producer = KafkaProducer(bootstrap_servers='kfk0:11199')
    # for _ in range(n):
    #     # producer.send('test9', b'some_message_bytes {}'.format(_))
    #     producer.send('test9', bytes(a.format(_)))
    #     # producer.send('test9', b'fff {}'.format(_))
    #     print(_)

    a = "fff {}"
    future = producer.send('test9', bytes(a))
    # future = producer.send('test9', b'another_message')
    results = future.get(timeout=50)
    print(results)


if __name__ == '__main__':
    send_demo_msg(10)
