
from llama_cpp import Llama
import sys

# Load the model
model_path = "/app/model/meta-llama-3.1-8b-instruct-abliterated.Q6_K.gguf"
llm = Llama(model_path=model_path, n_ctx=4096, n_threads=4, seed=55555)


def generate_text_stream(prompt, max_tokens=100):
    full_response = ""
    for token in llm(prompt, max_tokens=max_tokens, stream=True):
        new_text = token['choices'][0]['text']
        full_response += new_text
        yield new_text

    # Remove the input prompt from the full response
    output_only = full_response[len(prompt):].lstrip()
    return output_only


def get_multiline_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines)


if __name__ == "__main__":
    while True:
        prompt = get_multiline_input("Enter a prompt (or 'quit' to exit). Press Enter twice to finish input:")
        if prompt.lower() == 'quit':
            break

        max_tokens = input("Enter max tokens for response (default 100): ")
        max_tokens = int(max_tokens) if max_tokens.isdigit() else 100

        print("\nGenerated text:")
        output = ""
        for text_chunk in generate_text_stream(prompt, max_tokens):
            output += text_chunk
            sys.stdout.write(text_chunk)
            sys.stdout.flush()

        # Clear the line and reprint the output without the prompt
        sys.stdout.write('\r' + ' ' * len(output) + '\r')
        sys.stdout.flush()
        print(output.lstrip())
        print()  # Add a newline after the complete response