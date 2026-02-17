.PHONY: setup install clean

setup:
	python3 -m venv venv
	@echo "Virtual env created. Run 'source venv/bin/activate' to use it."

install:
	pip install --upgrade pip
	pip install -r requirements.txt

up:
	docker-compose up --build

down:
	docker-compose down