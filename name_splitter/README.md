# name_splitter

## Overview

The Name Splitter module extends Odoo's partner management functionality by automatically splitting full names into
separate first and last name fields. This module is particularly useful for organizations that need to maintain separate
first and last name records for their contacts.

## Features

- **Automatic Name Splitting**: Intelligently splits full names into first, middle, and last name components
- **Name Composition**: Automatically builds full names from individual components
- **Bidirectional Sync**: Changes to either the full name or individual components automatically update the other fields
- **Smart Name Parsing**: Handles various naming scenarios including single names, multiple middle names, and complex
  name structures

## Field Mapping

| Scenario              | Full Name                  | First Name | Middle Name     | Last Name |
|-----------------------|----------------------------|------------|-----------------|-----------|
| Single name           | "John"                     | "John"     | ""              | ""        |
| Two names             | "John Doe"                 | "John"     | ""              | "Doe"     |
| Three names           | "John Michael Doe"         | "John"     | "Michael"       | "Doe"     |
| Multiple middle names | "John Michael David Smith" | "John"     | "Michael David" | "Smith"   |

## Installation

This module includes a Docker Compose configuration for easy development and testing.

### Prerequisites

- Docker and Docker Compose installed on your system
- Basic knowledge of Docker containers

### Quick Start

1. Start the services:
   ```bash
   docker-compose up -d
   ```

2. Access Odoo at `http://localhost:8069`
    - Email: `user@example.com`
    - Password: `bitnami`

3. Install the Name Splitter module:
    - Go to Apps menu
    - Install the "Contacts" module if not already installed
    - Remove the "Apps" filter
    - Search for "Name Splitter"
    - Click Install

### Docker Services

The docker-compose.yml file sets up two services:

**Odoo Service (`odoo`)**

- **Image**: `bitnami/odoo:18` - Official Bitnami Odoo 18 image
- **Port**: `8069` - Web interface accessible at http://localhost:8069
- **Volumes**:
    - `odoo_data` - Persistent storage for Odoo data
    - `./addons:/addons` - Maps the current directory to the addons folder
- **Environment Variables**:
    - `BITNAMI_DEBUG=true` - Enables debug mode for development
    - `ALLOW_EMPTY_PASSWORD=yes` - Allows empty passwords (development only)
    - `ODOO_ADDONS_DIR=/addons` - Custom addons directory

**PostgreSQL Service (`postgresql-odoo`)**

- **Image**: `bitnami/postgresql:latest` - Official Bitnami PostgreSQL image
- **Purpose**: Database backend for Odoo
- **Volume**: `postgresql-odoo_data` - Persistent database storage
- **Credentials**:
    - Username: `bn_odoo`
    - Database: `bitnami_odoo`
    - Password: None (empty for development)

## Usage

## Field Behavior

### Name Splitting Logic

- **Two words**: "John Doe" → First: "John", Last: "Doe"
- **Multiple words**: "John Michael Doe" → First: "John", Last: "Michael Doe"
- **Single word**: "John" → First: "John", Last: ""
- **Empty**: "" → First: "", Last: ""

### Name Composition Logic

- **Both fields**: First: "John", Last: "Doe" → Name: "John Doe"
- **First only**: First: "John", Last: "" → Name: "John"
- **Last only**: First: "", Last: "Doe" → Name: "Doe"
- **Both empty**: First: "", Last: "" → Name: ""

## Module Structure

```
odoo-name-splitter/
├── __init__.py                 # Module initialization
├── __manifest__.py            # Module manifest and dependencies
├── README.md                  # This documentation
├── models/
│   ├── __init__.py           # Models initialization
│   └── res_partner.py        # Partner model extension with name splitting logic
├── views/
│   └── res_partner_views.xml # UI modifications for partner forms and lists
├── security/
│   └── ir.model.access.csv   # Access control configuration
└── demo/
    └── res_partner_demo.xml  # Demo data for testing
```

## Technical Details

### Dependencies

- `base`: Core Odoo functionality
- `contacts`: Contact management features

### Model Extensions

- **Model**: `res.partner`
- **New Fields**:
    - `first_name`: Char field for first name
    - `middle_name`: Char field for middle name(s)
    - `last_name`: Char field for last name
- **Modified Fields**:
    - `name`: Now computed from name components with inverse function

