# Equation to LaTeX API

This is a FastAPI-based API that converts images of mathematical equations into LaTeX code using the `pix2tex` library. It is designed for integration with Canva extensions or other frontends (e.g., Next.js apps) and supports multiple simultaneous users through a scalable Dockerized setup.

## Features
- **Image to LaTeX Conversion**: Upload an image of a mathematical equation to get its LaTeX representation.
- **RESTful API**: Exposes endpoints for conversion (`/v1/convert`) and health checks (`/v1/health`).
- **Docker Support**: Containerized for easy deployment and scalability.
- **Multi-User Support**: Handles concurrent requests with multiple Uvicorn workers.
- **CORS Configuration**: Configurable for frontend integration (e.g., Next.js at `http://localhost:3000`).


## Prerequisites
- **Python**: 3.11
- **Docker**: For containerized deployment
- **Postman**: For testing API endpoints
- **Image**: A clear equation image (e.g., PNG/JPEG) for testing
- **System**: Sufficient RAM (4GB+ recommended) for `pix2tex`; GPU optional for faster inference


## Setup

### Local Setup
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd equation-latex-api
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   - Copy `.env.example` to `.env` or create `.env`:
     ```text
     FRONTEND_URL=http://localhost:3000
     PORT=8000
     WORKERS=4
     ```
   - `FRONTEND_URL`: Your frontend’s URL (e.g., Next.js app).
   - `PORT`: API port (default: 8000).
   - `WORKERS`: Number of Uvicorn workers (default: 4).

4. **Run the Server**:
   ```bash
   python -m src.main
   ```
   - The server starts at `http://localhost:8000`.
   - Access the Swagger UI at `http://localhost:8000/docs` for interactive testing.


### POST /v1/convert
Converts an equation image to LaTeX code.
- **Request**: `multipart/form-data`
  - Key: `file` (Type: File, PNG/JPEG image)
- **Response**:
  ```json
  {
    "latex_code": "\\frac{a}{b} = c",
    "confidence": null,
    "error": null
  }
  ```
- **Errors**:
  - `400 Bad Request`: Invalid file type.
  - `500 Internal Server Error`: Processing error (e.g., unclear image).

### GET /v1/health
Checks API health.
- **Response**:
  ```json
  {"status": "healthy"}
  ```
## Integration with Next.js
Call the API from your Next.js app:
```javascript
const formData = new FormData();
formData.append("file", imageFile);
const response = await fetch("http://localhost:8000/v1/convert", {
  method: "POST",
  body: formData,
});
const result = await response.json();
console.log(result.latex_code);
```
- Ensure `FRONTEND_URL` in `.env` matches your Next.js app’s URL.