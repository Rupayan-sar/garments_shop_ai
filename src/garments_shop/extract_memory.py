from ollama import chat

from typing import Optional

from pydantic import BaseModel

import json

from garments_shop.memory import remember

class UserProfile(BaseModel):
    product: Optional[str] = None
    quantity: Optional[int] = None
    buying_price: Optional[float] = None
    selling_price: Optional[float] = None

def extract_memory(user_message):

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": """
Extract useful long-term information from the user's message.

Allowed fields:
- product name
- quantity
- buying_price
- selling_price

If nothing should be remembered, return {}.

Example:

User:
"Today I sold 50 t-shirt's for rupees 300 each which I bought at a wholesale price of rupees 250 each."

Output:
{
    "product": "t-shirt",
    "quantity": "50"
    "buying_price": "250"
    "selling_price": "300"
}
"""
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        format=UserProfile.model_json_schema()
    )

    result = response.message.content

    try:
        data = json.loads(result)

       
    except (json.JSONDecodeError, ValueError):
     return {}

    for key, value in data.items():
        remember(key, value)

    return data