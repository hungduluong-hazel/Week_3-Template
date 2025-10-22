# FastAPI is a Python library that 
# allows us to 
# - take in a request (typically sent from the client)
# - send back a response
from fastapi import FastAPI

# CORS (Cross-Origin Resource Sharing)
# allows us to restrict/enable which
# client urls are allowed to call 
# this backend code. 
# CORS is part of the FastAPI library.
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI application
app = FastAPI(
    title="FastAPI Example",
    description="This is an example of using FastAPI"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # star means all client urls allowed 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# some data
data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 24, "city": "London"},
        {"name": "Charlie", "age": 35, "city": "Paris"}
    ]

@app.get("/")           #endpoint, or route, always starts with a forward slash
def default_route():    #route handler function
    """
    This is the default endpoint for this back-end.
    """
    return "You have reached the default route. Back-end server is listening..."
    
@app.get("/example")  
def get_example():    
    """
    This endpoint returns a JSON object consisting of a simple message.
    """
    return {"message": "Greetings! Brought to you by The Back-End Example Endpoint!"}


# TO RUN:
# 1. Put this code in api/main.py and deploy to Vercel
# 2. Test by using your-vercel-backend-url/docs
# 3. Later call from front-end using JavaScript fetch()