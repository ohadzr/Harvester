
from llama_cpp import Llama

# Load the model
model_path = "/app/model/meta-llama-3.1-8b-instruct-abliterated.Q6_K.gguf"
llm = Llama(model_path=model_path, n_ctx=4096, n_threads=32)

def generate_text(prompt, max_tokens=50):
    output = llm(prompt, max_tokens=max_tokens, echo=True)
    return output['choices'][0]['text']

if __name__ == "__main__":
    while True:
        prompt = input("Enter a prompt (or 'quit' to exit): ")
        if prompt.lower() == 'quit':
            break
        generated_text = generate_text(prompt)
        print("Generated text:", generated_text)