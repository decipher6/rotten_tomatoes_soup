import requests
from bs4 import BeautifulSoup
import time

# URL of the Rotten Tomatoes page to scrape
URL = 'https://editorial.rottentomatoes.com/guide/best-netflix-movies-to-watch-right-now/'

def fetch_page(url):
    """Fetches the content of the page using requests."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def parse_page(html):
    """Parses the page content to extract movie names and ratings."""
    soup = BeautifulSoup(html, 'html.parser')
    movies = []

    # Update the class names based on the actual page structure
    for item in soup.find_all('div', class_='article_movie_title'):
        title_tag = item.find('a')
        title = title_tag.text.strip() if title_tag else 'N/A'
        rating_tag = item.find_next_sibling('div', class_='tMeterScore')
        rating = rating_tag.text.strip() if rating_tag else 'N/A'
        movies.append({'title': title, 'rating': rating})
    
    return movies

def main():
    html = fetch_page(URL)
    if html:
        movies = parse_page(html)
        for movie in movies:
            print(f"Title: {movie['title']}, Rating: {movie['rating']}")
        # Respectful scraping: Add delay between requests
        time.sleep(1)

if __name__ == "__main__":
    main()
