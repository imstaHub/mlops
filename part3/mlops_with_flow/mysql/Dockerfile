FROM mysql:8

# 쉘 스크립트 복사 (자동 실행 위치)
COPY init.sh /docker-entrypoint-initdb.d/init.sh

# 실행 권한 부여 (선택사항, 일반적으로 mysql 이미지에서는 자동 처리됨)
RUN chmod +x /docker-entrypoint-initdb.d/init.sh
