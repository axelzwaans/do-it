import os
from vanlife_blog import app

"""
Boilerplate code that protects users from
unintentionally invoking the script
"""
if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
