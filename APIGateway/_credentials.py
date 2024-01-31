import os


def _load_credential_from_file(filepath):
    real_path = os.path.join(os.path.dirname(__file__), filepath)
    with open(real_path, "rb") as f:
        return f.read()


SERVER_CERTIFICATE = _load_credential_from_file("credentials/docker_host.crt")
SERVER_CERTIFICATE_KEY = _load_credential_from_file("credentials/docker_host.key")
ROOT_CERTIFICATE = _load_credential_from_file("credentials/root.crt")
