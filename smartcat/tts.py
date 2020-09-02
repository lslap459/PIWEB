# pip install gtts
import os
# pip install playsound
# from playsound import playsound
from gtts import gTTS

tet = "이제, 점심시간 끝났습니다. 분당경영고 학생분들 신달수선생님 앞으로 모여주세요."
tet = "오늘 오후의 수업내용은, 아주 멋진 순서가 준비되어 있습니다. 모두 코로나때문에 지치고 힘들지만, 힘을 냅시다. 화이팅!!"
txt = "덕영고등학교 소프트웨어학과 2학년 신희준, 자바를 열심히 공부하고 있습니다."

filename = "ttsresult.mp3"

tts = gTTS(text=txt, lang='ko')
tts.save(filename)

os.system(f'start {filename}')
# playsound(filename)
