// Provide a REST API for controlling a PowerPac robot uver Ij

#include <Arduino.h>
#include "PinDefinitionsAndMore.h" // Define macros for input and output pin etc.
#include <IRremote.hpp>
#include <ESP8266WiFi.h>

#ifndef STASSID
#define STASSID "ASUS_68_2G"
#define STAPSK  "trishaw1"
#endif
// Static IP
IPAddress local_IP(192, 168, 50, 185);
IPAddress gateway(192, 168, 50, 1);
IPAddress subnet(255, 255, 255, 0);
IPAddress primaryDNS(8, 8, 8, 8);   //optional
IPAddress secondaryDNS(8, 8, 4, 4); //optional

const char* ssid = STASSID;
const char* password = STAPSK;

WiFiServer server(80);

#define REPEAT_NUM  1
uint16_t powerPacUpRawData[17] = {3080,970, 730,1470, 1530,670, 730,1470, 730,1470, 730,1470, 730,1470, 730,1470, 1530};
uint16_t powerPacDownRawData[17] = {3030,1020, 680,1470, 1530,720, 680,1470, 730,1470, 730,1470, 730,1470, 1530,670, 1530};
uint16_t powerPacLeftRawData[17] = {3080,920, 730,1520, 1530,670, 680,1520, 680,1520, 680,1470, 1580,670, 680,1470, 1580};
uint16_t powerPacRightRawData[17] = {3080,970, 730,1470, 1530,670, 730,1470, 730,1470, 730,1470, 1530,670, 1530,670, 1530};
uint16_t powerPacCenterRawData[17] = {3030,1020, 680,1520, 1530,670, 1530,670, 1480,720, 680,1520, 1480,720, 680,1520, 1480};
uint16_t powerPacReturnRawData[17] = {3080,970, 680,1520, 1530,670, 680,1520, 1480,720, 680,1520, 680,1470, 1530,670, 1530};
uint16_t powerPacEdgeRawData[17] = {3080,970, 680,1470, 1530,670, 730,1470, 730,1470, 1530,670, 1530,670, 730,1470, 1530};
uint16_t powerPacAutoRawData[17] = {3030,970, 730,1470, 1530,670, 730,1470, 730,1470, 1530,670, 730,1470, 1530,670, 730};

const char* remoteUpReturnString = "Remote Button UP Pressed";
const char* remoteDownReturnString = "Remote Button DOWN Pressed";
const char* remoteLeftReturnString = "Remote Button LEFT Pressed";
const char* remoteRightReturnString = "Remote Button RIGHT Pressed";
const char* remoteCenterReturnString = "Remote Button CENTER Pressed";
const char* remoteReturnReturnString = "Remote Button RETURN Pressed";
const char* remoteEdgeReturnString = "Remote Button EDGE Pressed";
const char* remoteAutoReturnString = "Remote Button AUTO Pressed";

unsigned char rc6Toggle = 0;

void setup()
{
    pinMode(LED_BUILTIN, OUTPUT);
    pinMode(APPLICATION_PIN, INPUT_PULLUP);
    Serial.begin(115200);

    Serial.println(F("START " __FILE__ " from " __DATE__ "\r\nUsing library version " VERSION_IRREMOTE));

    IrSender.begin(); 
    // Start with IR_SEND_PIN as send pin and if NO_LED_FEEDBACK_CODE is NOT defined, enable feedback LED at default feedback LED pin
    Serial.print(F("Ready to send IR signals at pin ")); Serial.println(IR_SEND_PIN);

    Serial.println(); Serial.print(F("Connecting to ")); Serial.println(ssid);
    if (!WiFi.config(local_IP, gateway, subnet, primaryDNS, secondaryDNS)) {
        Serial.println("STA Failed to configure");
    }
    
    // Connect to Wi-Fi network with SSID and password
    Serial.print("Connecting to ");
    Serial.println(ssid);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
      Serial.print(".");
    }
    // Print local IP address and start web server
    Serial.println("");
    Serial.println("WiFi connected.");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());

    server.begin(); Serial.println(F("Server started"));
}

void generateClientResponse(WiFiClient *client, const char *string) {
    client->print(F("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<!DOCTYPE HTML>\r\n<html>\r\n"));
    client->print(string);
    client->print("\r\n");
    client->print(F("</html>"));
}

void loop()
{
    WiFiClient client = server.available();

    if (client) {
        client.setTimeout(5000); 

        String req = client.readStringUntil('\r');
        Serial.println(F("Received Request: ")); Serial.println(req);
        // Match the request
        if (req.indexOf(F("/remote/up")) != -1){
            Serial.println(remoteUpReturnString); 
            generateClientResponse(&client, remoteUpReturnString);
            IrSender.sendRaw(powerPacUpRawData, sizeof(powerPacUpRawData) / sizeof(powerPacUpRawData[0]), NEC_KHZ);
            rc6Toggle = rc6Toggle?0:1;
        }
        else
            if (req.indexOf(F("/remote/down")) != -1){
                IrSender.sendRaw(powerPacDownRawData, sizeof(powerPacDownRawData) / sizeof(powerPacDownRawData[0]), NEC_KHZ);
                Serial.println(remoteDownReturnString); 
                generateClientResponse(&client, remoteDownReturnString);
                rc6Toggle = rc6Toggle?0:1;
            }
        else
            if (req.indexOf(F("/remote/left")) != -1){
                IrSender.sendRaw(powerPacLeftRawData, sizeof(powerPacLeftRawData) / sizeof(powerPacLeftRawData[0]), NEC_KHZ);
                Serial.println(remoteLeftReturnString); 
                generateClientResponse(&client, remoteLeftReturnString);
                rc6Toggle = rc6Toggle?0:1;
            }
        else
            if (req.indexOf(F("/remote/right")) != -1){
                IrSender.sendRaw(powerPacRightRawData, sizeof(powerPacRightRawData) / sizeof(powerPacRightRawData[0]), NEC_KHZ);
                Serial.println(remoteRightReturnString); 
                generateClientResponse(&client, remoteRightReturnString);
                rc6Toggle = rc6Toggle?0:1;
            }
        else
            if (req.indexOf(F("/remote/center")) != -1){
                IrSender.sendRaw(powerPacCenterRawData, sizeof(powerPacCenterRawData) / sizeof(powerPacCenterRawData[0]), NEC_KHZ);
                Serial.println(remoteCenterReturnString); 
                generateClientResponse(&client, remoteCenterReturnString);
                rc6Toggle = rc6Toggle?0:1;
            }
        else
            if (req.indexOf(F("/remote/return")) != -1){
                IrSender.sendRaw(powerPacReturnRawData, sizeof(powerPacReturnRawData) / sizeof(powerPacReturnRawData[0]), NEC_KHZ);
                Serial.println(remoteReturnReturnString); 
                generateClientResponse(&client, remoteReturnReturnString);
                rc6Toggle = rc6Toggle?0:1;
            }
        else
            if (req.indexOf(F("/remote/edge")) != -1){
                IrSender.sendRaw(powerPacEdgeRawData, sizeof(powerPacEdgeRawData) / sizeof(powerPacEdgeRawData[0]), NEC_KHZ);
                Serial.println(remoteEdgeReturnString); 
                generateClientResponse(&client, remoteEdgeReturnString);
                rc6Toggle = rc6Toggle?0:1;
            }
        else
            if (req.indexOf(F("/remote/auto")) != -1){
                IrSender.sendRaw(powerPacAutoRawData, sizeof(powerPacAutoRawData) / sizeof(powerPacAutoRawData[0]), NEC_KHZ);
                Serial.println(remoteAutoReturnString); 
                generateClientResponse(&client, remoteAutoReturnString);
                rc6Toggle = rc6Toggle?0:1;
            }
        else
            generateClientResponse(&client, WiFi.localIP().toString().c_str());

        // read/ignore the rest of the request
        // do not client.flush(): it is for output only, see below
        while (client.available()) {
            // byte by byte is not very efficient
            client.read();
        }
    } else {
        Serial.println(WiFi.localIP());
        delay(1500);
    }

    delay(50);
}
