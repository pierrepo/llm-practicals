from pathlib import Path
import shutil

from bs4 import BeautifulSoup
from markdownify import markdownify
import requests


def extract_links(base_url, div_class):
    """Extract links from documentation."""
    # Get page content
    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Cannot get URL {base_url}")
        print(f"Status code: {response.status_code}")
        return False
    html_content = BeautifulSoup(response.text, 'html.parser')

    # Find target class.
    div_content = html_content.find("div", class_=div_class)
    if div_content is None:
        print(f"No class {div_class} found")
        return False

    # Extract and clean link urls.
    link_urls = set()
    for link in div_content.find_all("a"):
        url = link.get("href")
        if not url:
            continue
        if "#" in url:
            url = url.split("#")[0]
        if not url.startswith("http"):
            url = base_url + url
        link_urls.add(url)
    print(f"Found {len(link_urls)} urls")
    link_urls = list(link_urls)
    return link_urls

def download_html_files(links, folder_name):
    """Download HTML files and save to Markdown."""
    folder = Path(folder_name)
    folder.mkdir(exist_ok=True)
    for url in links:
        file_name = url.split("/")[-1].replace(".html", ".md")
        try:
            print(f"Downloading {url}")
            response = requests.get(url)
            content = BeautifulSoup(response.content, 'html.parser')
            article = content.find("article")
            if article:
                article_html = str(article)
                article_md = markdownify(article_html)
                print(f"Saving to {file_name}")
                path = folder / Path(file_name)
                path.write_text(article.get_text(strip=True))
        except Exception as e:
            print(f"Cannot download {url}: {e}")


if __name__ == "__main__":
    base_url = "https://manual.gromacs.org/2024.3/reference-manual/"
    div_class = "toctree-wrapper"
    links = extract_links(base_url, div_class)
    target_folder = "gromacs_ref_manual"
    download_html_files(links, target_folder)
    shutil.make_archive(f"{target_folder}.zip", "zip", target_folder)

    