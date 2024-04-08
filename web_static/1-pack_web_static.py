#!/usr/bin/env python3

from fabric import task
from datetime import datetime

@task
def do_pack(c):
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(now)
        c.local("mkdir -p versions")
        c.local("tar -cvzf {} web_static".format(archive_path))
        print("web_static packed: {} -> {}".format(archive_path, archive_path))
        return archive_path
    except Exception as e:
        return None

