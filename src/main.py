import uvicorn
from endpoints.app import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
