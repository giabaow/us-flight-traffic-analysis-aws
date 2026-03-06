# Large-Scale Data Architecture Final Project: US Flight Traffic & Weather Analysis

## Project Overview
As a travel agency in the United States, understanding flight traffic patterns and the impact of weather conditions is essential for anticipating changes in travel demand. Passenger volume varies throughout the year due to seasonal weather, holidays, and traveler behavior, creating clear peak and off-peak seasons.  

This project analyzes historical air traffic passenger statistics for 5 major U.S. airports from 1999 to 2025, combining passenger counts with weather and time factors to identify recurring travel patterns and predict upcoming peak seasons. These insights help travel agencies plan promotions, vouchers, and operational resources in advance, enabling more data-driven marketing strategies and improved customer service.

---

## Stakeholders & Value

### Marketing Department
- Plan campaigns and promotions based on demand patterns.
- Offer vouchers or special deals during peak periods to attract more customers.
- Increase campaign effectiveness through targeted timing.

### Operations Manager
- Optimize staff and resource allocation during high-demand periods.
- Ensure smooth airport operations, including check-ins and boarding.
- Anticipate seasonal spikes in passenger traffic.

### Sales Team
- Focus on high-demand periods and popular destinations.
- Identify opportunities for upselling and creating customized travel packages.
- Align offers with customer behavior to increase revenue.

---

## Pipeline Architecture

### Data Collection
- Flight traffic data collected from CSV files.
- Weather data retrieved via an external API.
- AWS Lambda triggers the API automatically to fetch the latest weather data.
- Datasets are combined to analyze how weather affects passenger traffic.

### Data Storage (Amazon S3)
- Raw and processed data stored in S3 for scalability and durability.
- Provides centralized access to multiple teams without duplication.
- Supports future analysis and historical data retention.

### Data Processing (AWS Glue)
- Cleans, transforms, and merges flight and weather datasets.
- Creates a structured format for analysis and reporting.
- Catalogs the data for easy querying and consistent access.

### Data Analysis (Amazon Athena)
- Queries processed data directly from S3 using SQL.
- Explores passenger trends, seasonal variations, and weather effects.
- Supports marketing, operations, sales, and customer service decisions.

---

## Cost Estimate

| Service        | Cost Details                                                                 | Estimated Monthly Cost |
|----------------|----------------------------------------------------------------------------|----------------------|
| Amazon S3      | 10 GB data storage + requests                                              | $0.28                |
| AWS Lambda     | Triggering weather API (low requests within free tier)                     | $0                   |
| AWS Glue       | ETL job (1 hour/day using 1 DPU)                                          | $13.20               |
| Amazon Athena  | Querying ~50 GB of processed data per month                                | $0.25                |
| **Total**      |                                                                              | **$13.73**           |

> The pipeline is cost-effective due to serverless architecture, paying only for resources used while remaining scalable as data volume grows.

---

## Business Goals Supported
- Forecast peak travel periods for operational efficiency.
- Enable data-driven decisions for promotions, travel packages, and marketing strategies.
- Anticipate high-demand periods and potential disruptions to improve customer satisfaction.
- Leverage serverless services to maintain cost efficiency and scalability.

---

## Key Performance Indicators (KPIs)

1. **Monthly Passenger Volume Associated with Weather Conditions**
   - Measures passenger traffic variation by weather and airport.
   - Helps prepare services like airport transfers, staff allocation, and promotions.

2. **Average Passenger Volume Per Month**
   - Identifies peak and off-peak travel seasons.
   - Supports marketing campaigns, promotions, and resource planning.

3. **Yearly Passenger Volume Per Airline**
   - Tracks airline popularity and customer loyalty trends.
   - Informs partnerships, package deals, and targeted marketing strategies.

> Together, these KPIs help optimize operational planning, marketing strategies, and customer service, ultimately increasing efficiency, satisfaction, and revenue.

---

## Technologies Used
- **Amazon S3** – Data storage and durability  
- **AWS Lambda** – Weather API automation  
- **AWS Glue** – ETL and data processing  
- **Amazon Athena** – Serverless SQL queries on S3  

---

## Future Work
- Implement machine learning models to predict passenger traffic.
- Integrate real-time flight delay and cancellation data.
- Expand analysis to additional airports and international travel.

---

## License
This project is licensed under the MIT License.
