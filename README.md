# LogParser

> #### 퍼저를 돌리고 나면 수 많은 Log(Crash Log 파일)들이 생성됩니다.
> #### 여기서 어떤 종류의 크래시가 존재하는지를 전체 로그 파일들을 대상으로 파싱하여
> #### 로그 유형 구분 및 빈도수를 확인하기 위해 LogParser를 만들게 되었습니다.

- 사용법
	```
	#도움
	python LogParser.py (-h or --help)
	
	#기본적인 사용법
	python LogParser.py -p (./[DIRECTORY NAME] or ../[DIRECTORY NAME])
	python LogParser.py -p (./[DIRECTORY NAME] or ../[DIRECTORY NAME]) --win
	python LogParser.py --win
	```
- __주의사항__
	```
	#Run As Client 모드는 리눅스에서만 실행 (--win 옵션 또한 사용 X)

	#sshpass 설치 필요
	apt install sshpass

	#ssh 연결 테스트 필요
	ssh ec2-user@[ServerIP] ("yes"입력 후 [Ctrl + C])
	```


- OUTPUT
	- 크래시 종류 및 파일명 리스트파일         : ./OUTPUT/DIVISION.txt
	- 크래시 종류 및 빈도수와 백분율 리스트파일 : ./OUTPUT/RESULT.txt

- Server OUTPUT
	- Slack으로 보낼 내용을 담은 파일 : ./Cache/Data.txt
	- POC 코드                       : ./Cache/POC/?.zip
	
## Update

> #### __Editor__ : Result 가 출력되고 Editor로 파일 조회를 할 건지 정할 수 있습니다.   
> #### __"--win"__ : 시작할 때 옵션을 줘서 Windows에서도 작동 할 수 있습니다.      

#### Editor 의 장단점  
#### __장점__ : 일련번호를 입력하면 각 운영체제에 맞는 Text Editor로 열어서 볼 수 있습니다.   
#### __단점__ : 한번에 한 파일 밖에 열지 못합니다.

- __추가된 기능__
	- __"--win"__ 옵션 (Windows Version)
	- __Editor__ (Open Log Files With A Text Editor)
		- __Windows__ : Notepad
		- __Linux__   : Gedit

- - -
## POC & Parsing Result Sharing Update

> #### LogCollector로 보내기 위해(Client) 실행 할 것인지 파싱 결과만 보기 위해(JustRun) 실행할 것인지 결정하도록 변경했습니다.

- __추가된 기능__
	- __1 번 옵션__ 인 __Run As Client__ 로 실행할 경우   
	  LogCollector를 실행하면 LogParser를 통해 얻은   
	  결과를 LogCollector에 __10분__ 간격으로 보내서 모아두고 __1시간__ 마다 Slack 으로 전송하도록 만들었습니다.

