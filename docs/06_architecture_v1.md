# Architecture v1.0

## Project Name
Enterprise AI Analytics Framework

## Purpose
A reusable analytics framework that can support multiple business domains using shared data engineering, analytics, dashboarding, reporting, and AI insight modules.

## Core Design
The framework separates reusable platform logic from domain-specific business logic.

## Folder Responsibilities

### app/
User-facing applications:
- Streamlit dashboard
- Report interface
- Future API layer

### framework/
Reusable engine of the platform:
- connectors
- ingestion
- validation
- transformation
- storage
- analytics
- AI insights
- scheduling
- shared utilities

### domains/
Domain-specific logic, mappings, KPI definitions, and documentation.

Supported domains:
- retail
- healthcare
- finance
- HR
- supply_chain
- media_ads

### config/
YAML configuration files for environment settings and domain settings.

### data/
Local data zones:
- raw: original source files
- staging: intermediate cleaned files
- curated: analytics-ready datasets
- exports: final output datasets

### database/
Local DuckDB database files.

### sql/
SQL logic separated by purpose:
- views
- KPIs
- transformations

### docs/
Business and technical documentation.

### notebooks/
Exploration only. Not production code.

### outputs/
Generated reports, summaries, and exports.

### screenshots/
Dashboard and report screenshots for portfolio use.

### tests/
Validation and unit tests.

## Domain Expansion Strategy
Each new domain should include:
- domain README
- domain configuration
- connector
- validation rules
- KPI definitions
- dashboard/report mapping

## Current Version Scope
Version 1 will implement the Retail / Sales Analytics domain first.

## Future Domain
Media Ads Analytics will be added later to reflect advertising and media analytics use cases such as campaign performance, impressions, clicks, CTR, CPM, CPC, conversions, and ROAS.

## Technology Stack
- Python
- pandas
- DuckDB
- SQL
- Streamlit
- PyYAML
- openpyxl
- GitHub
- Public datasets only

## Data Flow

```text
Public Dataset
     ↓
Domain Connector
     ↓
Ingestion
     ↓
Validation
     ↓
Transformation
     ↓
DuckDB
     ↓
SQL KPI Layer
     ↓
Dashboard
     ↓
Executive Summary
     ↓
Automated Report