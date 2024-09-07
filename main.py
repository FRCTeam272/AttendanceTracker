from routes import app
from server_functions import sf

def main():
    try:    
        app.run(debug=True)
        pass
    except Exception as e:
        sf.session.close()
        raise e

if __name__ == "__main__":
    main()