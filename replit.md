# Document Generator

## Overview

A Flask-based web application that generates Microsoft Word documents programmatically. The system allows users to execute Python code that creates documents using the python-docx library, with automatic file generation and download capabilities. Designed primarily for academic research document creation with a focus on simplicity and user-friendly document generation.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture
- **Framework**: Flask web framework chosen for its simplicity and rapid development capabilities
- **Document Generation Engine**: python-docx library for programmatic Word document creation, allowing full control over document structure and formatting
- **Code Execution System**: Controlled namespace execution environment that safely runs user-provided Python code while maintaining security boundaries
- **File Management**: Temporary document storage in static directory with timestamp-based naming to prevent conflicts
- **Session Management**: Flask's built-in session handling with secret key configuration for user state management

### Frontend Architecture
- **Rendering Strategy**: Server-side rendered HTML using Jinja2 templating engine
- **Styling Approach**: Embedded CSS with neumorphism design principles, featuring gradient animations and shadow effects
- **User Interface Pattern**: Single-page application with form-based interaction for code input and document generation
- **Responsive Design**: Mobile-first approach with flexible container layouts

### Security and File Handling
- **Code Execution Security**: Controlled namespace execution with limited available modules and functions
- **File Serving**: Direct Flask file serving with automatic cleanup and secure path handling
- **Caching Strategy**: Aggressive no-cache headers implementation to prevent browser caching of generated documents
- **Session Security**: Secret key configuration for Flask session encryption

### Document Generation Workflow
- **Input Processing**: User-provided Python code execution in sandboxed environment
- **Document Validation**: Verification that executed code produces valid Document objects
- **File Creation**: Timestamp-based file naming and storage in accessible static directory
- **Download Mechanism**: Automatic file serving through Flask's send_file functionality

## External Dependencies

### Core Python Libraries
- **Flask**: Web application framework for HTTP request handling and response generation
- **python-docx**: Document creation and manipulation library for Microsoft Word format
- **datetime**: Built-in module for timestamp generation and date handling
- **tempfile**: File system utilities for temporary file management
- **os**: Operating system interface for directory and file operations

### Frontend Technologies
- **Vanilla CSS**: Custom styling without external frameworks, implementing neumorphism design patterns
- **Inter Font Family**: Modern typography with system font fallbacks
- **CSS Animations**: Gradient animations and hover effects for enhanced user experience
- **HTML5**: Semantic markup with accessibility considerations

### Runtime Environment
- **Python 3.x**: Required interpreter version for Flask and python-docx compatibility
- **Web Browser**: Any modern browser supporting HTML5 and CSS3 features
- **File System Access**: Local directory creation and file writing permissions required