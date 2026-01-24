# LAYER Project Constitution

> B2B 고신뢰성 문서 플랫폼 'LAYER' 프로젝트 헌법
> "바퀴를 다시 발명하지 않는다" - 검증된 라이브러리를 조립하여 개발한다.

---

## 원칙 (Principles)

- **모든 백엔드 로직은 TDD로 개발한다** (Testcontainers 사용)
- 검증된 라이브러리 우선 사용 (FastAPI, Next.js, Arq, Calamine)
- 코드 품질과 타입 안정성을 최우선으로 한다

---

## Backend 규칙

- **FastAPI 비동기(Async) 우선**: 모든 I/O 작업은 비동기로 처리
- **Router에는 로직 금지**: Service 계층을 분리하여 비즈니스 로직 처리
- **Pydantic v2 엄격 검증**: 모든 입출력 데이터는 Pydantic 모델로 검증
- 디렉토리 구조:
  ```
  backend/
  ├── app/
  │   ├── api/          # Router 정의 (로직 금지)
  │   ├── services/     # 비즈니스 로직
  │   ├── models/       # SQLAlchemy/Pydantic 모델
  │   ├── repositories/ # 데이터 접근 계층
  │   └── core/         # 설정, 의존성 등
  └── tests/
  ```

---

## Frontend 규칙

- **Shadcn/UI 사용**: 일관된 UI 컴포넌트 시스템
- **Server Actions 활용**: 서버 사이드 로직 최대 활용
- **클라이언트 컴포넌트 최소화**: `"use client"` 사용을 최소화
- 디렉토리 구조:
  ```
  frontend/
  ├── app/              # App Router
  ├── components/
  │   ├── ui/           # Shadcn/UI 컴포넌트
  │   └── features/     # 기능별 컴포넌트
  ├── lib/              # 유틸리티
  └── actions/          # Server Actions
  ```

---

## Testing 규칙

- **pytest-check 사용**: 다중 assertion 실패 시에도 모든 테스트 결과 확인
- **DB/Redis는 Mocking 금지**: 실제 환경과 동일하게 Testcontainers 사용
- 테스트 커버리지 최소 80% 유지
- 테스트 파일 네이밍: `test_*.py`

---

## 커밋 규칙

- Conventional Commits 사용
- pre-commit hooks 통과 필수 (ruff, mypy, pytest)
- PR 전 모든 테스트 통과 필수
