# Autoria automotive market data collection and analysis system with automatic processing and reporting

## **Technology stack:** reportlab, bentoml, langchain-ollama, matplotlib, scikit-learn, seaborn, Scrapy, xgboost, docker

## **Goal:** Scrap a website and collect car sales data, then save it in JSON format for data analysis

## Service APIs: BentoML Service API endpoints for inference.

````
URL: /create_scrapy
Scrapy API
:return:
Description: The default COUNT_PAGES=13983 parameter is set in .env. This specifies the number of pages to scan.
When running the Docker image, specify `-e COUNT_PAGES=13983`.
Pages will be scanned automatically and the results will be saved to a file.
````

````
URL: /generate_report_group_models_city
Generate report groups models in the city
:param name:
:param city:
:return:
Description: This function groups data by models in the specified city.
Creates a graph and, using AI analysis, generates a report.
````
````
URL: /generate_report_group_models_name
Generate report groups models for name
:param name:
:return:
Description: This function groups data by models.

Creates a graph and, using AI analysis, generates a report.
````
````
URL: /generate_report_group_year
Generate report group models for name
:return:
Description: This function groups data by year.

Creates a graph and, using AI analysis, generates a report.
````
````
URL: /generate_report_group_switch
Generate report group models for switch
:return:
Description: This function groups data by transmission type.
Creates a graph and, using AI analysis, generates a report.
````
````
URL: /generate_report_group_types
Generate report group models for type
:return:
Description: This function groups data by fuel use type.
Creates a graph and, using AI analysis, generates a report.
````
````
URL: /generate_report_group_year
Generate report group models for year
:param year:
:return:
Description: This function groups data by the specified year of manufacture.
Creates a graph and, using AI analysis, generates a report.
````
````
URL: /generate_report_group_years
Generate report group models for name
:return:
Description: This function groups data by year of manufacture.
Creates a graph and, using AI analysis, generates a report.
````
````
URL: /generate_report_predict
Generate report predict
:return:
Description: This function finds parameters that influence the price of a car and the correlation between parameters.
Creates a graph and, using AI analysis, generates a report.
````