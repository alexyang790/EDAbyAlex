# EDAbyAlex

A Python package for streamlined Exploratory Data Analysis (EDA) with support for various file formats.

## Features

- **Flexible Data Loading**
  - Support for both CSV and Excel (.xlsx) files
  - Single file loading with automatic sheet detection
  - Multiple file loading with pattern matching
  - Smart Excel sheet handling

- **Comprehensive EDA Tools**
  - Quick data preview (first 10 rows)
  - Statistical description of numerical columns
  - Dataset information and structure
  - Column listings
  - Unique value analysis
  - Missing value detection

## Installation

```bash
pip install edabyalex
```

## Quick Start

```python
from extractor import extractor

# Initialize and load a CSV file
eda = extractor(path="data.csv")
eda.load()
eda.eda()  # Run complete analysis
```

## Detailed Usage

### Initialization
```python
from extractor import extractor

# For CSV files
eda = extractor(
    path="path/to/file.csv",  # Required: File path
    file_type=None,           # Optional: Defaults to CSV
    file_query=None           # Optional: For multiple file loading
)

# For Excel files
eda = extractor(
    path="path/to/file.xlsx",
    file_type=".xlsx",
    sheet_name="Sheet1"       # Optional: Sheet name
)
```

### Loading Data

#### Single File Loading
```python
# Load CSV
eda = extractor(path="data.csv")
df = eda.load()

# Load Excel with specific sheet
eda = extractor(path="data.xlsx", file_type=".xlsx")
df = eda.load(sheet_name="Sheet1")
```

#### Multiple File Loading
```python
# Load multiple CSV files
eda = extractor(path="./data/", file_query="2024")
df = eda.load_multiple_csv()

# Load multiple Excel files
eda = extractor(path="./data/", file_query="2024")
df = eda.load_multiple_xlsx()
```

### Exploratory Data Analysis

```python
# Run complete EDA
eda.eda()  # Shows:
           # - Data preview (first 10 rows)
           # - Statistical description
           # - Dataset information
           # - Column list
           # - Unique values
           # - Missing values

# View columns
eda.columns()

# Analyze unique values
eda.print_unique()  # All columns
eda.unique_values(col_name="category")  # Specific column
```

### Data Export

```python
# Export to CSV
eda.export(file_type="csv", file_name="output_data")

# Export to Excel
eda.export(file_type=".xlsx", file_name="output_data")
```

### Error Handling

The package includes comprehensive error handling for common scenarios:
- File not found
- Invalid sheet names in Excel files
- Missing columns
- Operations on unloaded data

Example:
```python
try:
    eda = extractor(path="data.xlsx", file_type=".xlsx")
    df = eda.load(sheet_name="NonexistentSheet")
except TypeError as e:
    print(f"Sheet error: {e}")
```

## Requirements

- pandas >= 1.0.0
- numpy >= 1.18.0
- openpyxl >= 3.0.0 (for Excel support)

## Version History

### 0.1.2 (updating documentation)
- Updated README.md

### 0.1.1 (export feature)
- Added export functionality
- Improved package build configuration
- Enhanced error handling
- Updated documentation

### 0.1.0 (Initial Release)
- Basic EDA functionality
- Support for CSV and Excel files
- Data loading and preview features
- Unique value analysis
- Missing value detection

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Alex Yang

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
