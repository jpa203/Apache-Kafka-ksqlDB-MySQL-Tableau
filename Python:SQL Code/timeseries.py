import mysql.connector
import json
from confluent_kafka import Consumer
from time import sleep


conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)

consumer.subscribe(['timeseries'])

#Connect to MySQL database
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='flights')

cursor = cnx.cursor()

# Loop through objects and insert data into PostgreSQL table

i = 0

while True:

    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
        
    msg = json.loads(msg.value().decode('utf-8'))


    cursor.execute(
        "INSERT INTO time_series \
            (land_time, flight_no, country, population) VALUES (%s, %s, %s, %s)", 
                (msg['LANDTIME'], msg['NUMBER'], msg['COUNTRY_NAME'], msg['POPULATION']))                                                                                                                                          

    print(i)
    
    i += 1

    sleep(3)
# Commit changes
    cnx.commit()




