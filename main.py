from updating_and_refreshing.RAG_pipeline import RAGPipeline







def main():
    # Using two of our amazing articles as examples
    urls = [
        "https://www.geeksforgeeks.org/stock-price-prediction-project-using-tensorflow/",
        "https://www.geeksforgeeks.org/training-of-recurrent-neural-networks-rnn-in-tensorflow/"
    ]
    
    pipeline = RAGPipeline(urls)
    pipeline.build()
    
    query = "What is recurrent neural network?"
    response = pipeline.query(query)
    
    print(f"\nQuery: {query}")
    print(f"Response: {response}")

if __name__ == "__main__":
    main()