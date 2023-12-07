import bardapi
import os

# Github Secret에 환경 변수로 저장
# BARD_SECRET_KEY = os.getenv('BARD_SECRET_KEY')
# 정식 KEY가 아니여서 10~15분에 한 번씩 변경되기 때문에 공개해도 괜찮다고 판단했습니다.
BARD_SECRET_KEY = "dwi_KFY6df1dTNFOnt9_GhRztEE3U2h2UTiCKh3r7ZwFpBIcNuYTub4Xf6D0ypH_0gAqZA."


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
