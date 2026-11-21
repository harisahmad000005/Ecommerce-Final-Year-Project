# Buy-and-Sell E-Commerce Platform (Undergraduate Final Year Project)

> **Academic Context:** Undergraduate Capstone Project (`CS 699 Project-I` & `CS 6990 Project-II`)  
> **Degree Program:** BS (Honors) Computer Science — Imperial College of Business Studies, Lahore (2015–2019)  
> **Author / Backend Architect:** Haris Ahmad Mubashir (Registration No.: `C1CS013R15-052`)  

---

## 1. Project Overview & Problem Statement

Traditional local buy-and-sell marketplaces often suffer from fragmented listing management, inconsistent transaction states, and tight coupling between presentation layers and business logic. 

This final year project addresses those challenges through the design and implementation of a **decoupled, full-stack Buy-and-Sell E-Commerce Platform**. Built with **Django** on the backend and **React** on the frontend, the system enables users to register, list products, browse and filter marketplace catalogs, and execute end-to-end buying and selling workflows through a structured RESTful API layer.

---

## 2. System Architecture

The application follows a decoupled client-server architecture separating frontend state and UI rendering from backend business logic, persistence, and validation:

```text
+-----------------------+         HTTP / JSON (REST API)         +-----------------------+
|                       |  ----------------------------------->  |                       |
|    React Frontend     |                                        |    Django Backend     |
|  (Client Views & UI)  |  <-----------------------------------  |  (Business Logic &    |
|                       |         Serialized Responses           |   API Endpoints)      |
+-----------------------+                                        +-----------+-----------+
                                                                             |
                                                                             | ORM / SQL
                                                                             v
                                                                 +-----------------------+
                                                                 |  Relational Database  |
                                                                 | (Users, Catalog,      |
                                                                 |  Orders & Listings)   |
                                                                 +-----------------------+
```

---

## 3. My Role & Backend Contributions

As the **Backend Developer** for this two-semester capstone sequence, my primary responsibilities included:

1. **RESTful API Architecture & Endpoint Design:**
   * Designed and implemented modular REST API endpoints exposing marketplace resources (users, product listings, categories, cart/order states, and transaction records) to the React client.
   * Standardized request parsing, JSON response serialization, and HTTP status handling to ensure predictable client-server integration.

2. **Relational Data Modeling & Persistence:**
   * Structured normalized database schemas using Django's ORM to enforce referential integrity across user accounts, seller listings, product metadata, and buyer transactions.

3. **Authentication, Authorization & Validation:**
   * Implemented user registration, authentication flows, and permission checks ensuring sellers can only modify or manage their own listings while buyers can safely browse and initiate purchases.
   * Enforced server-side input validation and data consistency rules across product lifecycle states (e.g., active listings, stock availability, and completed sales).

4. **Integration & Functional Testing:**
   * Tested API endpoints across end-to-end marketplace scenarios in coordination with the React frontend to verify reliability, error handling, and transactional accuracy.

---

## 4. Core Functional Modules

* **User Management & Authentication:** Account creation, login/session/token handling, and role-aware access control for buyers and sellers.
* **Product Catalog & Listing Management:** CRUD operations for creating, updating, categorizing, and managing buy/sell item listings.
* **Search & Filtering:** Query endpoints supporting product discovery by keywords, categories, and listing attributes.
* **Marketplace Transaction Workflows:** Structured endpoints managing buyer inquiries, cart/order creation, and listing status updates upon purchase.

---

## 5. Technology Stack

* **Backend Framework:** Python, Django, Django REST API layer
* **Frontend Framework:** React.js (JavaScript, HTML5, CSS3)
* **Database:** Relational Database (Django ORM)
* **Architecture & Tooling:** RESTful JSON APIs, Git version control

---

## 6. Local Setup & Installation

### Prerequisites
* Python 3.x & `pip`
* Node.js & `npm` (for running the React client)

### Backend Setup (Django)
```bash
# 1. Clone the repository
git clone https://github.com/harisahmad000005/Ecommerce-Final-Year-Project.git
cd Ecommerce-Final-Year-Project

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install backend dependencies
pip install -r requirements.txt

# 4. Apply database migrations and start the development server
python manage.py migrate
python manage.py runserver
```

---

## 7. Academic Evaluation & Outcomes

Completed across `CS 699 Project-I` and `CS 6990 Project-II`, the project successfully demonstrated:
* Clean separation of concerns between a Django REST API backend and a React single-page frontend.
* Reliable relational data modeling and server-side validation for multi-user marketplace operations.
* End-to-end delivery of a functional software engineering system within a structured two-semester academic timeline.
