import textract
import glob
import re
import os


url_pattern = re.compile(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')

def extract_url_from_file():
    text = textract.process(os.path.dirname(os.path.abspath(__file__))+ "/Springer Ebooks.pdf")
    
    return [url.group() for url in url_pattern.finditer(str(text))]
