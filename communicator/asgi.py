"""
ASGI config for communicator project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from com_main import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'communicatir.settings')

application = ProtocolTypeRouter({
                                "http": get_asgi_application(),
                                "websocket": AuthMiddlewareStack(
                                    URLRouter(
                                        routing.websocket_urlpatterns
                                        )
                                    ),
                                })
