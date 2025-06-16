# Crear entorno virtual
venv:
	python3 -m venv venv

# Mensaje para activar entorno
activate:
	@echo "Para activar manualmente ejecuta: source venv/bin/activate"

# Instalar dependencias desde requirements.txt
install:
	source venv/bin/activate && pip install -r requirements.txt

# Levantar servidor de desarrollo
dev:
	source venv/bin/activate && uvicorn main:app --reload

# Generar requirements.txt actual
freeze:
	pip freeze > requirements.txt


setup-env:
	cp .env.example .env
	echo "Archivo .env generado. Completa los valores necesarios."	