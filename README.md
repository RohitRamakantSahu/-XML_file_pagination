# XML Feed Image Viewer

A Streamlit application that parses XML feeds and displays images with pagination.

## Features

- Parse XML feeds and extract image URLs
- Display images in a responsive grid layout
- Pagination support
- Error handling for failed image loads
- Support for multiple XML feed formats

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

## Usage

1. Open the application in your web browser
2. Enter an XML feed URL in the input field
3. Click "Load Feed" to fetch and display images
4. Use the pagination controls to navigate through the images

## Supported XML Feed Formats

The application supports various XML feed formats including:
- RSS feeds with image enclosures
- Media RSS feeds
- Custom XML feeds with image URLs

## Error Handling

The application includes error handling for:
- Invalid XML feeds
- Failed image loads
- Network errors
- Malformed image data 