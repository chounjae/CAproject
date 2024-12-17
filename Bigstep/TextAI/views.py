from django.http import HttpResponse
from django.shortcuts import render
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings
from decouple import config


def home(request):
    return render(request, 'textAI.html')


# OpenAI API 키 설정
openai.api_key = ㅇ

@csrf_exempt
def beautify_text(request):
    if request.method == 'POST':
        # 사용자가 보낸 텍스트 가져오기
        data = json.loads(request.body)
        user_text = data.get('text', '')
        
        #프롬프트 설정(== 변경할 말투 설정)
        prompt = f"""입력 받은 문장을 우아한 공주님 말투로 바꿔줘
        예시: "햄버거 먹고싶다" -> "공쥬는 햄버거가 먹꼬 시푼데"
        오직 변환 시킨 문장만 출력해줘.
        사람 이름이 있다면 "이름 + 공쥬"를 붙여서 출력해줘
        반드시 사람 이름일 때만 해야해
        예시: 길동 공쥬는 ~~ 하고싶어.
        완전 공주병 걸린 사람 말투면 좋겠어 
        예시: "똥마렵다" -> "공쥬는 똥마렵다능..."
        말투는 반드시 본인이 상대방에게 말 하는 것 처럼 해줘.
        입력 받은 문장 : \n{user_text}
        """

        try:
            # OpenAI API 호출 (gpt-3.5-turbo 엔진 사용, messages로 전달)
            response = openai.ChatCompletion.create(
                model="gpt-4o",  # 엔진명 수정
                messages=[{"role": "system", "content": "You are a helpful assistant."},
                          {"role": "user", "content": prompt}],
                max_tokens=100,
                temperature=0.7
            )

            # 변환된 텍스트 추출
            beautiful_text = response['choices'][0]['message']['content'].strip()

            return JsonResponse({'success': True, 'text': beautiful_text})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)