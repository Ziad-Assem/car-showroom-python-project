# 🚗 Car Showroom Management System

A comprehensive system for managing car showrooms across multiple branches, with user authentication and AWS cloud integration.

![Project Diagram](Project%20Diagram.gif)

## 🌟 Features

- **Multi-branch management**: Create and manage multiple showroom branches
- **User roles**: Admin, Manager, and Agent with different privileges
- **Car inventory**: Add, remove, and search cars across branches
- **Sales tracking**: Record and view sales transactions
- **AWS Cloud Integration**: Connects to AWS RDS for database management

## 🛠️ System Architecture

The system uses a 3-tier architecture:
1. **Presentation Layer**: Python CLI interface
2. **Application Layer**: Python business logic (`branches.py`, `functions.py`)
3. **Data Layer**: MySQL database hosted on AWS RDS
