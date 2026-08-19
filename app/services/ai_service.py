from openai import OpenAI
from app.config import settings

TOPICS = [
    "AI Agents", "RAG", "LLM engineering", "MCP", "Generative AI",
    "AI architecture", "FastAPI and AI", "AI developer productivity",
    "AI coding assistants", "production AI systems",
]

def generate_post(topic: str) -> str:
    if not settings.openai_api_key:
        return (
            f"AI Engineering Insight: {topic}\n\n"
            "The biggest shift in modern software development is moving from "
            "AI demos to reliable production systems. The key is not only the model, "
            "but also good APIs, observability, validation, security and measurable outcomes.\n\n"
            "What are you currently building with AI?\n\n"
            "#AI #GenerativeAI #SoftwareEngineering #AIEngineering"
        )

    client = OpenAI(api_key=settings.openai_api_key)
    prompt = f"""
You are writing a LinkedIn post for a senior software engineer.
Topic: {topic}

Write an original, practical LinkedIn post.
Requirements:
- Strong first-line hook
- 150-220 words
- Human and professional tone
- Explain one useful engineering lesson
- Include a practical example
- Avoid fake claims and generic motivational language
- End with a thoughtful question
- Add 3-5 relevant hashtags
- Do not mention that AI generated the post
"""
    response = client.chat.completions.create(
        model=settings.openai_model,
        messages=[
            {"role": "system", "content": "You are an expert technical LinkedIn content writer."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.8,
    )
    return response.choices[0].message.content.strip()
