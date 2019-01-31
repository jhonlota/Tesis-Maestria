1. Eliminar la carpeta actual
- rm -rf Tesis-Maestria

2. Actualizar carpeta
- git clone https://github.com/jhonlota/Tesis-Maestria.git
- sudo apt-get update
- sudo apt-get install python3-mysql.connector

Otros sin resultado
apt-get install python-mysql.connector
apt-get -f install python-mysql.connector
pip install mysql-connector-python
pip install mysql-connector-python-rf
pip install mysql-connector

3. Tarea programada al iniciar Raspberry
- crontab -e
- @reboot sleep 60; /usr/bin/python3 /home/pi/Documents/Tesis-Maestria/motionsensor.py  > /home/pi/Documents/log.txt # JOB_ID_1

4. Actualizo el repositorio
- git add *
- git commit -m "comentario"
- git push -u origin master

5. Configuro el reloj ntp
- sudo apt-get install ntp
- sudo systemctl stop systemd-timesyncd.service
- sudo systemctl disable systemd-timesyncd.service
- sudo /etc/init.d/ntp stop
- sudo /etc/init.d/ntp start
- sudo nano /etc/ntp.conf
- sudo /etc/init.d/ntp restart
- ntpq -pn

6. Cambiar el nombre del equipo para la RED
- sudo nano /etc/hosts

7. Verificar las redes Wifi
- sudo nano /etc/wpa_supplicant//wpa_supplicant.conf 

  GNU nano 2.7.4 Fichero: /etc/wpa_supplicant//wpa_supplicant.conf              

ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=CO

network={
        ssid="AndroidAPCACA"
        psk="nwyx5998"
        key_mgmt=WPA-PSK
}

network={
        ssid="ELIANA"
        psk="Eliana#@123_Az"
        key_mgmt=WPA-PSK
}

8. Deshabilitar wlan0
@reboot sudo ifdown wlan0




