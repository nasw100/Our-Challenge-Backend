import importlib
import os

setting = importlib.import_module(os.getenv("OC_SETTINGS_MODULE", "app.config.dev"))