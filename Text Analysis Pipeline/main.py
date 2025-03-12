from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import textProcessing

# Create the FastAPI app
app = FastAPI()


origins = ["*"]  # Allow any website to access the API; you can specify specific domains if needed

# Add CORS middleware to handle cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.), adjust based on your needs
    allow_headers=["*"],  # Allow all headers in requests
)


# Include the text processing router
app.include_router(textProcessing.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Text Processing API!"}