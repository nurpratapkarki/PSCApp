"""generated with djinit"""

import os
import environ
from django.core.asgi import get_asgi_application

env = environ.Env()
environ.Env.read_env()

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    env("DJANGO_SETTINGS_MODULE", default="core.settings.production"),
)
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import src.routing

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(URLRouter(src.routing.websocket_urlpatterns)),
    }
)
