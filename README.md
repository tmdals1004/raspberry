# 라즈베리파이
## 한글패치
```
$ sudo apt-get install fonts-unfonts-core
$ sudo apt-get install ibus ibus-hangul
$ sudo reboot
```

# 리눅스 문법
```
ls : 리스트의 줄임말,현재 경로 파일 리스트확인
cd : 디렉토리 바꾸기
mkdir : 디렉토리 만들기
> :  입출력 등을 사용자가 지정한 위치로 우회할 수 있게 해주는 역할(리다이렉션)
echo : 뒤에 쓴 문자열 출력
cat : 파일의 내용을 확인
pwd : 현재 디렉토리 확인
history : 지금까지 친 명령어들 확인
sudo : 최고권리자 권한 대행 사용(최고권리자의 명령)
vim : 편집기
mv : 디렉토리, 파일등을 다른 디렉토리, 파일로 옮기게 해주는 명령어
mv 형태 : mv [이동할 파일이름][이동될 위치][옵션/ 바꿀 파일 이름]
```

# 명령행인수
```python
import sys

for i in range(1,len(sys.argv)):
  print(sys.argv[1])
```
