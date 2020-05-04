from bs4 import BeautifulSoup
from requests import Session
import re
from urllib.parse import urlparse
import os


class Downloader:
    __s = Session()
    __s.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0'})
    
    def __get_pdf_url(self, url):
        req = self.__s.get(url)
        book_url = None
        if(req.ok):
            soup = BeautifulSoup(req.text, "html.parser")
            parsed = urlparse(req.url)
            a = soup.find("a", "c-button__icon-right", href=re.compile("\/content\/pdf"))
            book_name = re.sub("\n|\r|/", "", soup.find("div", "page-title").get_text().strip())
            try:
                book_url = a.get('href')
                return (book_name, f"https://{parsed.netloc}{book_url}")
            except AttributeError:
                raise ValueError(f"Book {book_name} isn't available")
            

    def __download_file(self, url, download_path):
        file_name = f"{download_path}/{url[0]}.pdf"
        if not os.path.isfile(file_name): #Check if the file already exists locally
            with self.__s.get(url[1], stream=True) as r:
                r.raise_for_status()
                with open(file_name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192): 
                        f.write(chunk)

        return file_name


    def download_pdf(self, url, download_path) -> str:
        return self.__download_file(self.__get_pdf_url(url), download_path)