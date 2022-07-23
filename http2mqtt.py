#!/usr/local/bin/python3
import paho.mqtt.publish as publish
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_id():
  if request.args.get('topic') == None or request.args.get('topic') == '':
    return 'topic not specified<br><br>Send MQTT Publish Messages via HTTP GET Requests<br><br>Default Host: broker.mqttdashboard.com Port: 1883<br><br>Example: http://127.0.0.1:5000/?topic=MyTopic&message=MyMessage&host=broker.mqttdashboard.com&port=1883'
  else:
    topic = request.args.get('topic')
  if request.args.get('message') == None or request.args.get('message') == '':
    return 'message not specified<br><br>Send MQTT Publish Messages via HTTP GET Requests<br><br>Default Host: broker.mqttdashboard.com Port: 1883<br><br>Example: http://127.0.0.1:5000/?topic=MyTopic&message=MyMessage&host=broker.mqttdashboard.com&port=1883'
  else:
    message = request.args.get('message')
  if request.args.get('host') == None or request.args.get('host') == '':
    host = 'broker.mqttdashboard.com'
  else:
    host = request.args.get('host')
  if request.args.get('port') == None or request.args.get('port') == '' or request.args.get('port') == "0":
    port = 1883
  else:
    port = request.args.get('port')
    port = int(port)
  publish.single(topic, message, hostname=host, port=port)
  return 'send:<br>Topic: ' + topic + '<br> Message: ' + message + '<br>Host: ' + host + '<br>Port: ' + str(port)

if __name__ == '__main__':
  app.run()
