# 한국 감리교 사경회 관계망 지도 (클릭형 전자판)

석사학위논문 「한국 감리교 평신도 운동의 역사적 고찰 — 사경회의 형성과 역할을 중심으로」의 부록용 클릭형 지도입니다.

- `index.html` : 지도 본체 (파일 하나로 완결, 인터넷 없이도 열림)
- `program.html` : 전체 프로그램 단독 실행 페이지
- `.nojekyll` : GitHub Pages가 파일을 가공하지 않도록 하는 빈 파일
- `make_qr.py` : 게시 주소로 QR 코드(`qr.png`)를 만드는 스크립트

## 로컬에서 보기
`index.html`을 더블클릭하면 브라우저에서 열립니다.

## 게시된 사이트
- 클릭형 관계망 지도: https://pgh3254-droid.github.io/sakyunghoe-map/
- 전체 프로그램: https://pgh3254-droid.github.io/sakyunghoe-map/program.html

두 페이지는 공개 상태로 게시되어 있어 GitHub 로그인 없이 열 수 있습니다.

## QR 코드 만들기
```
pip install qrcode pillow
python make_qr.py https://pgh3254-droid.github.io/sakyunghoe-map/
```
생성된 `qr.png`를 논문 캡션 옆이나 부록에 넣고, 반드시 휴대폰으로 한 번 스캔해 확인하세요.

## 인용 표기 예
지도 캡션: `<그림 1 : 지역별 사경회 관계망 개략도>` / 출처: 연구자 작성 (『코리아 리포지터리』·『코리아 미션 필드』·『기독신보』에 근거). 클릭형 전자판: 위 게시 주소 및 별첨 파일.
