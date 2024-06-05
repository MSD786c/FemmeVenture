"""
ASGI config for femme_venture project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'femme_venture.settings')
django_asgi_app = get_asgi_application()

# Now import other components that require Django to be setup
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

# Define the application protocol type router
application = ProtocolTypeRouter({
    'http': django_asgi_app,  # Django's ASGI application to handle traditional HTTP requests
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns  # Handling WebSocket connections
        )
    )
})
