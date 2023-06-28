# Backend Developer Discovery

[![Coverage Status](coverage-badge.svg?dummy=8484744)](./reports/coverage/index.html)


## 프로젝트 소개
개발의 유용한 정보를 모아두는 사이트로 Discovery 에 영감을 받아 작업합니다.

### 연계 프로젝트
- [Frontend 프로젝트](https://github.com/rha6780/Frontend_Developer_Discovery) 의 API를 주로 구성합니다.
- [Infra 프로젝트](https://github.com/rha6780/Infra_Developer_Discovery) 에는 Terraform으로 AWS를 구성합니다.
- Frontend에서 구성한 페이지는 SSR로 로컬에서는 docker-compose로 확인할 수 있습니다.


<br>

## Architecture

### DB ERD
![Developer Discovery](https://github.com/rha6780/Backend_Developer_Discovery/assets/47859845/2b6d7e53-414c-4f47-b9c9-71237bff0194)

<br>

## 개발 환경

<details>
<summary>환경 구성</summary>

- Python 3.10
- 다음 명령어를 순차적으로 실행하여 환경 구성을 합니다.
- git clone 프로젝트_CLONE_URL
- `pipenv install`
- `pipenv shell` 로 가상환경에 들어갑니다.
- .envs 폴더를 생성하고 폴더 안에 .dev, .prod, .test 파일을 생성합니다.
- 해당 파일들에 아래 코드를 작성합니다.
```
SECRET_KEY='시크릿 키'
POSTGRES_DB=test_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
```

</details>

<details>
<summary>coverage</summary>

- 로컬에서 환경 구성 이후 developer_discover 폴더에서 coverage run manage.py test 를 통해 현재 커버리지를 알 수 있습니다. 로컬 개발 시 수시로 확인해서 80% 를 목표로 테스트 코드를 작성합시다.
- [coverage](https://coverage.readthedocs.io/en/latest/index.html) 및 [badge](https://smarie.github.io/python-genbadge/) 관련 문서를 참고하세요.
- TODO: github action으로 coverage 뱃지 업데이트 자동화하기

**수동 업데이트**
- 프로젝트 루트에서 `cd developer discover`
- 이전에 테스트한 결과가 있는 경우, `coverage erase`
- `coverage run manage.py test` 를 통해 테스트
- `coverage xml && coverage html` 로 각각 파일 생성
- `mv coverage.xml ../reports/coverage` html의 경우 htmlcov 에서 index를 coverage 폴더로 이동
- 프로젝트 루트에서 `genbadge coverage`로 뱃지 업데이트

</details>
