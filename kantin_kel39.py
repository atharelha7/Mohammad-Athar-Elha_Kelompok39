WATERMARK = "Kelompok 39"

def banner() -> None:
    print("=" * 46)
    print(f" Sistem Pemesanan Kantin - {WATERMARK} ")
    print("=" * 46)


def info(msg: str) -> None:
    print(f"[INFO] {msg}")


def default_tax() -> float:
    return 0.05


def hitung_total(subtotal: float, pajak: float) -> float:
    if pajak < 0:
        pajak = 0
    if pajak > 0.5:
        pajak = 0.5
    return subtotal * (1 + pajak)

class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def label(self) -> str:
        return f"{self.name} (Rp{self.price:,.0f})"

    def set_price(self, new_price: float) -> None:
        if new_price < 0:
            new_price = 0
        self.price = new_price


class Cart:
    def __init__(self):
        self.items: list[tuple[MenuItem, int]] = []

    def add(self, item: MenuItem, qty: int) -> None:
        if qty <= 0:
            info("Qty minimal 1.")
            return
        for i, (it, q) in enumerate(self.items):
            if it.name == item.name:
                self.items[i] = (it, q + qty)
                return
        self.items.append((item, qty))

    def list(self) -> None:
        if not self.items:
            print("Keranjang kosong.")
            return
        print("Isi Keranjang:")
        for idx, (it, q) in enumerate(self.items, start=1):
            print(f"[{idx}] {it.label()} x{q} = Rp{it.price*q:,.0f}")

    def subtotal(self) -> float:
        total = 0.0
        for it, q in self.items:
            total += it.price * q
        return total

    def clear(self) -> None:
        self.items.clear()


class Canteen:
    def __init__(self):
        self.menu: list[MenuItem] = []
        self.menu.append(MenuItem("Nasi Goreng", 15000))
        self.menu.append(MenuItem("Mie Ayam", 12000))
        self.menu.append(MenuItem("Es Teh", 5000))
        self.menu.append(MenuItem("Air Mineral", 3000))

    def show_menu(self) -> None:
        if not self.menu:
            print("Menu belum tersedia.")
            return
        print("Menu Kantin:")
        for i, m in enumerate(self.menu, start=1):
            print(f"[{i}] {m.label()}")

    def get_item(self, index: int) -> MenuItem | None:
        if 1 <= index <= len(self.menu):
            return self.menu[index - 1]
        return None

def read_int(prompt: str) -> int:
    while True:
        txt = input(prompt)
        if txt.strip().lstrip("-+").isdigit():
            try:
                return int(txt)
            except ValueError:
                pass
        print("Masukkan bilangan bulat yang valid.")


def read_float(prompt: str) -> float:
    while True:
        txt = input(prompt).replace(",", ".")
        try:
            return float(txt)
        except ValueError:
            print("Masukkan angka yang valid.")

def main():
    banner()
    kantin = Canteen()
    cart = Cart()

    while True:
        print("\nMenu:")
        print("1. Lihat menu kantin")
        print("2. Tambah ke keranjang")
        print("3. Lihat keranjang")
        print("4. Hapus semua (clear)")
        print("5. Hitung total + pajak (default 5%)")
        print("0. Keluar")

        pilih = input("Pilih: ").strip()

        if pilih == "1":
            kantin.show_menu()

        elif pilih == "2":
            kantin.show_menu()
            if not kantin.menu:
                continue
            idx = read_int("Pilih nomor menu: ")
            item = kantin.get_item(idx)
            if item is None:
                print("Nomor menu tidak valid.")
            else:
                qty = read_int("Jumlah: ")
                cart.add(item, qty)
                info("Ditambahkan ke keranjang.")

        elif pilih == "3":
            cart.list()

        elif pilih == "4":
            cart.clear()
            info("Keranjang dikosongkan.")

        elif pilih == "5":
            sub = cart.subtotal()
            pajak = default_tax()
            total = hitung_total(sub, pajak)
            print(f"Subtotal : Rp{sub:,.0f}")
            print(f"Pajak    : {pajak*100:.1f}%")
            print(f"Total    : Rp{total:,.0f}")

        elif pilih == "0":
            print("Terima kasih telah memesan di kantin.")
            break

        else:
            print("Pilihan tidak dikenal, coba lagi.")


if __name__ == "__main__":
    main()


