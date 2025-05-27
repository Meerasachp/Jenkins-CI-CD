# __init__.py

# Import core modules from your package
from .models import Task
from .database import db
from .routes import task_routes

# Define package-level variables
__version__ = "1.0.0"
__author__ = "Meerasa"

# Optional: Preload essential configurations
def initialize_app():
    print("TODO App Initialized")

initialize_app()
