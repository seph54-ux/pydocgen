# Document Generator

## Overview

This is a Flask-based web application that generates Word documents for academic research purposes. The application specifically creates "Scope and Limitations" documents for a Smart Coin-Operated Water Dispenser IoT project. Users can generate and download pre-formatted Word documents through a simple web interface.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture
- **Framework**: Flask web framework for Python
- **Document Generation**: Uses python-docx library to create Microsoft Word documents programmatically
- **Template Engine**: Jinja2 templating (built into Flask) for HTML rendering
- **Session Management**: Flask's built-in session handling with secret key configuration

### Frontend Architecture
- **Technology**: Server-side rendered HTML with embedded CSS
- **Styling**: Inline CSS with responsive design principles
- **User Interface**: Single-page application with minimal JavaScript requirements
- **Layout**: Centered container design with modern styling (shadows, rounded corners, hover effects)

### File Management
- **Document Storage**: Temporary file generation in memory or local filesystem
- **Download Mechanism**: Direct file serving through Flask's send_file functionality
- **Caching Strategy**: Aggressive no-cache headers to prevent browser caching issues

### Security Considerations
- **Secret Key**: Configured for Flask session security (placeholder implementation)
- **HTTP Headers**: Security headers implemented to prevent caching of sensitive content
- **File Handling**: Secure file generation and serving without persistent storage

## External Dependencies

### Python Libraries
- **Flask**: Web framework for handling HTTP requests and responses
- **python-docx**: Library for creating and manipulating Microsoft Word documents
- **datetime**: Built-in Python module for timestamp handling
- **os**: Built-in Python module for operating system interface

### Frontend Dependencies
- **No external CSS frameworks**: Uses vanilla CSS for styling
- **No JavaScript libraries**: Minimal client-side functionality
- **Web fonts**: Relies on system fonts (Arial, sans-serif fallback)

### Runtime Requirements
- **Python 3.x**: Required for running the Flask application
- **Web browser**: Any modern browser for accessing the application
- **Microsoft Word compatibility**: Generated documents use .docx format