# LAYER Project Constitution

> B2B 고신뢰성 문서 플랫폼 'LAYER' 프로젝트 헌법
> "바퀴를 다시 발명하지 않는다" - 검증된 라이브러리를 조립하여 개발한다.

---

## 원칙 (Principles)

- **모든 백엔드 로직은 TDD로 개발한다** (Mock 기반 단위 테스트)
- 검증된 라이브러리 우선 사용 (FastAPI, Next.js, Arq, Calamine)
- 코드 품질과 타입 안정성을 최우선으로 한다
- **Cloud Native**: 로컬 Docker 대신 외부 클라우드 서비스 활용

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
      ├── unit/         # Mock 기반 단위 테스트
      └── integration/  # 실제 DB 연결 테스트 (선택적)
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

## Testing 규칙 (Mock 기반)

> **중요**: Docker 환경이 없으므로 Testcontainers는 사용하지 않는다.

### 단위 테스트 (Unit Test) - 기본
- **pytest-mock / unittest.mock 사용**: DB, Redis 등 외부 의존성은 철저히 Mock 처리
- **pytest-check 사용**: 다중 assertion 실패 시에도 모든 테스트 결과 확인
- **AsyncMock 활용**: 비동기 함수 테스트 시 `unittest.mock.AsyncMock` 사용
- 테스트 커버리지 최소 80% 유지
- 테스트 파일 네이밍: `test_*.py`

### 통합 테스트 (Integration Test) - 선택적
- 실제 DB 연결이 필요한 테스트는 `@pytest.mark.integration` 마커 사용
- 로컬에서는 `@pytest.mark.skipif` 또는 **SQLite** 대안 사용
- CI/CD 환경에서만 실제 DB 연결 테스트 실행

### 테스트 실행 예시
```bash
# 단위 테스트만 실행 (기본)
pytest tests/unit/

# 통합 테스트 포함 (DB 연결 필요)
pytest tests/ --run-integration
```

---

## 인프라 규칙 (Cloud Native)

> 로컬 Docker 대신 외부 클라우드 서비스를 사용한다.

| 서비스 | 로컬 대안 | 클라우드 |
|--------|-----------|----------|
| PostgreSQL | SQLite (테스트용) | **Supabase** |
| Redis | fakeredis (테스트용) | **Upstash** |

### 환경 변수 (.env)
```env
DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/dbname
REDIS_URL=redis://default:pass@host:6379
```

### 참고
- `.env` 파일은 절대 커밋하지 않는다
- `.env.example`을 참고하여 로컬 환경 설정

---

## 커밋 규칙

- Conventional Commits 사용
- pre-commit hooks 통과 필수 (ruff, mypy, pytest)
- PR 전 모든 테스트 통과 필수
