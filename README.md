# SovereignSys API

## Overview

The SovereignSys API is a project that simulates the management of a micronation. This FastAPI-based application provides endpoints for citizen registration, passport issuance, law creation, and more. It's designed to showcase how a RESTful API can be used to manage the complex operations of a small, self-declared nation.

## Features

- Citizen Registry: Register and manage citizens
- Virtual Passport System: Issue and verify digital passports
- Legal Framework: Create and store laws

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Apsurt/SovereignSys.git
   cd SovereignSys
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the API locally:

1. Start the FastAPI server:
   ```
   fastapi dev SovereignSys/main.py
   ```

2. The API will be available at `http://localhost:8000`

3. Access the interactive API documentation at `http://localhost:8000/docs`

## API Endpoints

- `POST /`: 
- `GET /`: 

For detailed information on request/response formats, please refer to the API documentation at `/docs` when the server is running.

## Example Usage

Here's a quick example of how to use the API with curl:

1. Create a new citizen:
   ```
   curl -X POST "http://localhost:8000/citizens/?name=John%20Doe"
   ```

2. Issue a passport (replace `{citizen_id}` with the ID returned from the previous request):
   ```
   curl -X POST "http://localhost:8000/passports/?citizen_id={citizen_id}"
   ```

3. Create a new law:
   ```
   curl -X POST "http://localhost:8000/laws/?title=Freedom%20of%20Speech&content=All%20citizens%20have%20the%20right%20to%20free%20speech"
   ```

## Contributing

This is a project for demonstration purposes. However, if you'd like to expand on this idea, feel free to fork the repository and make your own changes!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, please open an issue in this repository.

Happy coding, and may your micronation prosper! 🏴