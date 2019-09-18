import mysql.connector
from mysql.connector import connection, errorcode

def connect(user = 'root', password = '', host='127.0.0.1', database='annuaire'):
    try:
        cnx = connection.MySQLConnection(user = user, password = password,
              host = host, database = database)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Il y a un problème avec votre user name ou password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base n’existe pas")
        else: print(err)
    else:

        cursor = cnx.cursor()

        select_stmt = "SELECT mle, nom, prenom, datnais, ville, sexe FROM employee LIMIT 50"
        cursor.execute(select_stmt)
        result = cursor.fetchall()

        # return une valeur pour la fonction connect, ici une liste du select de la table
        return result

        cnx.close()
