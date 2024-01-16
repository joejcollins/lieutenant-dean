"""Print out some stuff from the child settings."""
from flask_app.settings import FLASK_APP

print(FLASK_APP.app_name)
print(FLASK_APP.redis_address)
print(FLASK_APP.log_directory)
