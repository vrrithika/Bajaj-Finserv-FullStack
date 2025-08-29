from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List

app = FastAPI()


FULL_NAME = "v_r_rithika"
DOB = "27012005" 
EMAIL = "rithikaravi27@gmail.com"
ROLL_NUMBER = "22BLC1315"


class InputData(BaseModel):
    data: List[str]


@app.post("/bfhl")
async def process_data(input_data: InputData):
    try:
        data = input_data.data

        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        sum_numbers = 0
        concat_string = ""

        for item in data:
            if item.isdigit(): 
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                sum_numbers += num
            elif item.isalpha(): 
                alphabets.append(item.upper())
                concat_string += item
            else:  
                special_characters.append(item)

        concat_string = concat_string[::-1] 
        alt_caps = ""
        for i, ch in enumerate(concat_string):
            alt_caps += ch.upper() if i % 2 == 0 else ch.lower()

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME.lower()}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(sum_numbers),
            "concat_string": alt_caps
        }

        return response
    except Exception as e:
        return {"is_success": False, "error": str(e)}
