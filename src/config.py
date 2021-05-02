import pathlib

MODEL_PATH = 'checkpoint/{file_name}.pt'
pathlib.Path(MODEL_PATH.split('/')[0]).mkdir(parents=True, exist_ok=True)
