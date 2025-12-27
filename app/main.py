from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Initialize FastAPI app
app = FastAPI(title="Ishtar AI", description="AI Solutions for Finance and Media")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routes
from app.routes import pages

app.include_router(pages.router)

