# http2mqtt
Send MQTT Publish Messages via HTTP GET Requests

Node.js Version:
Start it like this: node index.js

Default Host: mqtt://broker.mqttdashboard.com:1883

Example: https://http-mqtt-dashboard.herokuapp.com/?topic=Testtopic&message=Testmessage

https://zctr7r.sse.codesandbox.io/?url=mqtt://broker.hivemq.com:1883&user=MyUsername&password=MyPassword&clientid=MyClientID&topic=MyTopic&message=MyMessage

Python Version:
Uses Flask and paho. (Install it like this: sudo pip3 install flask or pip install paho-mqtt)
Start it like this: python3 http2mqtt.py

Default Host: broker.mqttdashboard.com Port: 1883

Example: http://127.0.0.1:5000/?topic=MyTopic&message=MyMessage&host=broker.mqttdashboard.com&port=1883
