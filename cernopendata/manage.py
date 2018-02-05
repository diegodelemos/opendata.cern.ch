from __future__ import absolute_import, print_function

from flask_script import Manager
from flask_sitemap.script import Sitemap

from .factory import create_app

app = create_app()
import wdb; wdb.set_trace()
sitemap_ext = Sitemap(app)
# configure your app

manager = Manager(sitemap_ext)
manager.add_command('sitemap', Sitemap())

if __name__ == "__main__":
    manager.run()
