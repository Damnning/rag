from enum import Enum


class DocumentFormat(Enum):
    PDF = '.pdf'
    DOCX = '.docx'
    HTML = '.html'
    TXT = '.txt'


class DocumentRetriever:
    def __init__(self, path: str, format: DocumentFormat):
        self.path = path
        self.format = format

