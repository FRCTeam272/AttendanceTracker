from routes import app
import uvicorn
import server_functions as sf
from flasgger import Swagger

import routes_adds
import routes_gets

def main():
    try:    
        # uvicorn.run(app, host="127.0.0.1", port=5000)
        pass
    except Exception as e:
        print("closing database session")
        sf.session.close()
        raise e

if __name__ == "__main__":
    main()