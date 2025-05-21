
from contextlib import asynccontextmanager
import os
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
import joblib
from models.chat_req import ChatRequestBody, ChatStartRequestBody
from sklearn.preprocessing import StandardScaler
import pandas as pd
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()


questions = {
    1: {
        "question": "How do you identify your gender?",
        "answers": [{"Male":1}, {"Female":0}]
    },
    2: {
        "question": "What is your age?",
        "answers": []
    },
    
    3: {
        "question": "How much academic pressure do you feel?",
        "answers": [{"None":0}, {"Low":1}, {"Moderate":2}, {"Average":3},{"High":4}, {"Extremely high":5}]
    },
    4: {
        "question": "How are you with your academic CGPA value?",
        "answers": []
    },
    5: {
        "question": "How satisfied are you with your current field of study?",
        "answers": [{
            "Very dissatisfied":0
        }, {
            "Dissatisfied":1
        }, {
            "Neutral":2
        }, {
            "Satisfied":3
        }, {
            "Very satisfied":4
        },{
            "Best":5
        }]
    },
    6: {
        "question": "If you are employed, how satisfied are you with your job?",
        "answers": [{
            "Very dissatisfied":0
        }, {
            "Dissatisfied":1
        }, {
            "Neutral":2
        }, {
            "Satisfied":3
        }, {
            "Very satisfied":4
        },{
            "Best":5
        }]
    },
    7: {
        "question": "On average, how many hours do you sleep?",
        "answers": [ {
            "Less than 5 hours":0,
        
        },{
            "5-6 hours":1
        }, {
            "6-7 hours":2
        }, {
            "More than 8 hours":3
        }, {
            "Others":4
        }]
    },
   
    8: {
        "question": "How would you rate your daily dietary habits?",
        "answers": [{'Healthy':0},{'Moderate':1}, {'Unhealthy':2}, {'Others':3}]
    },
    9: {
        "question": "What level of education are you currently pursuing or have completed?",
        "answers": [{"B.Arch": 3},
        {"B.Com": 10},
        {"B.Ed": 5},
        {"B.Pharm": 7},
        {"B.Tech": 17},
        {"BA": 27},
        {"BBA": 11},
        {"BCA": 2},
        {"BE": 12},
        {"BHM": 8},
        {"BSc": 15},
        {"Class 12": 25},
        {"LLB": 9},
        {"LLM": 16},
        {"M.Com": 21},
        {"M.Ed": 18},
        {"M.Pharm": 1},
        {"M.Tech": 22},
        {"MA": 19},
        {"MBA": 20},]
    },
    10: {
        "question": "Have you ever had suicidal thoughts?",
        "answers": [{"Yes":1},{"No":0}]
    },
    11: {
        "question": "On average, how many hours do you study or work per day?",
        "answers": []
    },
    12: {
        "question": "How would you rate your financial stress level?",
        "answers": [{"Not at all":1}, {"Very low":2}, {"Moderate":3}, {"High":4}, {"Extreme":5}]
    },  
    13: {
        "question": "Does anyone in your immediate family have a history of mental illness?",
        "answers": [{"No":1}, {"Yes":0}]
    },
    
}


# model=_joblib.load('svc_model.joblib')
model=None
gptModel=None 

@asynccontextmanager
async def lifespan(app: APIRouter):
    # Load the ML model
    model=joblib.load('svc_model.joblib')
    # gptModel = OpenAI(
    #     api_key=os.getenv("OPENAI_API_KEY"),
        
    # )

    # response =await gptModel.responses.create(
    #     model="gpt-4.1",
    #     input="Tell me a three sentence bedtime story about a unicorn."
    # )
    # print(response.choices[0].text.strip())
    yield
    # Clean up the ML models and release the resources
    del model

router=APIRouter(
    prefix="/api/v1/chat",
    lifespan=lifespan,
)

# questions=json.loads(open(os.path.join('../data/questions.json'), 'r'))
@router.get('/questions')
def get_questions():
    """
    Get all questions.
    """

    print(dir(model))

    return questions


@router.post('/first')
async def start_chat(body:ChatStartRequestBody):
    """
    Start a chat.
    """

    email=body.email

    data_folder = './data'
    file_path = os.path.join(data_folder, f"{email}.txt")

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    if os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.truncate(0)  # Clear the file
    else:
        with open(file_path, 'w') as file:
            file.write("")  # Create a new file

    

    return {"q": questions[1], "q_no": 1}


@router.post('/respond')
async def respond_to_chat(body:ChatRequestBody):
    """
    Respond to a chat.
    """

    email=body.email

    file=open(os.path.join('./data', f"{email}.txt"), 'a')
    
    if body.q_no not in questions.keys():
        raise HTTPException(status_code=404, detail="Question not found")

    if not body.q_no <max(questions.keys())+1:
        return JSONResponse(status_code=400, content={"message": 'question out of range'})
    

    answer_val=None

    if len(questions[body.q_no]['answers'])==0:
        answer_val=body.answer
    else:
        answer=questions[body.q_no]['answers'][body.answer]

    
    if not answer_val:
        return JSONResponse(status_code=400, content={"message": 'answer not found'})
    
    # return JSONResponse(status_code=200, content={"q": questions[body.q_no+1], "q_no": body.q_no+1})
    
    
    file.write(f"{body.q_no} - {answer_val}\n")

    file.close()

    if body.q_no == max(questions.keys()):

        with open(os.path.join('./data', f"{email}.txt"), 'r') as file:
            lines = file.readlines()
            lines=list(set(lines))
            # print(lines)

            
            answers=list(map(lambda x: x.split(' - ')[1].strip(), lines))

            print(answers)
            

            column_names=[
                'Gender',	'Age','City',	'Academic Pressure'	,	'CGPA',	'Study Satisfaction'	,	'Sleep Duration',	'Dietary Habits',	'Degree',	'Have you ever had suicidal thoughts ?',	'Work/Study Hours',	'Financial Stress',	'Family History of Mental Illness'

            ]
            answers_df=pd.DataFrame(answers, columns=column_names)

            #TODO 
            

            print(answers_df.head())

        return JSONResponse(status_code=200, content={"message": 'End of questions'})
    
    
    # pred=predict_answer(body.answer)

    next_q=questions[body.q_no+1] if body.q_no+1 in questions.keys() else None

    if not next_q:

        return JSONResponse(status_code=400, content={"message": 'question not found'})

    return JSONResponse(status_code=200, content={"q": questions[body.q_no+1], "q_no": body.q_no+1})



def predict_answer(data: dict[str, any]) -> int:
    """
    Predict the answer to a question.
    """

    

    return 1
