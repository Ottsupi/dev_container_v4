import os

# Google Cloud Run default port is 8080
PORT = os.environ.get("PORT", default="8080")
HOST = "0.0.0.0"
bind = f"{HOST}:{PORT}"

workers = 1
threads = 1
timeout = 0