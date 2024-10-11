
from llama_cpp import Llama
import sys

# Load the model
model_path = "/app/model/meta-llama-3.1-8b-instruct-abliterated.Q6_K.gguf"
llm = Llama(model_path=model_path, n_ctx=131072, n_threads=4)

# LM Studio configuration
config = {
    "input_prefix": "<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n",
    "input_suffix": "<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
    "pre_prompt": "You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability.",
    "pre_prompt_prefix": "<|start_header_id|>system<|end_header_id|>\n\n",
    "pre_prompt_suffix": "",
    "antiprompt": ["<|start_header_id|>", "<|eot_id|>"]
}

def generate_text_stream(prompt, max_tokens=100):
    # Construct the full prompt with the correct structure
    full_prompt = (
        f"{config['pre_prompt_prefix']}{config['pre_prompt']}{config['pre_prompt_suffix']}"
        f"{config['input_prefix']}{prompt}{config['input_suffix']}"
    )

    full_response = ""
    for token in llm(full_prompt, max_tokens=max_tokens, stream=True):
        new_text = token['choices'][0]['text']
        # Check if the new text contains any antiprompt
        if any(ap in new_text for ap in config['antiprompt']):
            break
        full_response += new_text
        yield new_text

    # Remove the input prompt and system message from the full response
    output_only = full_response.split(config['input_suffix'])[-1].strip()
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
