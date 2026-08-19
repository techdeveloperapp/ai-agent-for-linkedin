import requests
from app.config import settings

def publish_to_linkedin(content: str) -> str:
    if not settings.linkedin_access_token or not settings.linkedin_person_urn:
        raise RuntimeError("LinkedIn credentials are not configured.")

    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {settings.linkedin_access_token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
    }
    payload = {
        "author": settings.linkedin_person_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": content},
                "shareMediaCategory": "NONE",
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    return response.headers.get("x-restli-id", response.text[:255])
