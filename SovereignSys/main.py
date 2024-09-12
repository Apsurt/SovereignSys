from .app_builder import app
from .country import create_country

@app.get("/")
async def root():
    return