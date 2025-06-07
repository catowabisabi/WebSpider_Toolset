"""
Configuration utilities for WebSpider Toolset.
"""

import os
from pathlib import Path
from typing import Dict, Any

import yaml
from dotenv import load_dotenv

def load_config(config_path: str = None) -> Dict[str, Any]:
    """
    Load configuration from YAML file and environment variables.
    
    Args:
        config_path (str, optional): Path to config YAML file. Defaults to None.
        
    Returns:
        Dict[str, Any]: Configuration dictionary
    """
    config = {
        'user_agent': os.getenv('USER_AGENT', 'WebSpider-Toolset/1.0'),
        'request_timeout': int(os.getenv('REQUEST_TIMEOUT', '30')),
        'retry_count': int(os.getenv('RETRY_COUNT', '3')),
        'proxy': os.getenv('PROXY_URL'),
        'api_key': os.getenv('API_KEY'),
    }
    
    if config_path and Path(config_path).exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            yaml_config = yaml.safe_load(f)
            if yaml_config:
                config.update(yaml_config)
    
    return config 