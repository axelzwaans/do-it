import os
# from vanlife_blog import create_app
from vanlife_blog import app

# app = create_app()

if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )