# Text Similarity Check


A brief description of what this project does and who it's for. Explain the purpose of your project and its main functionality. Highlight any unique features or technologies used.

## Getting Started

These instructions will guide you on how to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have met the following requirements:
- You have a working installation of Python (3.x or newer recommended).
- You have installed pip, Python's package installer.

### Installing

Follow these steps to get your development environment running:

1. **Clone the repository**

   ```
   git clone https://github.com/Deepak-7564/text-similarity-check.git
   ```

2. **Navigate to the project directory

   ```
   cd text-similarity-check
   ```

3. Install required packages

   ```
   pip install -r requirements.txt
   ```

This will install all the necessary Python packages as listed in requirements.txt.

## Running the Application
To run the application, execute:

   ```
   python app.py
   ```

## API Endpoints

This application provides several endpoints for computing similarities between texts. Here's how to use them:

### Character-wise Similarity

- **Endpoint:** `/char_similarity`
- **Method:** `POST`
- **Description:** Computes similarity based on character composition between two texts.
- **Payload Example:**

   ```json
   {
     "text1": "Hello, world!",
     "text2": "Hello, everyone!"
   }
   
   ```

## Word Overlap Similarity
- **Endpoint:** `/word_similarity`
- **Method:** `POST`
- **Description:** `Calculates similarity based on the overlap of words between two texts.`
- **Payload Example:**
   ```json
   {
     "text1": "Hello, world!",
     "text2": "Hello, everyone!"
   }
   ```

## Sentiment-wise Similarity
- **Endpoint:** `/sentiment_similarity`
- **Method:** 'POST'
- **Description:** `Computes similarity based on the sentiment analysis of two texts.`
- **Payload Example:**
   ```json
   {
     "text1": "I love sunny days.",
     "text2": "Rainy days make me sad."
   }
   ```

## Embedding-based Word Similarity
- **Endpoint:** `/embedding_similarity`
- **Method:** `POST`
- **Description:** `Determines similarity using word embeddings for more nuanced comparisons.`
- **Payload Example:**
   ```json
   {
     "text1": "I enjoy reading books.",
     "text2": "Reading novels is my hobby."
   }
   ```

## All Similarities
- **Endpoint:** `/all_similarities`
- **Method:** `POST`
- **Description:** `Returns a comprehensive analysis including character-wise, word overlap, embedding-based, and sentiment-wise similarities between two texts.`
- **Payload Example:**
   ```json
   {
     "text1": "Exploring the world is fulfilling.",
     "text2": "Traveling brings joy and enlightenment."
   }
   ```

Each endpoint expects a JSON payload with two keys: text1 and text2, representing the texts to compare. The response will include the similarity score(s) based on the specific comparison method.


Project Link: https://github.com/Deepak-7564/text-similarity-check.git
