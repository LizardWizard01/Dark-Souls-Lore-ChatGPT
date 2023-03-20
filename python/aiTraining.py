import config
import os
import openai
Authorization: Bearer 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
openai.api_key = os.getenv("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")
openai.Model.list()

curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $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" \
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
   }'