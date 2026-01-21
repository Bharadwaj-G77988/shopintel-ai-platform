from fastapi import APIRouter, Depends
from backend.app.core.roles import admin_required
from backend.app.models.user import User

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/dashboard")
def admin_dashboard(current_user: User = Depends(admin_required)):
    return {
        "message": "Welcome Admin",
        "admin_email": current_user.email
    }
