<?php
require('phpMQTT.php');

// Beispiel GET-Request: http://localhost/mqtt-publish-get.php?url=mqtt://broker.hivemq.com:1883&user=&password=&clientid=MyClientID&topic=test/topic&message=HelloWorld

// Parameter aus dem GET-Request lesen
$url       = $_GET['url']       ?? 'mqtt://broker.hivemq.com:1883';
$user      = $_GET['user']      ?? '';
$password  = $_GET['password']  ?? '';
$client_id = $_GET['clientid']  ?? 'phpMQTT-publisher';
$topic     = $_GET['topic']     ?? '';
$message   = $_GET['message']   ?? '';

// URL aufteilen in Host und Port
if (!preg_match('/^mqtt:\/\/([^:]+):(\d+)$/', $url, $matches)) {
    die("Ungültiges URL-Format. Erwartet: mqtt://host:port\n");
}
$host = $matches[1];
$port = (int)$matches[2];

// Verbindung zum MQTT-Broker herstellen
$mqtt = new Bluerhinos\phpMQTT($host, $port, $client_id);

if ($mqtt->connect(true, NULL, $user, $password)) {
    $mqtt->publish($topic, $message, 0);
    $mqtt->close();
    echo "Nachricht erfolgreich gesendet an $topic\n";
} else {
    echo "Verbindung zum MQTT-Broker fehlgeschlagen.\n";
}
