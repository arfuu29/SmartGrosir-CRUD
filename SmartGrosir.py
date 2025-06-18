# Grocery Store Management Application - Full commented version
# Grocery Store Management Application
# Simple CLI for sellers and buyers to manage products and sales

# Import library
from tabulate import tabulate
# Import libraries and typing tools
from typing import Dict, Any, List, Optional
import getpass


# Sample data
catalog_dict = {
    1:  {"nama": "Indomie Mi Goreng",                "kategori": "Makanan Instan",      "harga": 3250,   "stok": 50},
    2:  {"nama": "Beras Ramos 5kg",                  "kategori": "Bahan Pokok",         "harga": 62000,  "stok": 30},
    3:  {"nama": "Minyak Goreng Filma 1L",           "kategori": "Bahan Pokok",         "harga": 14200,  "stok": 40},
    4:  {"nama": "Gula Pasir Gulaku 1kg",            "kategori": "Bahan Pokok",         "harga": 14000,  "stok": 35},
    5:  {"nama": "Tepung Terigu Segitiga Biru 1kg",  "kategori": "Bahan Pokok",         "harga": 10500,  "stok": 25},
    6:  {"nama": "Telur Ayam Petelur 1kg (~16 bt)",   "kategori": "Protein",             "harga": 38000,  "stok": 20},
    7:  {"nama": "SariWangi Teh Celup 25s",          "kategori": "Minuman",             "harga": 8000,   "stok": 45},
    8:  {"nama": "Kapal Api Special Mix 200g",       "kategori": "Minuman",             "harga": 22000,  "stok": 28},
    9:  {"nama": "Aqua Mineral 600ml",               "kategori": "Minuman",             "harga": 4500,   "stok": 60},
    10: {"nama": "Teh Kotak Sosro 250ml",            "kategori": "Minuman",             "harga": 6000,   "stok": 50},
    11: {"nama": "Ultra Milk UHT 1L",                "kategori": "Minuman",             "harga": 18500,  "stok": 22},
    12: {"nama": "Detergent Attack 800g",            "kategori": "Kebutuhan Rumah Tangga","harga": 13000,  "stok": 30},
    13: {"nama": "Sabun Mandi Dove 100g",            "kategori": "Kebutuhan Rumah Tangga","harga": 9000,   "stok": 25},
    14: {"nama": "Garam Refina 500g",                "kategori": "Bumbu Dapur",         "harga": 4500,   "stok": 40},
    15: {"nama": "Kecap Bango 550ml",                "kategori": "Bumbu Dapur",         "harga": 15000,  "stok": 20},
    16: {"nama": "Saus Sambal ABC 335ml",            "kategori": "Bumbu Dapur",         "harga": 11500,  "stok": 18},
    17: {"nama": "Masako Bumbu Instan 60g",          "kategori": "Bumbu Dapur",         "harga": 8500,   "stok": 35},
    18: {"nama": "Mie Sedaap Rasa Ayam",             "kategori": "Makanan Instan",      "harga": 3500,   "stok": 48},
    19: {"nama": "Minyak Goreng Tropical 2L",        "kategori": "Bahan Pokok",         "harga": 30000,  "stok": 15},
    20: {"nama": "Biskuit Roma Marie 300g",          "kategori": "Snack",               "harga": 12000,  "stok": 25},
    21: {"nama": "Gudang Garam Merah Filter",        "kategori": "Rokok",               "harga": 18000,  "stok": 40},
    22: {"nama": "Sampoerna A Mild",                 "kategori": "Rokok",               "harga": 20000,  "stok": 35},
    23: {"nama": "Djarum Super Kretek",              "kategori": "Rokok",               "harga": 16000,  "stok": 30},
    24: {"nama": "Permen Kopiko 10g",                "kategori": "Jajanan",             "harga": 1000,   "stok": 100},
    25: {"nama": "Permen Spearmint 10g",             "kategori": "Jajanan",             "harga": 1000,   "stok": 90},
    26: {"nama": "Choki-Choki 12g",                  "kategori": "Jajanan",             "harga": 1000,   "stok": 80},
    27: {"nama": "Big Babol Bubble Gum 9g",          "kategori": "Jajanan",             "harga": 1000,   "stok": 110},
    28: {"nama": "Chitato 45g",                      "kategori": "Snack",               "harga": 8000,   "stok": 50},
    29: {"nama": "Taro Net 75g",                     "kategori": "Snack",               "harga": 5000,   "stok": 45},
    30: {"nama": "Beng-Beng Wafer Bar 27g",          "kategori": "Snack",               "harga": 3000,   "stok": 60},
}

# Menggunakan class agar lebih terstruktur

# Class produk untuk membuat objek produk yang berisi sku, name, catagory, price and stok
# Class Product: represents a single product with its attributes and to_dict method
class Product:
    """Represents a single product in the store."""
    def __init__(self, sku: int, name: str, category: str, price: int, stock: int):
        # Initialize product attributes
        self.sku = sku
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    # Convert product to a dictionary for display or export
    def to_dict(self) -> Dict[str, Any]:
        return {"sku": self.sku, "name": self.name, "category": self.category, "price": self.price, "stock": self.stock}

# Class Store: manages products, cart, and business logic for seller/buyer
class Store:
    """Manages products, shopping cart, and provides seller/buyer operations."""
    def __init__(self, products: List[Product]):
        # Store products by SKU for quick lookup
        self.products: Dict[int, Product] = {p.sku: p for p in products}
        self.cart: List[Dict[str, Any]] = []   

    # Method to display products in a table format using tabulate
    def display_products(self, products: Optional[List[Product]] = None) -> None:
        """
        Tampilkan tabel produk.
        Kalau products None → semua produk self.products.values().
        """
        prods = products if products is not None else list(self.products.values())
        # Ubah ke list of dict
        rows = [p.to_dict() for p in prods]
        print(tabulate(rows, headers="keys", tablefmt="grid", showindex=False))

    # Method to filter catalog based on Category, price, stok avaibility
    def filter_products(
        self,
        kategori: Optional[str] = None,
        min_harga: Optional[int] = None,
        max_harga: Optional[int] = None,
        only_in_stock: bool = False) -> List[Product]:
        """Kembalikan list Product yang cocok dengan kriteria."""
        hasil: List[Product] = []

        for p in self.products.values():
            # filter kategori jika diisi
            if kategori and p.category.lower() != kategori.lower():
                continue
            # filter harga minimal
            if min_harga is not None and p.price < min_harga:
                continue
            # filter harga maksimal
            if max_harga is not None and p.price > max_harga:
                continue
            # hanya stok > 0
            if only_in_stock and p.stock <= 0:
                continue

            hasil.append(p)
        return hasil

    # Method to add a product (or add to cart) with validation checks
    def add_product(self, sku: int, name: str, category: str, price: int, stock: int) -> None:
        # Add a new product if SKU not already in catalog
        if sku in self.products:
            print(f"SKU {sku} sudah ada di katalog.")
        else:
            self.products[sku] = Product(sku, name, category, price, stock)

    def update_product(self, sku: int, price: Optional[int] = None, stock: Optional[int] = None) -> None:
        # Update price and/or stock for an existing product
        product = self.products.get(sku)
        if not product:
            print("Produk tidak ditemukan.")
            return
        if price is not None:
            product.price = price
        if stock is not None:
            product.stock = stock
        print(f"Produk '{product.name}' berhasil diperbarui.")

    def remove_product(self, sku: int) -> None:
        # Remove product from catalog
        product = self.products.pop(sku, None)
        if product:
            print(f"Produk '{product.name}' berhasil dihapus.")
        else:
            print("Produk tidak ditemukan.")

    def add_to_cart(self, sku: int, qty: int) -> None:
        # Add item to cart if enough stock is available        
        product = self.products.get(sku)
        if not product:
            print("Produk tidak ditemukan.")
            return
        if qty <= 0:
            print("Jumlah harus lebih besar dari 0.")
            return
        if qty > product.stock:
            print(f"Stok tidak cukup. Tersedia: {product.stock}.")
            return
        product.stock -= qty
        total_price = qty * product.price
        self.cart.append({"Nama": product.name, "QTY": qty, "Harga": product.price, "Total": total_price})
        print(f"{qty} x '{product.name}' ditambahkan ke keranjang.")

    def view_cart(self) -> None:
        # Display current cart contents
        if not self.cart:
            print("Keranjang kosong.")
        else:
            print(tabulate(self.cart, headers="keys", tablefmt="grid"))

    def checkout(self) -> int:
        # Calculate total, display cart, and clear it
        if not self.cart:
            print("Keranjang kosong.")
            return 0
        total = sum(item["Total"] for item in self.cart)
        self.view_cart()
        print(f"Total pembayaran: Rp {total}")
        self.cart.clear()
        return total
    
SELLER_CREDENTIALS = {
    "admin": "rahasia123", 
    "owner": "rahasia123"
}

# Seller Validation
def authenticate_seller() -> bool:
    username = input("Username: ")
    # getpass tidak menampilkan input saat mengetik password
    password = getpass.getpass("Password: ")
    if SELLER_CREDENTIALS.get(username) == password:
        print("Login berhasil.\n")
        return True
    print("Login gagal: username atau password salah.\n")
    return False

# Utility function to safely parse integer inputs with optional minimum value       
def input_int(prompt: str, min_val: Optional[int] = None) -> int:
    """Prompt user until a valid integer (>= min_val if given) is entered."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Nilai minimal adalah {min_val}.")
                continue
            return value
        except ValueError:
            print("Input tidak valid. Masukkan angka.")


def select_role() -> str:
    """Let user choose between seller or buyer menu."""
    print("\nSelamat datang di Toko Kelontong Namiya!")
    while True:
        choice = input("Pilih: (1) Penjual, (2) Pembeli: ")
        if choice in ("1", "2"):
            return choice
        print("Pilihan tidak valid.")

# Menampilkan menu untuk seller
# CLI menu loop for sellers to manage products
def seller_menu(store: Store) -> None:
    while True:
        print("\n-- Menu Penjual --")
        print("1. Lihat Katalog")
        print("2. Tambah Produk")
        print("3. Update Harga dan Stok")
        print("4. Hapus Produk")
        print("5. Exit")
        choice = input_int("Pilih opsi: ")

        # Display katalog
        if choice == 1:
            store.display_products()

        # Add product
        elif choice == 2:
            # Loop sampai user memasukkan SKU yang belum ada
            while True:
                sku = input_int("SKU baru: ")
                if sku in store.products:
                    print(f"Error: SKU {sku} sudah ada. Silakan masukkan SKU lain.")
                    continue   # ulangi loop untuk input ulang
                break          # keluar loop jika SKU belum terpakai

            # Setelah dapat SKU unik, lanjut input data lain
            name = input("Nama produk: ")
            category = input("Kategori produk: ")
            price = input_int("Harga produk: ", 1)
            stock = input_int("Stok produk: ", 1)

            # Panggil method Store untuk menambah produk
            store.add_product(sku, name, category, price, stock)
            print(f"Berhasil menambahkan produk '{name}' dengan SKU {sku}.")


        # Update product
        elif choice == 3:
            sku = input_int("SKU produk yang diubah: ")
            price = input_int("Harga baru (-1 untuk tidak ubah): ")
            stock = input_int("Stok baru (-1 untuk tidak ubah): ")
            store.update_product(sku, price if price >= 0 else None, stock if stock >= 0 else None)

        # Remove product
        elif choice == 4:
            sku = input_int("SKU produk yang dihapus: ")
            store.remove_product(sku)

        # Exit program
        elif choice == 5:
            print("Keluar menu penjual.")
            break
        else:
            print("Pilihan tidak valid.")

# Menampilkan menu untuk buyer
# CLI menu loop for buyers: browse, filter, and purchase
def buyer_menu(store: Store) -> None:

    # Minta nama pembeli segera setelah memilih role buyer
    customer_name = ""
    while not customer_name:
        customer_name = input("Masukkan nama Anda: ").strip()
        if not customer_name:
            print("Nama tidak boleh kosong. Silakan coba lagi.")
    print(f"\nHalo, {customer_name}! Selamat datang di menu Pembeli.")

    while True:
        print("\n-- Menu Pembeli --")
        print("1. Lihat Produk")
        print("2. Tambah ke Keranjang")
        print("3. Lihat Keranjang")
        print("4. Checkout")
        print("5. Filter Katalog")
        print("6. Exit")
        choice = input_int("Pilih opsi: ")

        # Display katalog
        if choice == 1:
            store.display_products()

        # Add product to cart
        elif choice == 2:
            sku = input_int("Masukkan SKU produk: ")
            qty = input_int("Masukkan jumlah: ", 1)
            store.add_to_cart(sku, qty)
        
        # View Cart
        elif choice == 3:
            store.view_cart()

        # Checkout
        elif choice == 4:
            total = store.checkout()
            if total > 0:
                bayar = input_int("Masukkan jumlah pembayaran: ")
                if bayar >= total:
                    sisa = bayar - total
                    print(f"Pembayaran sukses. Kembalian: Rp {sisa}")
                else:
                    print(f"Pembayaran kurang: Rp {total - bayar}")

        # Filter Produk
        elif choice == 5:
            kategori     = input("Filter kategori (enter untuk abaikan): ").strip() or None
            min_harga_in = input("Harga minimal (enter untuk abaikan): ").strip()
            max_harga_in = input("Harga maksimal (enter untuk abaikan): ").strip()
            only_in_stock = input("Hanya yang tersedia? (y/N): ").lower().startswith("y")

            # Konversi harga
            min_harga = int(min_harga_in) if min_harga_in.isdigit() else None
            max_harga = int(max_harga_in) if max_harga_in.isdigit() else None

            hasil = store.filter_products(
                kategori=kategori,
                min_harga=min_harga,
                max_harga=max_harga,
                only_in_stock=only_in_stock
            )
            if hasil:
                print("\n>>> Hasil Filter:")
                store.display_products(products=hasil)
            else:
                print("⚠️ Tidak ada produk yang cocok.")

        elif choice == 6:
            print(f"Terima kasih telah berbelanja! Semoga sehat selalu {customer_name}")
            break
        else:
            print("Pilihan tidak valid.")

# Main entry point: setup initial products and launch role selection
def main():
    products = [Product(sku, data["nama"], data["kategori"], data["harga"], data["stok"]) for sku, data in catalog_dict.items()]
    store = Store(products)
    role = select_role()
    if role == "1":
        # autentikasi
        if not authenticate_seller():
            return           # keluar kalau gagal
        seller_menu(store)
    else:
        buyer_menu(store)

if __name__ == "__main__":
    main()