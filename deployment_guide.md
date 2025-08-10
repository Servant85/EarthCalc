# APK 생성 완료 가이드

## 현재 성과

✅ **Capacitor Android 프로젝트 완성**
- `gradlew` 파일 생성: `./android/gradlew`
- Android 빌드 설정 완료
- 프로젝트 구조 준비됨

## APK 생성 방법

### 방법 1: 웹 기반 APK 생성 (가장 실용적)

#### 1단계: GitHub 업로드
현재 프로젝트를 GitHub에 업로드
- 저장소: https://github.com/Servant85/earth-calc

#### 2단계: Streamlit Cloud 배포
- https://share.streamlit.io/ 접속
- GitHub 저장소 연결
- 자동 배포로 공개 URL 확보

#### 3단계: PWA Builder 사용
- https://www.pwabuilder.com/ 접속
- Streamlit 앱 URL 입력
- "Android Package" 선택
- APK 자동 생성

### 방법 2: 온라인 APK 변환 도구

**AppsGeyser 사용:**
1. https://appsgeyser.com/ 접속
2. "Create App" 선택
3. "Website" 옵션 선택
4. Streamlit 앱 URL 입력
5. 앱 이름: "토목공사 재료 계산기"
6. APK 다운로드

### 방법 3: Capacitor Cloud Build (고급)

로컬 Android Studio 없이 클라우드에서 빌드:
1. Capacitor 프로젝트를 GitHub에 푸시
2. GitHub Actions 또는 Ionic Cloud 사용
3. 자동 APK 빌드

## 현재 파일 구조

```
earth-calc/
├── android/
│   ├── gradlew ✅           # Gradle Wrapper
│   ├── build.gradle ✅      # Android 빌드 설정
│   └── app/ ✅             # Android 앱 소스
├── www/
│   └── index.html ✅        # 웹앱 래퍼
├── app.py ✅               # Streamlit 메인 앱
├── materials_data.py ✅     # 재료 데이터베이스
├── capacitor.config.json ✅ # Capacitor 설정
└── package.json ✅          # Node.js 설정
```

## 추천 진행 순서

1. **즉시 가능**: PWA Builder 사용
2. **중급**: AppsGeyser 웹 변환
3. **고급**: GitHub Actions 자동 빌드

## 로컬 APK 빌드 (참고용)

만약 Android Studio가 설치된 환경에서:
```bash
cd android
./gradlew assembleDebug
# APK 생성 위치: android/app/build/outputs/apk/debug/
```

## 다음 단계

1. GitHub 업로드 완료
2. Streamlit Cloud 배포
3. 공개 URL로 PWA Builder 사용
4. APK 테스트 및 배포

현재 모든 기반 작업이 완료되었으므로 즉시 APK 생성이 가능합니다.