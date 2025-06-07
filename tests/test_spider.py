"""
Tests for WebSpider implementation.
"""

import pytest
import responses
from services.spider import WebSpider

@pytest.fixture
def spider():
    """Create a WebSpider instance for testing."""
    config = {
        'user_agent': 'TestSpider/1.0',
        'request_timeout': 5,
        'retry_count': 2
    }
    return WebSpider(config)

@responses.activate
def test_spider_get_success(spider):
    """Test successful GET request."""
    url = 'https://example.com'
    responses.add(
        responses.GET,
        url,
        json={'status': 'ok'},
        status=200
    )
    
    response = spider.get(url)
    assert response is not None
    assert response.status_code == 200

@responses.activate
def test_spider_get_retry(spider):
    """Test retry mechanism for failed requests."""
    url = 'https://example.com'
    # Add two failures followed by a success
    responses.add(
        responses.GET,
        url,
        status=500
    )
    responses.add(
        responses.GET,
        url,
        status=500
    )
    responses.add(
        responses.GET,
        url,
        json={'status': 'ok'},
        status=200
    )
    
    response = spider.get(url)
    assert response is not None
    assert response.status_code == 200
    assert len(responses.calls) == 3  # Verify retry count

@responses.activate
def test_spider_scrape(spider):
    """Test basic scraping functionality."""
    url = 'https://example.com'
    responses.add(
        responses.GET,
        url,
        json={'status': 'ok'},
        status=200
    )
    
    result = spider.scrape(url)
    assert result is not None
    assert result['status'] == 'success'
    assert result['url'] == url 