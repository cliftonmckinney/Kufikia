from fabric.operations import put


REMOTE_PROJECT_DIR = '/home/web/kufikia.com'


def upload():
    """Uploads the site content to the remote project directory."""
    put(local_path="Public/*", remote_path=REMOTE_PROJECT_DIR)


def deploy():
    """Deploy the site."""
    upload()
