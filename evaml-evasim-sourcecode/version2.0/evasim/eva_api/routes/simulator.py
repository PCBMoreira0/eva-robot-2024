from fastapi import APIRouter
from api_controllers import api_controller
from api_controllers import state_controller

router = APIRouter(prefix="/sim", tags=["Simulator"])

@router.get("/geteer")
def gettter():
    return api_controller.get_glob()

@router.post("/next")
async def next():
    api_controller.next_step_sim()
    result = await state_controller.get_result()
    return result