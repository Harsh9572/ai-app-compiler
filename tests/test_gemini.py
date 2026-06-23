from pipeline.gemini_client import client

print("Starting request...")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Reply with exactly HELLO"
)

print("Response received")
print(response.text)