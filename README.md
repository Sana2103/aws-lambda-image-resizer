# 📸 AWS Lambda Image Resizer

This project demonstrates how to build a **serverless image processing pipeline** using **AWS Lambda** and **Amazon S3**.  

Whenever you upload an image to a source bucket, this Lambda function **automatically resizes it** (default: 128x128) and saves it to a destination bucket.  

---

## 🛠 Tech Stack
- **AWS Lambda** → Runs the image resizing logic (serverless, pay-per-use)  
- **Amazon S3** → Stores both original and resized images  
- **Python 3.11** → Main programming language  
- **Pillow (PIL)** → Image processing library  
- **boto3** → AWS SDK for Python (to interact with S3)  

---

## ⚙️ How It Works
1. **Upload** → Add an image (e.g., `cat.jpg`) to the **source bucket** (`original-images-bucket-v1`).  
2. **Trigger** → S3 event triggers the Lambda function.  
3. **Process** → Lambda downloads the image, resizes it (128x128).  
4. **Store** → The resized image is uploaded to the **destination bucket** (`resized-images-bucket-v1`).  

✅ Fully serverless, no servers to manage!  

