import boto3

def comprehend_sentiment(text):
    # AWS CLI에서 구성된 자격 증명을 사용하여 Comprehend 클라이언트 생성
    comprehend = boto3.client('comprehend')
    
    # 텍스트 감정 분석pi
    response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    sentiment = response['Sentiment']
    
    return sentiment

def main():
    # 텍스트 입력 받기
    text = input("텍스트를 입력하세요: ")
    
    # 감정 분석 수행
    sentiment = comprehend_sentiment(text)
    # 1 : 긍정
    # 2 : 부정
    # 3 : 중립
    # 4 : 모호
    
    sentiment = 1
    
    # 결과 출력
    print('Sentiment:', sentiment)

if __name__ == "__main__":
    main()
