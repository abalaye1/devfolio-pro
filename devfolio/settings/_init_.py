# devfolio/settings/__init__.py
import importlib
import os


def get_settings():
    """Dynamically load the appropriate settings module."""
    environment = os.getenv('DJANGO_ENVIRONMENT', 'development')
    module_name = f'devfolio.settings.{environment}'

    return importlib.import_module(module_name)


# Export settings as a module
settings = get_settings()