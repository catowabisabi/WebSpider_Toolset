#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
WebSpider Toolset - Main Entry Point
"""

import logging
from pathlib import Path

from dotenv import load_dotenv
from rich.logging import RichHandler

from utils.config import load_config
from utils.logger import setup_logger

# Setup logging
setup_logger()
logger = logging.getLogger(__name__)

def main():
    """Main entry point for the WebSpider Toolset"""
    try:
        # Load environment variables
        load_dotenv()
        
        # Load configuration
        config = load_config()
        
        logger.info("WebSpider Toolset initialized successfully")
        
        # Your main logic here
        # Example:
        # spider = WebSpider(config)
        # results = spider.run()
        
    except Exception as e:
        logger.error(f"Error in main execution: {e}", exc_info=True)
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 