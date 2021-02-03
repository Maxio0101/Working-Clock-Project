# Working-Clock-Project
Using simple devices to record employees working hours for office management<br>
When a RFID key is scanned, the LED flashes.<br>
If the RFID key is Authorizated, and the timestamp is record into the remote database server, there will be a sound "Bi~" to confirm this action.<br>
Hardware: Raspberry Pi 3b+, MRFC522, LED, Buzzer<br>
Software: Python3, MySQL 8.0<br>

## Requirements
*Install SPI-Py  https://github.com/lthiery/SPI-Py<br>
*Download MRFC522 python library git clone https://github.com/mxgxw/MFRC522-python.git<br>

## Pins setting

|   Pi PIN NUM  |  PIN Name     |  
| ------------- | ------------- |
|       24      |  MRFC522_SDA  | 
|       23      |  MRFC522_SCK  | 
|       19      |  MRFC522_MOSI | 
|       21      |  MRFC522_MISO | 
|       20      |  MRFC522_GND  | 
|       22      |  MRFC522_RST  | 
|       17      |  MRFC522_3.3V | 
|        9      |  LED -        |
|       11      |  LED +        | 
|        7      |  Buzzer_S     | 
|        6      |  Buzzer_GND   | 
|        4      |  Buzzer_5V    | 

