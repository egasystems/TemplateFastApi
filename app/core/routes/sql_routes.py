from fastapi import APIRouter, Body
from app.core.controllers.sql_controller import execute_sql_query

router = APIRouter()
name = "sql"

@router.post("/execute")
def run_query(query: str = Body(..., embed=True)):
    return execute_sql_query(query)