

# 🐾 Zootopia

Zootopia is a small Python project that fetches animal information from the [API Ninjas](https://api-ninjas.com/api/animals) API and generates simple HTML pages.

## Features
- Fetch animal data using an API key stored in a `.env` file
- Generate an HTML page with animal facts
- Simple command-line interface

## Requirements
- Python 3.10+
- `requests`
- `python-dotenv`

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Zootopia.git
   cd Zootopia
   ```
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # on macOS/Linux
   .venv\Scripts\activate      # on Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root:
   ```
   NINJAS_API_KEY=your_api_key_here
   ```

## Usage
Run the main script and enter an animal name when prompted:
```bash
python animals_web_generator.py
```

## Example
```
Enter a name of an animal: shark
Generating animal page for: shark...
```

The result is a simple HTML file containing information about the chosen animal.

---

**Note:** Keep your `.env` file private and never commit it to Git.