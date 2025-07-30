from fastapi import APIRouter, File, UploadFile
from backend.services.file_service import analyze_file



router = APIRouter()
@router.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):
    try:
         print(f"File received: {file.filename}")
         contents = await file.read()
         summary = analyze_file(contents, file.filename)
         print("✅ Summary created successfully")
         return {"summary": summary}
    except Exception as e:
        print(f"❌ Error processing file: {str(e)}")
        return {"error": str(e)}