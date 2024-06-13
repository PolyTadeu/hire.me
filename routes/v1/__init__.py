from routes.v1 import shorten_url

# App Initial Configuration
def init_app(app):
    # Add Routes in the app
    app.include_router(shorten_url.router)
