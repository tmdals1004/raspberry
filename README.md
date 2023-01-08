# 라즈베리파이
## 한글패치
```
$ sudo apt-get install fonts-unfonts-core
$ sudo apt-get install ibus ibus-hangul
$ sudo reboot
```

# 리눅스
```
ls : 리스트의 줄임말,현재 경로 파일 리스트확인
cd : 디렉토리 바꾸기
mkdir : 디렉토리 만들기
> :  입출력 등을 사용자가 지정한 위치로 우회할 수 있게 해주는 역할(리다이렉션)
echo : 뒤에 쓴 문자열 출력
cat : 리다이렉트로 만든 파일의 내용을 확인함
pwd : 현재 디렉토리 확인
history : 지금까지 친 명령어들 확인
sudo : 슈퍼관리자 권한 대행 사용
vim : 편집기
```

# 명령행인수
```python
import sys

for i in range(1,len(sys.argv)):
  print(sys.argv[1])
```
