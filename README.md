# FastAPI Spam Detection Service

This project implements a FastAPI service for spam detection in email texts using a machine learning model. It includes a simple API with endpoints for basic interaction and spam prediction.

## Project Structure

- **`main.py`**: The main FastAPI application script.
- **`vectorizer.pkl`**: The pickled TF-IDF vectorizer model.
- **`model.pkl`**: The pickled machine learning model for spam classification.

## Requirements

To run this application, ensure you have the following Python packages installed:

- `fastapi`
- `uvicorn`
- `pickle`
- `nltk`
- `scikit-learn`
- `numpy`

You can install these packages using pip:

```bash
pip install fastapi uvicorn nltk scikit-learn numpy
