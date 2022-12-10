import os

USER_HOME_DIR = os.path.expanduser("~")

DATABASE_DIR = os.path.join(USER_HOME_DIR, ".config", "PassHub_sync")
DATABASE = os.path.join(DATABASE_DIR, "profiles.json")

os.makedirs(DATABASE_DIR, exist_ok=True)
