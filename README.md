# AI Agent for LinkedIn

FastAPI-based AI LinkedIn daily post generator and publisher.

## V1 architecture

GitHub Actions / APScheduler -> FastAPI -> LLM -> database -> LinkedIn API

RAG and MCP are intentionally not included in V1.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Open `http://localhost:8000/docs`.

## API

- `POST /api/posts/generate` - generate a draft
- `GET /api/posts` - list posts
- `GET /api/posts/{id}` - get a post
- `POST /api/posts/{id}/approve` - approve a draft
- `POST /api/posts/{id}/publish` - publish approved post
- `GET /health` - health check

## Environment

Set `OPENAI_API_KEY`, `LINKEDIN_ACCESS_TOKEN`, and `LINKEDIN_PERSON_URN` in `.env`.

Keep `AUTO_PUBLISH=false` while testing. After LinkedIn integration is verified, set it to `true` for unattended daily publishing.

Do not commit secrets.

## Next steps

1. Add LinkedIn OAuth 2.0 instead of static credentials.
2. Move production storage to PostgreSQL.
3. Add authentication to the FastAPI endpoints before public deployment.
4. Add AI news/search integration for fresh daily topics.
5. Add quality and duplicate-content checks.
