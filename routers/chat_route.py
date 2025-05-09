
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from api.models.chat_req import ChatRequestBody


questions={
    1:"What is your name?",
    2:"What is your age?",
    3:"What is your favorite color?",
    4:"What is your favorite food?",
    5:"What is your favorite movie?",
}


router=APIRouter(
  prefix="/api/v1/chat"
)

# questions=json.loads(open(os.path.join('../data/questions.json'), 'r'))
@router.get('/questions')
async def get_questions():
    """
    Get all questions.
    """

    return questions


@router.get('/first')
async def start_chat():
    """
    Start a chat.
    """
    return {"q": questions[1], "q_no": 1}


@router.post('/respond')
async def respond_to_chat(body:ChatRequestBody):
    """
    Respond to a chat.
    """

    if body.q_no not in questions.keys():
        raise HTTPException(status_code=404, detail="Question not found")
    
    if body.q_no <max(questions.keys()):
        return JSONResponse(status_code=200, content={"q": questions[body.q_no+1], "q_no": body.q_no+1})

    return {"message": f"you answerd all the questions, your last answer was {body.answer}"}
