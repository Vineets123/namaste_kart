# 📦 NamasteKart Order File Validation System

This project simulates a file validation pipeline for an e-commerce platform named **NamasteKart**, which operates in **Mumbai** and **Bangalore**. The system processes incoming daily transaction files, validates them against business rules, and organizes them into success and rejection folders. A summary email is then sent to notify stakeholders.

---

## 📄 Project Overview

Every day, NamasteKart receives transaction files from its operations in Mumbai and Bangalore. These files must be validated for correctness. The pipeline performs the following:

1. Validates each order within incoming files.
2. Routes each file into either `success_files` or `rejected_files` based on validation results.
3. Creates a detailed error report for each rejected file.
4. Sends an email summary with counts of total, successful, and rejected files.

---

## 🧾 Folder Structure
Incoming file folder is manually created but the other two should be created automatically via code
```
NamasteKart/
├── incoming_files/
│   └── YYYYMMDD/
├── success_files/
│   └── YYYYMMDD/
├── rejected_files/
│   └── YYYYMMDD/
│       └── error_{filename}.csv
├── product_master.csv
├── main.py
├── validations.py
├── mail.py
```

---

## ✅ Validation Rules

Each order in the file must satisfy the following rules:

1. **Product ID** must exist in the product master (`product_master.csv`).
2. **Sales amount** must match: `sales = quantity × product price` (from master).
3. **Order date** must not be in the future.
4. **No field** should be empty.
5. **City** must be either "Mumbai" or "Bangalore".

If even **one** order in the file fails, the **entire file** is marked as rejected.

---

## 📤 Output Handling

- **Successful files** are copied to:  
  `success_files/YYYYMMDD/`

- **Rejected files** are copied to:  
  `rejected_files/YYYYMMDD/`

- **Error report** for each rejected file is created as:  
  `rejected_files/YYYYMMDD/error_{filename}.csv`  
  This file contains:
  - All invalid order rows
  - A column with reason(s) for rejection (semicolon-separated if multiple)

---

## 📧 Email Notification

After processing, an email is sent with:

- Total files processed
- Number of successful files
- Number of rejected files

Even if there are **no files**, the email will still be sent.

**Example Email Content:**
```
Subject: validation email 2023-06-09

FILE VALIDATION DETAILS
1. Number of files - 10
2. Number of successful files - 8
3. Number of rejected files - 2
```

---

## 🛠 Technologies Used

- Python 3.x
- `pandas`, `csv`, `os`, `datetime`, `smtplib`, `email`

---

## ▶️ How to Run

1. Place incoming files in: `NamasteKart/incoming_files/YYYYMMDD/`
2. Ensure `product_master.csv` is in the root directory.
3. Run the pipeline:

```bash
python main.py
```

4. Email summary will be sent automatically.

---

## 📁 Input Files

- `product_master.csv`: Contains `product_id` and price info
- `orders_1.csv`, `orders_2.csv`, etc.: Order files for a specific day

---

## 🧪 Components

- `main.py`: Orchestrates file reading, validation, sorting, and reporting
- `validations.py`: Contains all business logic for order validation
- `mail.py`: Sends validation summary email to stakeholders

---

## 💡 Sample Scenario

10 incoming files on 2025-06-09:
- 8 files valid → moved to `success_files/20250609/`
- 2 files invalid → moved to `rejected_files/20250609/`
- 2 error reports → saved as `error_{filename}.csv` in the same folder
- Email sent with summary

---

## 📌 Note

Ensure you use **app-specific password** in `mail.py` when using Gmail for secure access.

---
