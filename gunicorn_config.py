# Gunicorn configuration for production
bind = "127.0.0.1:8000"
workers = 3
worker_class = "sync"
worker_connections = 1000
timeout = 120
keepalive = 5

# Logging
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "info"

# Process naming
proc_name = "checklist_app"

# Server mechanics
daemon = False
pidfile = "/var/run/gunicorn.pid"
user = None
group = None
tmp_upload_dir = None

# SSL (handled by Nginx)
# Gunicorn runs behind Nginx reverse proxy
