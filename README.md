# FastAPI GenAI on Azure

This is a scalable **FastAPI application** for integrating **Generative AI** with **Azure Services**. It includes authentication, caching, and database support.


## 🚀 Features:
- **OpenAI GPT-4 Integration** via Azure OpenAI Service
- **JWT Authentication** for secured access
- **Redis Caching** for optimized API response time
- **PostgreSQL Database** for storing chat history
- **Kubernetes-ready deployment** with Docker


## 🔧 Setup & Installation

1️⃣ **Clone the repository**

git clone https://github.com/your-repo/fastapi-genai-azure.git
cd fastapi-genai-azure


2️⃣ **Install dependencies**

pip install -r requirements.txt


3️⃣ **Set up environment variables**

cp .env.example .env

Replace the values inside `.env` with your own API keys.

4️⃣ **Run the application**

uvicorn app.main:app --reload


---

## 🛠 API Endpoints

### **🔐 Authentication**
- `POST /token` – Get JWT token for authentication

### **🤖 AI Chat Generation**
- `POST /generate` – Generate AI responses using GPT-4

### **📊 Health Check**
- `GET /health` – Check if API is running

---

## 🏗 Deployment on Azure Kubernetes (AKS)

1️⃣ **Build & Push Docker Image**

docker build -t fastapi-genai .
docker tag fastapi-genai your-container-registry.azurecr.io/fastapi-genai
docker push your-container-registry.azurecr.io/fastapi-genai


2️⃣ **Deploy to Kubernetes**

kubectl apply -f deployment.yaml


3️⃣ **Check Deployment Status**

kubectl get pods
