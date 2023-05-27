#!/bin/bash
set -B                  # enable brace expansion

timestamp() {
  date +"%T" # current time
}
timestamp
echo "float operations \n"
for i in {1..50}; do
curl -m 70 -X POST https://float-operation-2tf3r7mlpq-uw.a.run.app \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{
  "N": "100"
}'
echo "\n"
done

timestamp
echo "matmul \n"
for i in {1..50}; do
curl -m 70 -X POST https://matmul-2tf3r7mlpq-uw.a.run.app \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{
  "N": "500"
}'
echo "\n"
done

timestamp
echo "gzip \n"
for i in {1..50}; do
curl -m 70 -X POST https://gzip-compression-2tf3r7mlpq-uw.a.run.app \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{
  "file_size": "500"
}'
echo "\n"
done

timestamp
echo "image-processing \n"
for i in {1..50}; do
curl -m 70 -X POST https://image-processing-2tf3r7mlpq-uw.a.run.app \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{
  "bucket": "image-processing",
  "blob_name": "cat.png"
}'
echo "\n"
done

timestamp
echo "cloud-storage \n"
for i in {1..50}; do
curl -m 70 -X POST https://cloud-storage-2tf3r7mlpq-uw.a.run.app \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{
"src_bucket": "cloud-storage-src",
"dst_bucket": "cloud-storage-dst",
"blob_name": "50mb"
}'
echo "\n"
done

timestamp
echo "video-processing \n"
for i in {1..50}; do
curl -m 130 -X POST https://video-processing-2tf3r7mlpq-uw.a.run.app \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{
  "src_bucket": "video-processing-src",
  "dst_bucket": "video-processing-dst",
  "blob_name": "sample.mp4"
}'
echo "\n"curl -m 130 -X POST https://video-processing-2tf3r7mlpq-uw.a.run.app \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{
  "src_bucket": "video-processing-src",
  "dst_bucket": "video-processing-dst",
  "blob_name": "sample.mp4"
}'
done
