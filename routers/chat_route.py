
from contextlib import asynccontextmanager
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import joblib
from api.models.chat_req import ChatRequestBody
from sklearn.preprocessing import StandardScaler

questions = {
    1: {
        "question": "How do you identify your gender?",
        "answers": ["Male", "Female", "Non-binary", "Prefer not to say", "Other"]
    },
    2: {
        "question": "What is your age group?",
        "answers": ["Below 18", "18–21", "22–25", "26–30", "Above 30"]
    },
    3: {
        "question": "How urbanized is your current city or town of residence?",
        "answers": ["Rural", "Semi-rural", "Suburban", "Urban", "Metropolitan"]
    },
    4: {
        "question": "How much academic pressure do you feel?",
        "answers": ["None", "Low", "Moderate", "High", "Extremely high"]
    },
    5: {
        "question": "How satisfied are you with your academic CGPA?",
        "answers": ["Very dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very satisfied"]
    },
    6: {
        "question": "How satisfied are you with your current field of study?",
        "answers": ["Very dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very satisfied"]
    },
    7: {
        "question": "If you are employed, how satisfied are you with your job?",
        "answers": ["Very dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very satisfied"]
    },
    8: {
        "question": "On average, how many hours do you sleep on weekdays?",
        "answers": ["Less than 4 hours", "4–5 hours", "6–7 hours", "8–9 hours", "More than 9 hours"]
    },
    9: {
        "question": "On average, how many hours do you sleep on weekends?",
        "answers": ["Less than 4 hours", "4–5 hours", "6–7 hours", "8–9 hours", "More than 9 hours"]
    },
    10: {
        "question": "How would you rate your daily dietary habits?",
        "answers": ["Very unhealthy", "Unhealthy", "Neutral", "Healthy", "Very healthy"]
    },
    11: {
        "question": "What level of education are you currently pursuing or have completed?",
        "answers": ["High school", "Diploma", "Bachelor's", "Master's", "Doctorate"]
    },
    12: {
        "question": "Have you ever had suicidal thoughts?",
        "answers": ["Never", "Rarely", "Sometimes", "Often", "Very frequently"]
    },
    13: {
        "question": "On average, how many hours do you study or work per day?",
        "answers": ["Less than 2 hours", "2–4 hours", "5–7 hours", "8–10 hours", "More than 10 hours"]
    },
    14: {
        "question": "Does anyone in your immediate family have a history of mental illness?",
        "answers": ["Not at all", "Very unlikely", "Unsure", "Likely", "Definitely yes"]
    },
    15: {
        "question": "How often do you feel symptoms of depression (e.g., sadness, hopelessness, lack of energy)?",
        "answers": ["Never", "Rarely", "Sometimes", "Often", "Always"]
    }
}

# model=_joblib.load('svc_model.joblib')
model=None 

@asynccontextmanager
async def lifespan(app: APIRouter):
    # Load the ML model
    model=joblib.load('svc_model.joblib')
    yield
    # Clean up the ML models and release the resources
    del model

router=APIRouter(
    prefix="/api/v1/chat",
    lifespan=lifespan,
)

# questions=json.loads(open(os.path.join('../data/questions.json'), 'r'))
@router.get('/questions')
async def get_questions():
    """
    Get all questions.
    """

    print(dir(model))

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
    
    pred=predict_answer(body.answer)

    return {"message": f"you answerd all the questions, your last answer was {body.answer}"}



def predict_answer(data: dict[str, any]) -> int:
    """
    Predict the answer to a question.
    """

    

    return 1
