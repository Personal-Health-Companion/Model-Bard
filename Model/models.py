import bardapi
import os

# Github Secret에 환경 변수로 저장
# BARD_SECRET_KEY = os.getenv('BARD_SECRET_KEY')
BARD_SECRET_KEY = "dwi_KJehFLvhIV4bTJeH1ucEuXxZgomgr4aWRCK7o31cRSKwigDsWSd0ScnJUfLta1LbCQ."


def bard(returnString):
    os.environ['_BARD_API_KEY'] = BARD_SECRET_KEY

    # 바드 대답 받아 오기
    response = bardapi.core.Bard().get_answer(returnString)

    # 바드의 응답은 3가지로 오는데 마지막 응답을 끌어 내기 위하여 for문으로 응답을 돌림
    temp = ""
    for i, choice in enumerate(response['choices']):
        temp += f" Choice {i + 1}: {choice['content'][0]}\n"

    # 최종적으로 3번째 답변을 저장
    responseString = choice['content'][0]

    # 답변을 return
    return responseString
