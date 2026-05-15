# Personal Budgeter Web Application


[![Languages](https://img.shields.io/badge/languages-Python%20%7C%20HTML%20%7C%20CSS%20%7C%20JS-blue)]()
[![Tech Stack](https://img.shields.io/badge/tech%20stack-Frontend%20%7C%20API%20%7C%20Backend%20%7C%20Database-red)]()

Table of Contents
- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Design & Architecture](#design--architecture)
- [Contributing](#contributing)

---

## Project Overview

Personal Budgeter is a full-stack web application designed to help users manage their personal finances efficiently.  
The system allows users to create budgets, track transactions, define financial goals, and analyze spending behavior through reports and visual charts.

The project was developed using:

- **Django** for backend development
- **Django REST API** for communication between frontend and backend
- **HTML, CSS, and JavaScript** for frontend development
- **SQLite** as the database system

The application follows the **MVC architectural pattern**, separating:

- **Models** → Database interaction
- **Views** → User interface and presentation
- **Logic/Controllers** → Business logic and request handling
---

## Getting Started

### Prerequisites
- Language: Python 3.0+
- Django
- pillow
- requests
- djangorestframework
- environs

### Installation
Clone the repo and install dependencies:

```bash
git clone https://github.com/Meshref21/Software_implementation_assignment2.git
cd Personal-Budgeter
# make virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
# install dependencies
pip install -r requirements.txt
# run the server on localhost:8000
python manage.py runserver
```
## Design & Architecture
***Class Diagram UML***
<img src="PersonalBudgeter/personal budgeting system.svg">

[Software Design Specification](https://docs.google.com/document/d/1RbGrsFK0z6SSkzjjFF3j0cczkkRGEdBFcEP03kNSBTU/edit?usp=sharing)
Includes Architecture diagram (C4 model) and **Sequence Diagram** for 12 features

## Contributing
Contributions are welcome. Suggested workflow:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feat/short-description`
3. Make changes, add tests.
4. Run tests and linters locally.
5. Open a Pull Request with a clear description and reference to any issue.

