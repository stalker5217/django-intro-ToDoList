# To Do List

![todolist](https://user-images.githubusercontent.com/51525202/84785164-1e311380-b026-11ea-9d23-45981680a123.png)

<br/>

## 학습 내용

- 기본적인 django 환경 세팅 방법 파악
- app의 개념과 MVT 패턴
- SQLite3을 이용한 CRUD 구현

<br/>

## django 프로젝트 시작하기

django 설치 후 다음 명령어를 통해 프로젝트를 초기화 한다.
``` sh
$ django admin startproject mysite
```

그러면 다음과 같은 프로젝트 구조가 생성된다.

``` 
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py # 프로젝트의 전체적인 설정 값들(app, DB 등)을 관리한다.
        urls.py     # request url routing(특정 view와 연결)을 정의한다.
        asgi.py
        wsgi.py
```

<br/>

# app

하나의 프로젝트는 여러개의 app으로 구성되며 특정 기능 집합을 모듈화하여 개발한다.

다음 명령어로 app을 생성할 수 있다. 

``` sh
$ python manage.py startapp myapp
```

![image](https://user-images.githubusercontent.com/51525202/85221421-a6306800-b3ee-11ea-929a-d4294b430e0f.png)


- View : 요청한 URL에 매핑되어 비즈니스 로직을 실행하는 부분이다. MVC의 Controller 역할과 유사하다.
- Model : class로 나타내며 db 테이블로 표현(orm)이 된다. MVC의 Model 역할과 유사하다.
- template : html 파일로 작성하여 사용자에게 동적인 컨텐츠를 반환한다. MVC의 View 역할과 유사하다.