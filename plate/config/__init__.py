"""
 Configuration module for the system
"""
import os
from django.core.exceptions import ImproperlyConfigured


def rel(*path):
    """
    Converts path relative to the project root into an absolute path
    :rtype: str
    """
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.path.pardir, *path)
    ).replace("\\", "/")


# speculation looking for the env files maybe
def get_env_setting(setting, default=None):
    """
    Get the environment setting or raise exception
    :rtype: str
    """

    try:
        return os.environ[setting]
    except KeyError as key_error:
        if default is not None:
            return default
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg) from key_error