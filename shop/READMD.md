## 설치 및 시작

중요: django-oscar 의 쿼리 이슈로 **Postgresql 을 사용해야 합니다**

다음의 명령어를 순서대로 수행합니다

```bash
# Oscar 관련 패키지 설지 (이미 설치되었다면 Pass)
$ pip install -r requirements.txt

# Postgresql 설치 (MacOS)
$ brew install postgresql
$ brew services start postgresql

# Psql 사용자 생성
$ createuser root --interactive --pwprompt # 프롬프트 나오면 비밀번호 "PASSWORD" 로 설정
# Psql DB 생성
$ createdb new_real_wavvy

# Oscar 마이그레이션
$ ./manage migrate

# 샘플 데이터 로드
$ make sandbox_load_data
```

## 결제

Iamport 를 사용하여 결제합니다
현재는 제 개인 계정의 Iamport 로 설정되어 있어서, 이 값을 변경해야 합니다
(`inicis_payment.html` 파일의 15번째 줄의 `IMP.init()` 부분에 정보를 변경하면 됩니다)
결제된 정보는 `iamport_payment` 테이블에 저장됩니다