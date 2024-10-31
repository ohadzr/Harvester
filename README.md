# Harvester

## Installing Requirements

To install the project requirements, follow these steps:
1. Clone the repository:
```aiignore
git clone https://github.com/ohadzr/Harvester
cd Harvester
```

2. Create a virtual environment (optional but recommended):
```aiignore
python3 -m venv --system-site-packages .
source bin/activate
```
3. Install the required packages:
```
pip install -r requirements.txt
```
* If you have issues installing llama-cpp-python try installing it manually (requires scikit-build, Development Tools and cmake )
```
python3 -m pip install llama-cpp-python
```


## Running the container
```aiignore
source bin/activate
# running build once
docker build -t harvester .
# If you prefer not to copy the model file into the Docker image, you can use a Docker volume:
docker run -it -v /path/to/model/directory:/app/model harvester
```


## Tasks for Daniel
1. get a server with a GPU, something like 3080 or higher
2. Badel everything (git code, requirments installation if needed, model - both BF16[https://huggingface.co/mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated-GGUF/resolve/main/meta-llama-3.1-8b-instruct-abliterated.bf16.gguf?download=true] and Q6_K[https://huggingface.co/mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated-GGUF/resolve/main/meta-llama-3.1-8b-instruct-abliterated.Q6_K.gguf?download=true] versions, the small one runs smooth on GPU without CPU but less accurate)
3. Install on the server, if you managed to get the docker to run that's perfect
4. Call me to come and connect it to Nemesis, building a website and other stuff
