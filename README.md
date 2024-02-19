# Image Color Extractor

Flask Color Extractor is a web application that extracts colors from an uploaded image using the Colorgram library and displays the extracted colors on a webpage.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Features

- Upload an image.
- Extract a specified number of colors from the image.
- Display the extracted colors on a webpage.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/flask-color-extractor.git
    ```

2. Navigate to the project directory:

    ```bash
    cd flask-color-extractor
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open a web browser and go to [http://localhost:5000/](http://localhost:5000/).
3. Upload an image and specify the number of colors to extract.
4. Click the "Extract Colors" button.
5. View the extracted colors on the result page.

## Dependencies

The application relies on the following dependencies:

- Flask: Web framework for Python.
- Colorgram: Library for extracting colors from images.
