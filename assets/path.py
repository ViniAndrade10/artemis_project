from pathlib import Path
import os

__ROOT_PATH__ = Path(__file__).resolve().parent.parent

database_path = os.path.join(".", "data", "artemis_database.db")
print(database_path)