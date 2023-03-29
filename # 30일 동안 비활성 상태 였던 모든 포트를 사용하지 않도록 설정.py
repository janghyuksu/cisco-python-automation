# 30일 동안 비활성 상태 였던 모든 포트를 사용하지 않도록 설정

for switch in my_network:     #my_network의 각 스위치에 대해서
    for interface in switch:    #스위치의 각 인터페이스에 대해서
        if interface.is_down() and interface.last_change() > thirty_days: #인터페이스가 다운되고 30일이상 상태가 변경되지 않은 경우 다음 명령어 수행 
            interface.shutdown()    #인터페이스 종료
            interface.set_description("Interface disabled per Policy")  #인터페이스의 설명을 업데이트



#핵심 논리 
interface.last_change() 
interface_shutdown()


'''  CMD github 커무니티 라이브러리
$ pip install requests
Collecting requests
  Using cached https://files.pythonhosted.org/packages/49/df/50aa1999ab9bde74656c2919d9c0c085fd2b3775fd3eca826012bef76d8c/requests-2.18.4-py2.py3-none-any.whl
<-- output omitted for brevity -->
$ python
 import requests
 requests.get("https://api.github.com")
<Response [200]>
이제 RESTful API와 JSON과 같은 표준화된 데이터 형식 덕분에(나중에 더 깊이 있게 다룰 것입니다)이러한 최신 프로그래밍 언어가 제공하는 것과 동일한 편의를 통해 인프라 요청을 수행할 수 있습니다
'''

