
import mysql.connector.pooling


config = {
    'host':'localhost',
    'port':3306,
    'user':'root',
    'password':'a123456',
    'database':'vega',
    'auth_plugin':'mysql_native_password'
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(**config,pool_size=10)
except Exception as e:
    print(e)
