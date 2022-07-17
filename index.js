var mqtt = require('mqtt');
var express = require('express');
var app = express();
app.get('/', function (req, res) {
    var topic = req.query.topic;
    var message = req.query.message;
    var url = req.query.url;
    var options = {
        username: req.query.user,
        password: req.query.password
    };
    if (!topic) {
        res.status(500).send('topic not specified<br><br>Use HTTP GET Requests to send MQTT Messages<br><br>Default Host: mqtt://broker.mqttdashboard.com:1883<br><br>Example: https://http-mqtt-dashboard.herokuapp.com/?topic=Testtopic&message=Testmessage<br><br>https://http-mqtt-dashboard.herokuapp.com/?url=mqtt://broker.hivemq.com:1883&user=MyUsername&password=MyPassword&clientid=MyClientID&topic=MyTopic&message=MyMessage');
    }
    else if (!message) {
        res.status(500).send('message not specified');
    }
    else {
    if (!url) {
        url = 'mqtt://broker.mqttdashboard.com:1883';
    }
    if (req.query.clientid) {
        options.clientId = req.query.clientid
    }
    var mqttClient = mqtt.connect(url, options);
    mqttClient.publish(req.query['topic'], req.query['message']);
    res.sendStatus(200);
    }
});
app.listen(5000);
