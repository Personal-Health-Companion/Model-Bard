import bardapi
import os

SECRETKEY = ""


def bard(returnString):
    os.environ['_BARD_API_KEY'] = SECRETKEY

    # 바드 대답
    response = bardapi.core.Bard().get_answer(returnString)
    # print(response)

    temp = ""

    for i, choice in enumerate(response['choices']):
        temp += f" Choice {i + 1}: {choice['content'][0]}\n"

    responseString = choice['content'][0]

    return responseString
