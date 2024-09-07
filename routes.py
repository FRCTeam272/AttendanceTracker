from fastapi import FastAPI
import server_functions as sf

app = FastAPI()

@app.get("/")
def status():
    return {"Status": "Ok"}

if __name__ == '__main__':
    import uvicorn
    import webbrowser
    webbrowser.open('http://127.0.0.1:8000/docs')
    uvicorn.run(app, host="127.0.0.1", port=8000) # reload is true here for testing, will be solid on deployment