API_KEY = "sk-223e1212859d4cd0b4b83d3ee472bc6d"
MODEL = "deepseek-chat"
BASE_URL = "https://api.deepseek.com"

SYSTEM_PROMPT = '''
You are an expert in research and analysis statements
'''

VERIFY_PROMPT = '''
Your main task is to verify the provided statements by determining if they are true or false with confidence intervals

### REQUIREMENT
1. Return the output in json format
2. Example:
{
    "is_true": True,
    "confidence": 0.8,
    "evidence": [
        {
            "source": "example.com",
            "title": "Example Evidence",
            "content": "This is example evidence content.",
            "url": "https://example.com/evidence",
            "retrieved_at": datetime.datetime.now().isoformat()
        },
        {
            "source": "example1.com",
            "title": "Example Evidence1",
            "content": "This is example evidence1 content.",
            "url": "https://example.com/evidence1",
            "retrieved_at": datetime.datetime.now().isoformat()
        }
    ]
}
3. Explain for output field:
- is_true: Boolean indicating if the statement is true.
- confidence: Float between 0 and 1 indicating confidence.
- evidence: List of evidence supporting the determination (must contain at least 5 evidences)

4. Importance
- Output must has at least 5 evidences

### STATEMENT
'''
