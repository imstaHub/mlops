## Directory 구조

```
mlops_with_flow/
│
├── airflow/
│   └── Dockerfile
├── dags (airflow mount)
│
├── mlflow/
│   └── Dockerfile
├── mlruns (mlflow mount)
│
├── mysql/
│   ├── Dockerfile
│   └── init.sh
└── docker-compose.yml
```
<br>

## Features & Issues

#### Airflow와 MLflow의 DB를 Mysql로 사용
- Airflow의 경우, PostgreSQL 또는 MySQL을 사용하면 LocalExecutor(Multiprocessing)을 사용할 수 있음
- 두 개의 서비스가 같이 사용하기 때문에 같은 MySQL 인스턴스 내 다른 DB를 생성하여 사용

#### Airflow, MLflow의 python 패키지 설치 문제
- MySQL을 DB로 사용하기 때문에 python 패키지인 pymysql이 설치되어 있어야 함
- 기본 이미지에는 해당 패키지가 설치되어 있지 않기 때문에 별도의 Dockerfile을 작성하여 custom image 생성

#### MySQL DB 생성
- docker-compose.yml로 생성할 수 있는 DB는 한 개 이므로 두 서비스의 DB를 생성하기 위해서는 추가 command 입력이 필요하며, 별도의 접근 권한도 부여 필요
- MySQL의 컨테이너 생성 시 sh 파일을 통해 DB 생성 스크립트가 자동 실행될 수 있도록 custom image 생성
- sh 파일을 /docker-entrypoint-initdb.d 하위로 복사하면 컨테이너 생성 시 sh 파일을 자동 실행

#### Airflow의 webserver, scheduler 분리
- webserver와 scheduler에 각각 MySQL 연결 필요
- DB init은 둘 중 한 곳에만 하면 됨 (webserver에서 init 하는 것이 일반적)
- webserver에서 init이 완료된 후에 scheduler에서 DB를 연결해야 함

#### Airflow 각 인스턴스에서 DB init 완료 전 동시 connect 문제
- 컨테이너에 들어가 직접 DB 연결 가능
- 자동화를 위해 init을 하지 않은 인스턴스에 '60초 wait' + 'DB 체크' 후 자동 연결