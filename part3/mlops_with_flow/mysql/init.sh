#!/bin/bash
set -e

mysql -uroot -p"$MYSQL_ROOT_PASSWORD" <<EOF
CREATE DATABASE IF NOT EXISTS airflow;
CREATE DATABASE IF NOT EXISTS mlflow;

CREATE USER IF NOT EXISTS 'airflow'@'%' IDENTIFIED BY 'airflow';

GRANT ALL PRIVILEGES ON airflow.* TO 'airflow'@'%';
GRANT ALL PRIVILEGES ON mlflow.* TO 'airflow'@'%';

FLUSH PRIVILEGES;
EOF
