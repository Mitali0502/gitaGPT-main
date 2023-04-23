import pinecone


pinecone.init(api_key="YOUR_API_KEY",
              environment="us-west1-gcp")

pinecone.create_index("example-index", dimension=1024)