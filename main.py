import requests
from bs4 import BeautifulSoup
import time

# URL of the Rotten Tomatoes page to scrape
URL = 'https://www.rottentomatoes.com/top/bestofrt/'

def fetch_page(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    movies = []
    for item in soup.find_all('div', class_='media-body'):
        title = item.find('a', class_='unstyled articleLink').text.strip()
        critic_score = item.find('span', class_='tMeterScore')
        critic_score = critic_score.text.strip() if critic_score else 'N/A'
        movies.append({'title': title, 'critic_score': critic_score})
    return movies

def main():
    html = fetch_page(URL)
    if html:
        movies = parse_page(html)
        for movie in movies:
            print(f"Title: {movie['title']}, Critic Score: {movie['critic_score']}")
        # Respectful scraping: Add delay between requests
        time.sleep(1)

if __name__ == "__main__":
    main()
