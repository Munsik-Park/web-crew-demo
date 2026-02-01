#!/usr/bin/env python
import sys
import os
# 상위 디렉토리를 path에 추가하여 모듈 import 가능하게 함
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from crew import WebCrew

def run():
    """
    WebCrew를 실행합니다.
    """
    print("### Web Design Crew에 오신 것을 환영합니다! ###")
    topic = input("만들고 싶은 웹사이트의 주제를 입력하세요 (예: 맛집 소개 블로그): ")
    
    if not topic:
        topic = '모던한 포트폴리오 웹사이트' # 기본값
        print(f"입력이 없어 기본값 '{topic}'으로 진행합니다.")

    target_url = input("참고하거나 개선하고 싶은 웹사이트 URL이 있다면 입력하세요 (없으면 엔터): ")

    inputs = {
        'topic': topic,
        'target_url': target_url
    }
    
    print(f"\n🚀 '{inputs['topic']}' 프로젝트를 시작합니다! (GitHub 배포 포함)")
    WebCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
