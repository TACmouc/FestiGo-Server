def home_routes(app):
    @app.route('/')
    def home():
        app.logger.info("Home route accessed.")
        return "Hello, FestiGo Server!"
