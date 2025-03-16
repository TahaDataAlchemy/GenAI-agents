from data.schemaClass import TextInput
from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/download_report")
def download_rep():
    file_path = "analysis_report.docx"
    return FileResponse(path=file_path,filename="Text_Analysis_Report.docx",media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')