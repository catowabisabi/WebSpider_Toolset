![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![GitHub Stars](https://img.shields.io/badge/stars-0-gray)

# 🤖 WebSpider Toolset / 網路爬蟲工具集

[English](#english) | [中文](#中文)

<a name="english"></a>
## 📖 Introduction
WebSpider Toolset is a comprehensive Python-based web scraping and automation framework that provides efficient and reliable tools for data collection, processing, and analysis.

## 🎯 Purpose
- Build a modular and maintainable web scraping system
- Provide reusable components for common scraping tasks
- Ensure robust error handling and rate limiting
- Support multiple data sources and export formats

## ✨ Features
- 🚀 Modular architecture for easy extension
- 🛡️ Built-in rate limiting and proxy support
- 📊 Data processing and export utilities
- 🔄 Automatic retry mechanism
- 📝 Comprehensive logging system

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/WebSpider_Toolset.git
cd WebSpider_Toolset
```

2. Set up the environment:
```bash
# Using pip
pip install -r requirements.txt

# Or using conda
conda env create -f environment.yml
conda activate webspider
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

## 🚀 Usage

Basic usage example:
```python
from services.spider import WebSpider
from utils.config import load_config

# Initialize spider with configuration
config = load_config()
spider = WebSpider(config)

# Start scraping
data = spider.scrape("https://example.com")
```

## 📂 Module Breakdown

- `endpoints/`: API endpoints and webhook handlers
- `services/`: Core scraping and processing logic
- `utils/`: Utility functions and helpers
- `tests/`: Unit and integration tests
- `docs/`: Documentation and resources

## 🖼️ Architecture
![Architecture](docs/architecture.png)

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contribution
Contributions are welcome! Please feel free to submit a Pull Request.

---

<a name="中文"></a>
## 📖 簡介
WebSpider Toolset 是一個全面的 Python 網路爬蟲和自動化框架，提供高效且可靠的數據採集、處理和分析工具。

## 🎯 用途
- 建立模組化且易於維護的網路爬蟲系統
- 提供可重用的常見爬蟲任務元件
- 確保強大的錯誤處理和速率限制
- 支援多種數據來源和導出格式

## ✨ 主要功能
- 🚀 模組化架構，易於擴展
- 🛡️ 內建速率限制和代理支援
- 📊 數據處理和導出工具
- 🔄 自動重試機制
- 📝 完整的日誌系統

## ⚙️ 安裝方式

1. 克隆專案：
```bash
git clone https://github.com/yourusername/WebSpider_Toolset.git
cd WebSpider_Toolset
```

2. 設置環境：
```bash
# 使用 pip
pip install -r requirements.txt

# 或使用 conda
conda env create -f environment.yml
conda activate webspider
```

3. 配置環境變數：
```bash
cp .env.example .env
# 編輯 .env 填入您的憑證
```

## 🚀 使用方法

基本使用範例：
```python
from services.spider import WebSpider
from utils.config import load_config

# 初始化爬蟲與配置
config = load_config()
spider = WebSpider(config)

# 開始爬取
data = spider.scrape("https://example.com")
```

## 📂 模組說明

- `endpoints/`: API 端點和 webhook 處理器
- `services/`: 核心爬蟲和處理邏輯
- `utils/`: 工具函數和輔助程式
- `tests/`: 單元和整合測試
- `docs/`: 文檔和資源

## 🖼️ 架構圖
![架構圖](docs/architecture.png)

## 📄 授權
本專案採用 MIT 授權 - 詳見 LICENSE 文件。

## 🤝 貢獻方式
歡迎貢獻！請隨時提交 Pull Request。 