from .home import home_routes
from .generate import generate_routes

def register_routes(app):
    home_routes(app)
    generate_routes(app)
