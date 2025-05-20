import yaml

DEFAULT_PATH="config/default.yaml"

def _merge_configs(cfg: dict, defaults:dict):
    for k in defaults:
        if k in cfg:
            if isinstance(cfg[k], dict) and isinstance(defaults[k], dict):
                _merge_configs(cfg[k], defaults[k])
        else:
            cfg[k] = defaults[k]

def load_config(path: str="") -> dict:
    cfg = {}
    if path:
        with open(path) as f:
            cfg = yaml.load(f, Loader=yaml.FullLoader)
    with open(DEFAULT_PATH) as f:
        defaults = yaml.load(f, Loader=yaml.FullLoader)
    _merge_configs(cfg, defaults)
    return cfg

