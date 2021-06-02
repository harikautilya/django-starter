import site

from .config import rel

site.addpackage(rel(), "apps.pth", known_paths=set())