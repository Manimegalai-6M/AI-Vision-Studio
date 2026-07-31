from pathlib import Path

from models.story_model import load_story_model

PROMPT = Path(
    "prompts/accessibility_prompt.txt"
).read_text(
    encoding="utf-8"
)


def generate_accessibility_description(
    caption,
    objects
):
    """
    Generate an accessibility-friendly image description.
    """

    client = load_story_model()

    if isinstance(objects, list):
        object_text = ", ".join(objects)
    else:
        object_text = str(objects)

    prompt = (
        PROMPT.replace("{caption}", caption)
        .replace("{objects}", object_text)
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4,
        max_tokens=250
    )

    return response.choices[0].message.content