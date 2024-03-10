from pydantic import BaseModel, Field
from typing import AnyStr, Optional, Type, Any
import fitz
from gentopia.tools.basetool import BaseTool

class PDFReaderArgs(BaseModel):
    file_path: str = Field(..., description="The path to the PDF file to be read.")

class PDFReader(BaseTool):
    name = "pdf_reader"
    description = "A tool to read and extract text from PDF files."
    
    args_schema: Optional[Type[BaseModel]] = PDFReaderArgs

    def _run(self, file_path: AnyStr) -> str:
        try:
            doc = fitz.open(file_path)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()
            return text
        except Exception as e:
            return f"Failed to read PDF file at {file_path}: {e}"

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

if __name__ == "__main__":
    ans = PDFReader()._run("example.pdf")
    print(ans)

