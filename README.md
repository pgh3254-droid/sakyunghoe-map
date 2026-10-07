# 한국 감리교 사경회 관계망 지도 (클릭형 전자판)

석사학위논문 「한국 감리교 평신도 운동의 역사적 고찰 — 사경회의 형성과 역할을 중심으로」의 부록용 클릭형 지도입니다.

- `index.html` : 지도 본체 (파일 하나로 완결, 인터넷 없이도 열림)
- `.nojekyll` : GitHub Pages가 파일을 가공하지 않도록 하는 빈 파일
- `make_qr.py` : 게시 주소로 QR 코드(`qr.png`)를 만드는 스크립트

## 로컬에서 보기
`index.html`을 더블클릭하면 브라우저에서 열립니다.

## GitHub Pages로 게시하기
1. GitHub에 로그인하고 새 저장소(Repository)를 만듭니다. 이름 예: `sakyunghoe-map`, 공개(Public)로 설정합니다.
2. 저장소 화면에서 "Add file → Upload files"를 눌러 이 폴더의 파일 3개(`index.html`, `.nojekyll`, `make_qr.py`)와 `README.md`를 올리고 Commit 합니다.
   - 점(.)으로 시작하는 `.nojekyll`은 탐색기에서 안 보일 수 있습니다. 올리기 어려우면 생략해도 대체로 동작합니다.
3. 저장소의 Settings → Pages로 가서 Source를 "Deploy from a branch", Branch를 `main` / `(root)`로 선택하고 Save 합니다.
4. 1~2분 뒤 같은 화면에 주소가 표시됩니다. 보통 형태는 아래와 같습니다.
   `https://본인계정.github.io/sakyunghoe-map/`
5. 위 주소를 브라우저 시크릿 창에서 열어 보고, 지명을 눌러 지역이 열리는지 확인합니다.

※ GitHub 화면의 메뉴 이름과 위치는 바뀔 수 있습니다.

## QR 코드 만들기
```
pip install qrcode pillow
python make_qr.py https://본인계정.github.io/sakyunghoe-map/
```
생성된 `qr.png`를 논문 캡션 옆이나 부록에 넣고, 반드시 휴대폰으로 한 번 스캔해 확인하세요.

## 인용 표기 예
지도 캡션: `<그림 1 : 지역별 사경회 관계망 개략도>` / 출처: 연구자 작성 (『코리아 리포지터리』·『코리아 미션 필드』·『기독신보』에 근거). 클릭형 전자판: 위 게시 주소 및 별첨 파일.
