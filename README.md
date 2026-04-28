markdown
# Comprehensive API for Analyzing Pensioner Demographics and Trends in Abu Dhabi

## Introduction
This API provides programmatic access to the Pensioners Distribution Data for 2022, which includes detailed demographic insights on pensioners in the Abu Dhabi region. The dataset is categorized by gender, type, and quarter, offering valuable information for policymakers, researchers, and other stakeholders.

## Key Features
- Query pensioner distribution by quarter.
- Retrieve gender-based pensioner statistics.
- Calculate the total number of pensioners for 2022.
- Generate actionable insights for demographic analysis and policy-making.

## How to Use

### Installation
1. Clone the repository:
   bash
   git clone https://github.com/your-repo/pensioner-analysis-api.git
   
2. Navigate to the project directory:
   bash
   cd pensioner-analysis-api
   
3. Install the required Python packages:
   bash
   pip install -r requirements.txt
   

### Running the API
1. Place the dataset file (`Distribution of Pensioners 2022.xlsx`) in the project directory.
2. Start the API server:
   bash
   python app.py
   
3. The API will be accessible at `http://127.0.0.1:5000`

### Endpoints

#### 1. Get Pensioners by Quarter
**GET** `/pensioners/quarter`

**Parameters:**
- `quarter` (required): The quarter for which to retrieve data. Valid values: `Q1`, `Q2`, `Q3`, `Q4`.

**Example Request:**
bash
curl "http://127.0.0.1:5000/pensioners/quarter?quarter=Q1"


#### 2. Get Pensioners by Gender
**GET** `/pensioners/gender`

**Parameters:**
- `gender` (required): The gender for which to retrieve data. Valid values: `Male`, `Female`.

**Example Request:**
bash
curl "http://127.0.0.1:5000/pensioners/gender?gender=Male"


#### 3. Get Total Pensioners
**GET** `/pensioners/total`

**Example Request:**
bash
curl "http://127.0.0.1:5000/pensioners/total"


## Feedback
We encourage users to provide feedback to improve the API. Please email us at: opendata@abudhabi.gov.ae.

## License
This project is licensed under the MIT License. For more details, refer to the `LICENSE` file.

---

Developed by Abu Dhabi Open Data Platform

