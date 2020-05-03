from util.book_downloader import Downloader
from util.pdf_parser import extract_url_from_file
from util.progress import progress_bar
import sys



def main():
    books = extract_url_from_file()
    size = len(books)
    downloader = Downloader()
    progress_bar(0, size, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, book in enumerate(books):
        try:
            last_downloaded = downloader.download_pdf(book, sys.argv[1])
        except ValueError as ex:
            pass
        finally:
            progress_bar(i+1, size, prefix = 'Progress', suffix = 'Complete', length = 50)

if __name__ == "__main__":
    main()