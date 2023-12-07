import os
import json
import requests
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from Model import models

# Github Secret에 환경 변수로 저장
# BASE_URL = os.getenv('BASE_URL')
BASE_URL = "http://3.39.13.133:8080";


@method_decorator(csrf_exempt, name='dispatch')
class MyView(View):
    def get(self, request, id):
        # 프론트로부터 사용자가 입력한 text 전달 받음
        userText = request.GET.get('text', '')
        # 백으로부터 사용자의 userID가 id인 사용자의 세부 정보를 불러옴
        userDetails = json.loads(requests.get(f'{BASE_URL}/detail/{id}').text)

        # 각각의 대응되는 정보를 별도의 변수를 만들어 저장
        age = userDetails['age']
        gender = userDetails['gender']
        disease1 = userDetails['disease1']
        disease2 = userDetails['disease2']
        disease3 = userDetails['disease3']
        surgery = userDetails['surgery']
        hobby1 = userDetails['hobby1']
        hobby2 = userDetails['hobby2']
        hobby3 = userDetails['hobby3']
        medicine = userDetails['medicine']
        job = userDetails['job']

        if disease1 == '' and disease2 == '' and disease3 == '':
            diseaseString = ""
        elif disease2 == '' and disease3 == '':
            diseaseString = f"{disease1}을 앓았던 이력이 있어, "
        elif disease3 == '':
            diseaseString = f"{disease1}, {disease2}을 앓았던 이력이 있어, "
        else:
            diseaseString = f"{disease1}, {disease2}, {disease3}을 앓았던 이력이 있어, "

        if hobby1 == '' and hobby2 == '' and hobby3 == '':
            hobbyString = ""
        elif hobby2 == '' and hobby3 == '':
            hobbyString = f"{hobby1}를 취미로 하고, "
        elif hobby3 == '':
            hobbyString = f"{hobby1}, {hobby2}를 취미로 하고, "
        else:
            hobbyString = f"{hobby1}, {hobby2}, {hobby3}를 취미로 하고, "

        if medicine == '':
            medicineString = ""
        else:
            medicineString = f"{medicine}을 복용 중이고, "

        if surgery == '':
            surgeryString = ""
        else:
            surgeryString = f"{surgery} 경력이 있으며, "

        if job == '':
            jobString = ""
        else:
            jobString = f"{job}을 직업으로 하고 있어."

        # 사용자 세부 정보로 String 생성 --> bard 모델 튜닝하여 적절한 String의 형태로 구성
        userDetailString = f"내가 {age}이고 {gender}이고 {job}을 직업으로 하고있어.{diseaseString}{hobbyString}{medicineString}{surgeryString}{jobString}"

        # totalRequest: 사용자 세부 정보와 사용자 입력 질문을 모두 합친 String
        totalRequest = f'{userDetailString} {userText}'
        # bardResponse: totalRequest를 사용하여 bard api로 받아온 답변 String
        bardResponse = models.bard(totalRequest)

        # Spring에 보낼 채팅 저장을 위한 JSON
        data = {
            'requestText': userText,
            'responseText': bardResponse
        }
        # Spring으로 정해진 엔드포인트로 데이터 전송 --> data를 받은 Spring은 DB에 저장
        chatSave = requests.post(f'{BASE_URL}/chat/{id}', json=data)
        # 확인
        print(chatSave)

        # 프론트에는 출력 해야할 bardResponse String을 반환
        return HttpResponse(bardResponse)
