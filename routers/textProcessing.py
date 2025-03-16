from usecase.workflow import langgraphPipeline
from data.schemaClass import TextInput
from fastapi import APIRouter, HTTPException 
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/process_text")
def process_text(input_data:TextInput):
    try:
        pipeline_app = langgraphPipeline()

        state_input = {"text":input_data.text}

        result = pipeline_app.invoke(state_input)

        return JSONResponse(
            content={
                "classification": result.get("classification", ""),
                "entities": result.get("entities", []),
                "summary": result.get("summary", "")
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
