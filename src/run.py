from endpoints.app import create_app
from endpoints.config import Config

app = create_app(config_object=Config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
