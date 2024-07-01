# iot-socket-security

Para executar o envio por MQTT deve-se seguir os seguintes passos:

Não é necessário criar novas chaves públicas e privadas, elas já estão nas suas pastas

Ter o Python 3.12 instalado
Instalar as dependências do projeto:
executar o pip install para todos estes módulos:

a. pycryptodome
b. faker
c. paho-mqtt

1. Baixar o mosquitto para que seja executável pela linha de comando
2. Executar o seguinte comando no terminal: mosquitto -v
3. A partir da pasta raiz em um terminal, executar os seguintes comandos para iniciar o subscriber:
   cd AES/MQTT
   py main.py
4. Abrir um novo terminal a partir da pasta raiz
5. Executar os comandos neste novo terminal:
   cd AES/raspberryPi
   py publisher.py
