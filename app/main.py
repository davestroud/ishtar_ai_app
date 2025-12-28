from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.middleware import SecurityHeadersMiddleware

# Initialize FastAPI app
app = FastAPI(title="Ishtar AI", description="AI Solutions for Finance and Media")

# Add security headers middleware
app.add_middleware(SecurityHeadersMiddleware)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Include routes
from app.routes import pages, seo

app.include_router(pages.router)
app.include_router(seo.router)


# Error handlers
@app.exception_handler(404)
async def not_found_handler(request: Request, exc: StarletteHTTPException):
    return templates.TemplateResponse(
        "404.html",
        {"request": request, "config": None},
        status_code=status.HTTP_404_NOT_FOUND,
    )


@app.exception_handler(500)
async def server_error_handler(request: Request, exc: Exception):
    import traceback

    print(f"Internal server error: {exc}")
    traceback.print_exc()
    return templates.TemplateResponse(
        "500.html",
        {"request": request, "config": None},
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """Handle HTTP exceptions (excluding 404 which is handled by not_found_handler)"""
    return templates.TemplateResponse(
        "500.html", {"request": request, "config": None}, status_code=exc.status_code
    )
