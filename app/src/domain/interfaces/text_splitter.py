from abc import ABC, abstractmethod
from typing import List

from app.src.domain.entities.document_chunk import DocumentChunk


class TextSplitter(ABC):
    @abstractmethod
    def split(self, documents: List[DocumentChunk]) -> List[DocumentChunk]:
        pass
