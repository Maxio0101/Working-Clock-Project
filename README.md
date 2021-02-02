# Working-Clock-Project
A simple Prroject to record employer working hours for office management with Raspberry Pi 3b+, MRFC522, and MySQL
HradWare: aspberry Pi 3b+, MRFC522, LED, Buzzer
Software: Python3, MySQL 8.0

# Requirements
Install SPI-Py from https://github.com/lthiery/SPI-Py
Download MRFC522 python library git clone https://github.com/mxgxw/MFRC522-python.git

# Pins setting

|   Pi PIN NUM  | Second Header |  
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

