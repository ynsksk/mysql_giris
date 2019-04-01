#veritabanýna baglantý için mysql kütüphanesini tanýtmalýsýnýz
import mysql.connector
veritabaný=mysql.connector.connect(#baðlantý için connetct içinde host,user,passwd kullanýlmalý
    host="localhost",
    user="kullanýcý adýn",
    passwd="kullanýcý þifren"
)