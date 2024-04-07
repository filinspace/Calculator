# Базовый образ для вашего контейнера
FROM zabbix/zabbix-web-nginx-mysql:alpine-6.0-latest

# Опционально: копирование конфигурационных файлов и других настроек
# COPY my_config_file.conf /etc/my_config_file.conf

# Опционально: настройка исходных данных, если необходимо
# ADD my_data_folder /opt/my_data_folder

# Опционально: настройка переменных среды, если необходимо
# ENV MY_VARIABLE=my_value

# Опционально: определение портов для экспонирования
EXPOSE 80

# Опционально: команда по умолчанию для выполнения при запуске контейнера
CMD ["nginx", "-g", "daemon off;"]


