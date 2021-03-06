bind = "0.0.0.0:8000"
workers = 3
daemon = False
loglevel = "debug"
proc_name = "{{ project_name }}"
pidfile = "/tmp/{{ project_name }}.pid"
worker_class = "gevent"
debug = True
django_settings = "{{ project_name }}.settings"

