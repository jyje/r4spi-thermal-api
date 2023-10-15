from fastapi import APIRouter

from thermal.services.main import thermal_services


router = APIRouter()

@router.get("/thermal")
async def get_temperature():
    return await thermal_services.get_temperature()
