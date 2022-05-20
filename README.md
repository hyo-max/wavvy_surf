<h1 align="center">
서핑 정보 플랫폼 Wavvy
</h1>
‼ Wavvy는 서핑을 즐기는 사람들을 위한 플랫폼으로 날씨와 파도정보를 제공하고 주변 인프라, 편의시설과 서핑에 관한 정보들을 제공합니다

## [Wavvy](http://wavvy.surf)
<div align="center">
<img width="20%" src="https://user-images.githubusercontent.com/52864734/157870495-95bde00f-bff1-4cbc-b4ce-ce2ca068d6dd.png" />
</div>


## Wavvy가 제공하는 기능
- **서핑 스팟** : 해당하는 서핑 스팟의 현재의 날씨와 파도정보, 이후 6일 예측날씨 정보 제공과 이를 토대로 서핑 가능여부와 레벨 추천, 해당주변의 서핑스쿨, 숙박시설, 맛집, 편의시설 정보 제공
- **서핑 스쿨** : 해당 서핑스쿨의 주소, 번호, 사이트 등 과 시설정보, 구글 위치지도 제공
- **서핑 용품** : django-oscar 사용하여 e-commerce 기본 장바구니, 결제, 위시리스트, 상품평 구현
- **커뮤니티** : CRUD사용하여 삭제, 수정, 생성, 댓글
- **채널 웨이비** : model에서 video_key 받아 채널 웨이비에서 재생

## 주요 기능과 로직
- **헥사곤 날씨** : analyze.py > requests.get으로 stormglass api를 json으로 요청하고 DB에 저장하여 가공함.
- **댓글 기능** : 커뮤니티 상세페이지에서 댓글 등록, 수정, 삭제
- **로그인** : 구글 OAuth 로그인 API 사용 django-allauth==0.42.0, kakao API, naver API 간편로그인 제공
- **지도** : 구글 지도 API 사용 (서핑 스쿨 > 지도 페이지)
- **배포** : AWS EC2로 배포하고 media파일 s3에 저장 연동, RDS postgresql 연동

## 기술 스택

- Front
    - Javascript, HTML, CSS, jquery
- Back
    - Python, Django, Postgresql, AWS(EC2, RDS, S3)

