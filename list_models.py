from pipeline.gemini_client import client

models = client.models.list()

for model in models:
    print(model.name)