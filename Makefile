.PHONY: setup install up down help

# Default target: display available commands
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  setup     Create a Python virtual environment"
	@echo "  install   Upgrade pip and install project dependencies"
	@echo "  up        Build and start the data platform using Docker Compose"
	@echo "  down      Stop and remove the Docker containers"

# Initialize the Python virtual environment
setup:
	python3 -m venv venv
	@echo "Virtual environment created. Run 'source venv/bin/activate' to activate it."

# Install required Python packages
install:
	pip install --upgrade pip
	pip install -r requirements.txt

# Build and launch the platform in a containerized environment
up:
	docker-compose up --build

# Shutdown the platform and clean up resources
down:
	docker-compose down