from abc import ABC, abstractmethod
from typing import List

from app.src.domain.entities.document_chunk import DocumentChunk


class DocumentLoader(ABC):
    @abstractmethod
    def load(self, source: str) -> List[DocumentChunk]:
        pass
