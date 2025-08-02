from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
from typing import Dict

app = FastAPI(title="Quote API", description="A simple API to get random quotes")

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vite and CRA default ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Hardcoded quotes list
QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "Be the change you wish to see in the world. - Mahatma Gandhi",
    "In the middle of difficulty lies opportunity. - Albert Einstein",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt"
]

@app.get("/")
async def root():
    return {"message": "Quote API is running! Visit /quote to get a random quote."}

@app.get("/quote")
async def get_quote() -> Dict[str, str]:
    """Get a random quote from the hardcoded list."""
    quote = random.choice(QUOTES)
    return {"quote": quote}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 