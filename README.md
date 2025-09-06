# Personal Document Generator

## Overview

A beautiful Flask-based web application that allows you to create custom Microsoft Word documents by executing your own Python scripts. This personal document generator features a modern neumorphism design with an uplifting animated gradient background, providing an elegant interface for programmatic document creation using the python-docx library.

## Features

- **Custom Script Execution**: Paste any Python script that uses python-docx to create documents
- **Beautiful Neumorphism UI**: Modern soft-shadow design elements with tactile feel
- **Animated Gradient Background**: Uplifting, colorful moving gradients for positive user experience
- **Instant Document Generation**: Execute your scripts and download Word documents immediately
- **Flexible Document Creation**: Support for any document structure (headings, paragraphs, tables, styles)
- **Clean Interface**: Simple text area for code input with helpful examples and validation

## How to Use

1. **Open the web application** in your browser
2. **Paste your Python script** in the text area that creates a Word document
3. **Ensure your script** creates a variable named `doc` containing a Document object
4. **Click "Generate Document"** to execute your script
5. **Download the generated file** using the provided download link

### Example Script

```python
from docx import Document

# Create a new Document
doc = Document()
doc.add_heading('My Custom Document', level=1)
doc.add_paragraph('This is a custom paragraph created from my script.')
doc.add_heading('Section 1', level=2)
doc.add_paragraph('Content for section 1.')
```

## System Architecture

### Backend Architecture
- **Framework**: Flask web framework with dynamic code execution
- **Document Engine**: python-docx library for Microsoft Word document creation
- **Code Execution**: Controlled namespace execution of user-provided Python scripts
- **File Management**: Timestamp-based file naming with static directory serving
- **Security**: Sandboxed execution environment with limited namespace access

### Frontend Architecture
- **Design Style**: Neumorphism with soft shadows and modern aesthetics
- **Background**: Animated gradient with smooth color transitions
- **Typography**: Inter font family with clean, readable styling
- **User Interface**: Single-page form-based interaction with real-time feedback
- **Responsive Design**: Mobile-friendly layout with flexible containers

### Document Generation Workflow
1. **User Input**: Python script submission through web form
2. **Code Validation**: Verification of required `doc` variable and Document object
3. **Script Execution**: Controlled execution in limited namespace environment
4. **File Creation**: Document generation with unique timestamp-based naming
5. **Download Delivery**: Secure file serving through Flask's send_file mechanism

## External Dependencies

### Python Libraries
- **Flask**: Web framework for HTTP handling and template rendering
- **python-docx**: Document creation and manipulation library
- **datetime**: Built-in module for timestamp generation
- **os**: Built-in module for file system operations

### Frontend Technologies
- **Vanilla CSS**: Custom neumorphism styling without external frameworks
- **Inter Font**: Modern typography with system font fallbacks
- **CSS Animations**: Smooth gradient transitions and interactive button effects
- **HTML5**: Semantic markup with accessibility considerations

### Runtime Requirements
- **Python 3.x**: Required interpreter for Flask and python-docx
- **Modern Web Browser**: HTML5 and CSS3 support required
- **File System Access**: Local directory creation and write permissions

## Security Considerations

- **Controlled Execution**: Limited namespace for Python script execution
- **Input Validation**: Verification of Document object creation
- **File Isolation**: Generated documents stored in secure static directory
- **Cache Prevention**: No-cache headers to prevent sensitive content caching
- **Session Management**: Flask session security with configured secret key

## Development Setup

1. Install dependencies: `Flask` and `python-docx`
2. Run the application: `python main.py`
3. Access the interface at `http://localhost:5000`
4. Start creating custom documents with your Python scripts!