from google.cloud import vision
from django.shortcuts import render
from django.http import JsonResponse

# 찾을 단어들 리스트 (단어의 순서가 중요함)
target_words = ["in3짱짱",  "오이김치볶음밥", "시락국밥", "지구는이춘식", "오병찐", "알로에맛젤리리",]

# 특정 단어가 레이블에 포함되어 있는지 확인하는 함수
def check_labels(labels, target_words):
    found_words = []
    for label in labels:
        for word in target_words:
            if word.lower() in label.lower():  # 텍스트에서 찾는 단어를 체크
                found_words.append(word)
    return found_words

# 이미지 분석을 처리하는 뷰 함수
def analyze_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']

        # Google Cloud Vision API 클라이언트 생성
        client = vision.ImageAnnotatorClient()

        # 이미지를 Google Cloud Vision API로 분석
        image_content = image.read()
        image = vision.Image(content=image_content)

        # 텍스트 감지 (text_detection 사용)
        response = client.text_detection(image=image)
        texts = response.text_annotations

        # 디버깅: 추출된 텍스트 출력
        print("Detected text:", texts)

        # 텍스트에서 해당 단어들 추출
        found_words = check_labels([text.description for text in texts], target_words)

        # 디버깅: found_words 출력 확인
        print("Found words:", found_words)

        if not found_words:
            return JsonResponse({
                'message': "분석된 단어가 없습니다. 다른 이미지를 시도해보세요."
            })

        # 순서대로 찾은 단어가 있을 때, 맨 오른쪽 단어를 기준으로 문구 생성
        response_message = ""   
 

        if len(found_words) >= 2:
            # 맨 오른쪽 단어를 기준으로 졌다는 문구 생성
            last_word = found_words[-1]
            response_message += f"<span style='color:blue'>{found_words[0]}</span>님이 가장 잘했으며<br> {', '.join(found_words[1:-1])} 님도 모두 잘했지만,<br> <span style='color:red'>{last_word}</span>님의 트롤로 인해 졌습니다."
        elif len(found_words) == 1:
            response_message += f"<span srtle=' color:blue'>{found_words[0]}</span>님을 제외한 팀의 트롤로 억울하게 졌습니다."


        # 결과를 템플릿에 전달하여 analysis_result.html로 렌더링
        return render(request, 'analysis_result.html', {'message': response_message})

    return render(request, 'analyze_image.html')  # 업로드 폼을 표시하는 HTML로 리디렉션