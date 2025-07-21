from dataclasses import dataclass
from typing import List

from app.src.domain.entities.document_chunk import DocumentChunk


@dataclass
class Answer:
    text: str
    source_chunks: List[DocumentChunk]