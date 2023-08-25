from fastapi import APIRouter

from src.api.user_management.views import user_profile_views 

# Add route with prefix /api/v1 to manage v1 APIs.
router = APIRouter(prefix="/api/user-management")

router.include_router(user_profile_views.router, tags=["User Management Service Endpoints"])
