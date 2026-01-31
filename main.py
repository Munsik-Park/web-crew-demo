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
    inputs = {
        'topic': '모던한 포트폴리오 웹사이트'
    }
    
    print(f"### '{inputs['topic']}' 제작 프로젝트 시작 ###")
    WebCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
