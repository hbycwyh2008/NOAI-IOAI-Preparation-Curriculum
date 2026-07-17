import os


def get_api_key(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing environment variable: {name}")
    return value


# TODO: use the current official SDK/API documentation.
# Never commit secret keys.
