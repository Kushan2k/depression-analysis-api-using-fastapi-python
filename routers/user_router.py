from fastapi import APIRouter


print("Loading user router...")

router=APIRouter(
    prefix="/api/v1/user",
    
)

@router.get("/test")
async def chat():
    """
    Chat with the user.
    """

    msgs={
        1:'3434'
    }
    return {"message": msgs}


@router.get("/")
async def read_user():
    """
    Get user data.
    """
    return {"message": "User data"}
