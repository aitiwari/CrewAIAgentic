import re
from bs4 import BeautifulSoup

def clean_text(text: str) -> str:
    """Remove extra whitespace and HTML tags, limiting length."""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'<.*?>', '', text)
    return text[:10000]

def scrape_page_content(url: str, requests_module) -> str:
    """Scrape a webpage’s main content using requests and BeautifulSoup."""
    try:
        response = requests_module.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            main_content = soup.find('main') or soup.find('article') or soup.body
            if main_content:
                return clean_text(main_content.get_text())
        return ""
    except Exception as e:
        return f"⚠️ Content unavailable: {str(e)}"
