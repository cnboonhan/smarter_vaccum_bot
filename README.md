# smarter_vaccum_bot

Augmenting a simple vaccum robot with AI capabilities.

```
conda create -n smarter_vaccum_bot python=3.10
```

## ir_adapter_powerpac
For low level control of robot.

### hardware
```
cd smarter_vaccum_bot/hardware

sudo usermod -aG dialout $USER
mkdir build

arduino-cli config init
arduino-cli config add board_manager.additional_urls http://arduino.esp8266.com/stable/package_esp8266com_index.json 
arduino-cli core install esp8266:esp8266
arduino-cli lib install IRRemote
arduino-cli compile --fqbn esp8266:esp8266:generic --verbose --build-path build  && arduino-cli upload --fqbn esp8266:esp8266:generic -p /dev/ttyUSB0 --input-dir build
```

### ui
```
cd smarter_vaccum_bot/ui

# for development
conda activate smarter_vaccum_bot
pip install -r requirements.txt

# deploy
docker build -t smarter_vaccum_bot_ui .
docker run -p 8000:8000 -e POWERPAC_ADAPTER_CONNECTION_STRING=http://192.168.50.185:80 smarter_vaccum_bot_ui
```

