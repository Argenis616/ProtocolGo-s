
import mysql.connector
from mysql.connector import Error
from model.poke_api import show_name
def connec():
    """
    Function that establishes a connection to the database
    """
    try:
        connection = mysql.connector.connect(host='localhost', database='pokemon', user='trainer', password='Trainer1*')
        return connection;
    except Error as e:
        print("Error while connecting to MySQL", e)

def get_trainers():
    """
    We can get all trainers
    """
    try:
        connection = connec()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT idTrainer,name FROM pokemon.Trainer;")
            s = ""
            trainers = cursor.fetchall()
            s += "0: Cerrar Conexion" + "\n"
            for t in trainers:
                s += str(t[0]) + ": " + str(t[1]) + "\n"
            return s
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def get_pokedex(id_trainer):
    """
    We get the Pokedex
    Args:
        id_trainer: We pass the trainer's identification as a parameter.
    """
    try:
        connection = connec()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT idPokemon FROM pokemon.Pokedex WHERE idTrainer = "+id_trainer+";")
            s = ""
            trainers = cursor.fetchall()
            for t in trainers:
                s += show_name((t[0])) +"\n"
            return s
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()

def set_pokedex(id_pokemon,id_trainer):
    """
    You can add a new pokemon to the pokedex
    Args:
        id_pokemon: We pass the pokemon's identification as a parameter.
        id_trainer: We pass the trainer's identification as a parameter.
    """
    try:
        connection = connec()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("INSERT INTO pokemon.Pokedex(idPokemon,idTrainer) VALUES(%s,%s);", (id_pokemon,id_trainer))
            print(id_pokemon + id_trainer)
        connection.commit()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
def get_name_trainer(id_trainer):
    """
    You get the trainer's name
    Args: We pass the trainer's identification as a parameter.
    """
    try:
        connection = connec()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT idTrainer,name FROM pokemon.Trainer WHERE idTrainer = "+id_trainer +";")
            s = ""
            trainers = cursor.fetchall()
            for t in trainers:
                s += str(t[1]) + "\n"
            return s
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
