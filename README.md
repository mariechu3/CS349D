# Benchmarking of AWS and GCP
code derived from: [Function Bench](https://github.com/ddps-lab/serverless-faas-workbench)

## gcp/
### Contains workloads for: 
- cloud-storage
- float-operations
- gzip
- image_processing
- matmul
- video_processing

### Usage
Create functions on gcp and congfigure the settings (we used the region us-west1 (Oregon) for our computations). Copy and main.py and requirements.txt and change the entry point to function_handler to deploy the functions.

**Note:** for image and video processing make sure to store the image/video to cloud bucket storage before running the functions