.PHONY: all prepare-env create_db clean run_pokemon_client run_pokemon_server

UNAME_S=$(shell uname -s)

all:
	@echo "make prepare-env"
	@echo "    Preparando el entorno."
	@echo "    Se necesita ejecutar con sudo para instalar el manejador de paquetes de Python3."
	@echo "make create_db"
	@echo "    Aclaracion este comando solo pobla la base de datos. por favor seguir indicaciones del archivo instalacion.txt"
	@echo "    Precaucion debe de ser cambiado el Makefile ya que debe introducir su propia contraseña de mysql."
	@echo "make clean"
	@echo "    Limpia el proyecto de archivos pycahce"
	@echo "make run_client"
	@echo "    Ejecuta el cliente."
	@echo "make run_server"
	@echo "    Ejecuta el servidor."
	@echo "    en el comando se llena en una base de datos previamente creada con create database pokemon; en MYSQL "
	@echo "    IMPORTANTE EN CASO DE NO CORRER EL SCRIPT HACERLO MANUALMENTE de MYSQL"

prepare-env:
	@if [ $(UNAME_S) = "Darwin" ]; then \
		install pip3; \
		echo OK; \
	else \
		apt-get install python3-pip; \
		echo OK; \
	fi
	@pip3 install -r requirements.txt
create_db:
	@if [ ! -d "/base" ]; then \
		cd base && mysql --user=trainer --password=Trainer1* pokemon < base_dump.SQL; \
		echo "La base de datos fue inicializada"; \
	fi
	@echo OK;
clean:
	@rm -rf src/model/__pycache__ 2> /dev/null || true
	@rm src/*.png 2> /dev/null || true
	@rm -rf src/Pokedex 2> /dev/null || true

run_client:
	@cd src && python3 client.py

run_server:
	@cd src && python3 server.py
