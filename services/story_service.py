from pathlib import Path
from models.story_model import load_story_model

PROMPT = Path(
    "prompts/story_prompt.txt"
).read_text(
    encoding="utf-8"
)


def generate_story(
    caption,
    story_type="Kids Story",
    story_length="Short"
):

    client = load_story_model()

    length_instruction = {
        "Short": "Write about 150 words.",
        "Medium": "Write about 300 words.",
        "Long": "Write about 600 words."
    }

    prompt = PROMPT.replace(
        "{caption}",
        caption
    )

    prompt += f"""

Story Type:
{story_type}

Story Length:
{length_instruction[story_length]}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.8,
        max_tokens=900
    )

    return response.choices[0].message.content