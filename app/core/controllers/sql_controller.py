from fastapi import HTTPException
from app.core.db.connection import get_connection

def execute_sql_query(query: str):
    try:
        with get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)

            # Si es un SELECT, devolvemos los resultados
            if query.strip().upper().startswith("SELECT"):
                rows = cursor.fetchall()
                return {
                    "status": True,
                    "description": "SUCCESSFUL",
                    "parameters": rows
                }
            else:
                # Para INSERT/UPDATE/DELETE
                conn.commit()
                return {
                    "status": True,
                    "description": "SUCCESSFUL",
                    "parameters": f"{cursor.rowcount} rows affected"
                }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))