"""
Logging configuration for WebSpider Toolset.
"""

import logging
import sys
from pathlib import Path

from rich.logging import RichHandler

def setup_logger(
    log_file: str = None,
    level: int = logging.INFO,
    rich_handler: bool = True
) -> None:
    """
    Setup logging configuration.
    
    Args:
        log_file (str, optional): Path to log file. Defaults to None.
        level (int, optional): Logging level. Defaults to logging.INFO.
        rich_handler (bool, optional): Use Rich handler for console. Defaults to True.
    """
    # Create logs directory if logging to file
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Basic configuration
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            RichHandler(rich_tracebacks=True) if rich_handler else logging.StreamHandler(sys.stdout)
        ] + ([logging.FileHandler(log_file)] if log_file else [])
    )
    
    # Suppress unnecessary logging
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("selenium").setLevel(logging.WARNING) 