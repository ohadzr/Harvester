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