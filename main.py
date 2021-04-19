from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    app.testing = True
    app.base_url = os.path.abspath(os.path.dirname(__file__))
    app.run(debug=False)
