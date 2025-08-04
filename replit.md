# Civil Engineering Materials Weight Calculator

## Overview

This is a Streamlit-based web application designed for civil engineering professionals to calculate the weight of construction materials based on volume inputs. The application provides a user-friendly interface where users can select from various construction materials (concrete, steel, aggregates, soil types, etc.) and calculate their total weight by entering volume in cubic meters. The system includes a comprehensive database of material densities commonly used in civil engineering projects, organized by categories for easy reference.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit web framework for rapid web app development
- **Layout**: Wide layout configuration with sidebar navigation
- **User Interface**: Simple form-based interface with material selection dropdown and volume input
- **Data Display**: Interactive dataframes for material reference tables with category filtering

### Application Structure
- **Modular Design**: Separation of concerns with dedicated modules for data management and UI logic
- **Single Page Application**: All functionality contained within a single page interface
- **Real-time Calculations**: Immediate weight calculations upon user input

### Data Management
- **Static Data Storage**: Material density data stored in Python dictionaries within the codebase
- **Data Processing**: Pandas DataFrames for data manipulation and display
- **Material Categories**: Organized classification system (concrete, steel, aggregates, soil, stone, etc.)

### Core Components
- **Materials Database**: Comprehensive collection of civil engineering material densities (kg/m³)
- **Category System**: Materials grouped by type for better organization and filtering
- **Calculation Engine**: Volume-to-weight conversion using material-specific density values
- **Reference Tables**: Sidebar display of material properties for quick lookup

## External Dependencies

### Python Libraries
- **Streamlit**: Web application framework for the user interface
- **Pandas**: Data manipulation and analysis for material data handling
- **NumPy**: Numerical computing support for calculations

### Data Sources
- **Material Density Database**: Static dataset containing density values for common civil engineering materials at standard conditions
- **No External APIs**: All material data is embedded within the application for offline functionality

### Deployment Considerations
- **Self-contained**: No external database connections required
- **Lightweight**: Minimal dependencies for easy deployment
- **Portable**: Can run in any Python environment with the required libraries