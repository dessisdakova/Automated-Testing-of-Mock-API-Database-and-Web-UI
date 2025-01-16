# Automated Testing of Mock API, Database, and Web UI

## Overview
This project demonstrates **manual** and **automated testing** for **API**, **databases**, and **web UI**, supported by a **custom testing framework** with **test logs** saved to a file. All tests are **containerized** using Docker for consistency and scalability.

------------

*The mock server* (app/, bin/, rsa-cert-generation/, debian_packages.txt), *database* (database/), *Docker images*, and *Docker Compose file* are **sourced from** [waad19/mock-api-server](http://github.com/waad19/mock-api-server "waad19/mock-api-server").

## Key Accomplishments
#### API Testing
- Explored the Flask-based API by reviewing the code and interacting with its endpoints using Postman.
- Created detailed API documentation covering available endpoints, requests, and responses.
- Developed and automated test cases using pytest and the requests library.
- Configured HTTPS requests with self-signed certificates.

------------

#### Database Testing
- Executed SQL queries to validate data integrity and consistency.
- Automated SQL query tests using Python:
	- Validated connection.
	- Verified query outputs against expected results.
- Managed sensitive information securely through environment variables.

------------

#### Web UI Automation
- Automated a shopping flow, including login, adding a product to the cart, proceeding to checkout, and confirming the order.
- Implemented the automation using pytest and Selenium with:
	- Explicit waits for reliable interactions.
	- Cross-browser compatibility testing on Chrome, Firefox, and Edge.

------------

#### Containerization with Docker
- Familiarized with Docker and Docker Compose for containerized environments.
- Gained hands-on experience creating a custom Docker image for the tests container, including investigating and understanding the commands used for image building.
- Ran Selenium tests in Dockerized environments, ensuring test consistency and scalability

------------

#### Testing Framework Development
Designed and implemented a custom testing framework that adheres to modern software engineering principles (SOLID, KISS, YAGNI) and satisfies the following key requirements:

- **Dependency Management**:
Utilized Poetry as the Python package manager to handle dependencies during development and container execution.

- **Test Logging**:
Integrated a logging mechanism using the logging library, with logs directed to a file for enhanced traceability.

- **Data Management**:
Organized test data in YAML files, leveraging the pyyaml library to load and utilize configuration data dynamically during test execution.

- **Pytest-Based Architecture**:
Built the framework around pytest as the test runner and base framework for its flexibility and powerful plugin ecosystem.

- **Helper Utilities**:
	- Created a structured local Python package (tests_lib) for helper classes and methods.
	- Ensured no hardcoded data within helpers; paths to test data files were the only constants.
	- Designed a custom base helper class, which served as a foundation for multiple specialized child helper classes.
	- Followed OOP principles strictly, maintaining one class per file for clarity and reusability.
	- Followed principles like SOLID, KISS, and YAGNI, ensuring modularity and maintainability.
	- Used POM design pattern for Selenium tests.

- **Scalable Design**:
Developed a modular and maintainable structure that aligns with best practices, allowing for easy expansion and collaboration.

## Tech Stack
- Programming Language: **Python**
- Libraries: **Requests**, **Psycopg2-binary**, **PyYAML**, **Logging**, **Python-dotenv**
- Plugin: **Pytest_custom_outputs**
- Testing Framework: **Pytest**
- Tools: **Postman**, **Selenium**, **Poetry**
- Containerization: **Docker**, **Docker Compose**

# Credits
This project utilizes the mock API server from waad19/mock-api-server. For detailed instructions on setting up the containers, please refer to the [original repository](http://github.com/waad19/mock-api-server "original repository").