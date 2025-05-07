from fastapi import APIRouter


router=APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_user():
    """
    Get user data.
    """
    return {"message": "User data"}
