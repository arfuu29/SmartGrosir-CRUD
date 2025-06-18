# SmartGrosir – CLI

**SmartGrosir** is a lightweight, menu-driven Python CLI that simulates a real-world grocery store. It supports two roles—**Seller** and **Buyer**—so you can manage inventory or shop from the terminal.

---

##  Overview

- **Seller**  
  - Secure login  
  - View / Add / Update / Delete products  
- **Buyer**  
  - Enter your name (no login)  
  - Browse & filter catalog  
  - Add items to cart & view subtotals  
  - Checkout (stock is auto-updated)  

Built with pure Python 3.x and [`tabulate`](https://pypi.org/project/tabulate/) for clean tables.

---

##  Quick Start

1. **Clone**  
   ```bash
   git clone https://github.com/arfuu29/SmartGrosir-CRUD.git
   cd python-project
   ```
2. **Install**  
   ```bash
   pip install tabulate
   ```
3. **Run**  
   ```bash
   python SmartGrosir.py
   ```
4. **Follow Prompts**  
   Choose **1** for Seller or **2** for Buyer and pick actions from the menu.

---

## 👥 Who Should Use This?

- **Small shop owners** who need a simple inventory tool  
- **Python beginners** learning OOP, CLI design, and basic data flow  
- **Students & educators** demoing CRUD + cart workflows

---

## 🔐 Sample Seller Credentials

- **Username**: `admin`  
- **Password**: `rahasia123`

*(Also: `owner` / `rahasia123`)*

---

## 📋 Example Workflow

### Seller
```text
$ python SmartGrosir.py
Select role [1=Seller, 2=Buyer]: 1
Username: admin
Password: *****

[Seller Menu]
1. View Products
2. Add Product
...
Choice: 1
# Displays inventory table
```

### Buyer
```text
$ python SmartGrosir.py
Select role [1=Seller, 2=Buyer]: 2
Enter your name: Alice

[Buyer Menu]
1. View Products
2. Filter Products
3. Add to Cart
4. View Cart
5. Checkout
6. Exit

Choice: 2
Filter keyword: “Milk”
# Shows filtered list
```

---

## 📁 Project Structure

```
python-project/
├── SmartGrosir.py    # Main CLI script
├── README.md         # This README
└── requirements.txt  # tabulate
```
