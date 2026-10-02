danh_sach_sinh_vien = [
    {
        "ma_sv": "SV01",
        "ten_sv": "Nguyen Van A",
        "gioi_tinh": "Nam",
        "diem_tb": 8.5,
    },
    {
        "ma_sv": "SV02",
        "ten_sv": "Ngyen Thi B",
        "gioi_tinh": "Nu",
        "diem_tb": 6.8,
    },
    {
        "ma_sv": "SV03",
        "ten_sv": "Le Van C",
        "gioi_tinh": "Nam",
        "diem_tb": 4.5,
    },
]


def xep_loai_sinh_vien(diem_tb):
    if diem_tb >= 8.5:
        return "Xuat sac"
    elif diem_tb >= 7.0:
        return "Kha"
    elif diem_tb >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"


def tim_sv_theo_ma(ma_sv):
    for sv in danh_sach_sinh_vien:
        if sv["ma_sv"] == ma_sv:
            return sv
    return None


def hien_thi_danh_sach():
    if len(danh_sach_sinh_vien) == 0:
        print("-> Danh sach sinh vien hien dang rong.")
        return
    print("\n" + "=" * 65)
    print(
        f"{'Ma SV':<10}{'Ho va Ten':<20}{'Gioi tinh':<12}{'Diem TB':<10}{'Xep loai':<13}"
    )
    print("-" * 65)
    for sv in danh_sach_sinh_vien:
        xep_loai = xep_loai_sinh_vien(sv["diem_tb"])
        print(
            f"{sv['ma_sv']:<10}{sv['ten_sv']:<20}{sv['gioi_tinh']:<12}"
            f"{sv['diem_tb']:<10.1f}{xep_loai:<13}"
        )
    print("=" * 65)


def them_sinh_vien(ma_sv, ten_sv, gioi_tinh, diem_tb):
    if tim_sv_theo_ma(ma_sv) is not None:
        print(f"-> Ma sinh vien {ma_sv} da ton tai, khong the them.")
        return
    danh_sach_sinh_vien.append(
        {
            "ma_sv": ma_sv,
            "ten_sv": ten_sv,
            "gioi_tinh": gioi_tinh,
            "diem_tb": diem_tb,
        }
    )
    print(f"-> Da them sinh vien {ten_sv} ({ma_sv}) thanh cong.")


def sua_sinh_vien(ma_sv):
    sv = tim_sv_theo_ma(ma_sv)
    if sv is None:
        print(f"-> Khong tim thay sinh vien co ma {ma_sv}.")
        return

    print(f"\n--- CAP NHAT THONG TIN SV: {sv['ten_sv']} ({ma_sv}) ---")
    ten_moi = input(
        f"Nhap ten moi (de ngoang va Nhan Enter de giu nguyen '{sv['ten_sv']}'): "
    ).strip()
    if ten_moi != "":
        sv["ten_sv"] = ten_moi.title()

    gioi_tinh_moi = input(
        f"Nhap gioi tinh moi (Nam/Nu) (Nhan Enter de giu nguyen '{sv['gioi_tinh']}'): "
    ).strip()
    if gioi_tinh_moi != "":
        sv["gioi_tinh"] = gioi_tinh_moi.title()

    diem_nhap = input(
        f"Nhap diem TB moi (Nhan Enter de giu nguyen '{sv['diem_tb']}'): "
    ).strip()
    if diem_nhap != "":
        try:
            diem_moi = float(diem_nhap)
            if 0 <= diem_moi <= 10:
                sv["diem_tb"] = diem_moi
            else:
                print("-> Diem khong hop le (phai tu 0-10). Giu nguyen diem cu.")
        except ValueError:
            print("-> Du lieu diem khong hop le. Giu nguyen diem cu.")

    print(f"-> Da cap nhat thong tin sinh vien {ma_sv} thanh cong.")


def xoa_sinh_vien(ma_sv):
    sv = tim_sv_theo_ma(ma_sv)
    if sv is None:
        print(f"-> Khong tim thay sinh vien co ma {ma_sv}.")
        return
    danh_sach_sinh_vien.remove(sv)
    print(f"-> Da xoa sinh vien {sv['ten_sv']} ({ma_sv}) khoi danh sach.")


def tim_kiem_sinh_vien():
    tu_khoa = (
        input("Nhap ma sinh vien hoac ten sinh vien can tim: ").strip().lower()
    )
    ket_qua = [
        sv
        for sv in danh_sach_sinh_vien
        if tu_khoa in sv["ma_sv"].lower() or tu_khoa in sv["ten_sv"].lower()
    ]

    if len(ket_qua) == 0:
        print(f"-> Khong tim thay sinh vien nao phu hop voi từ khóa '{tu_khoa}'.")
        return

    print(f"\nKET QUA TIM KIEM (Tim thay {len(ket_qua)} sinh vien):")
    print("-" * 65)
    for sv in ket_qua:
        xep_loai = xep_loai_sinh_vien(sv["diem_tb"])
        print(
            f"  {sv['ma_sv']} - {sv['ten_sv']} - Gioi tinh: {sv['gioi_tinh']} - "
            f"Diem TB: {sv['diem_tb']} - Xep loai: {xep_loai}"
        )


def thong_ke_diem():
    if len(danh_sach_sinh_vien) == 0:
        print("-> Chua co sinh vien nao de thong ke.")
        return

    tong_diem = sum(sv["diem_tb"] for sv in danh_sach_sinh_vien)
    diem_tb_chung = tong_diem / len(danh_sach_sinh_vien)

    thong_ke_xl = {"Xuat sac": 0, "Kha": 0, "Trung binh": 0, "Yeu": 0}
    for sv in danh_sach_sinh_vien:
        xl = xep_loai_sinh_vien(sv["diem_tb"])
        thong_ke_xl[xl] += 1

    print("\n" + "=" * 40)
    print("THONG KE DIEM VA XEP LOAI SINH VIEN")
    print("=" * 40)
    print(f"Tong so sinh vien: {len(danh_sach_sinh_vien)}")
    print(f"Diem trung binh chung: {diem_tb_chung:.2f}")
    print("-" * 40)
    print("Co cau xep loai:")
    for loai, so_luong in thong_ke_xl.items():
        ty_le = (so_luong / len(danh_sach_sinh_vien)) * 100
        print(f"  - {loai:<12}: {so_luong} sinh vien ({ty_le:.1f}%)")


def nhap_diem_thuc(loi_nhac):
    while True:
        try:
            diem = float(input(loi_nhac))
            if 0 <= diem <= 10:
                return diem
            print("-> Diem phai trong khoang tu 0 den 10.")
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so thực.")


def hien_thi_menu():
    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Hien thi danh sach sinh vien")
    print("2. Them sinh vien moi")
    print("3. Sua thong tin sinh vien")
    print("4. Xoa sinh vien")
    print("5. Tim kiem sinh vien")
    print("6. Thong ke diem va xep loai")
    print("0. Thoat chuong trinh")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach()
        elif lua_chon == "2":
            ma_sv = input("Nhap ma sinh vien moi: ").strip().upper()
            ten_sv = input("Nhap ho va ten: ").strip().title()
            gioi_tinh = input("Nhap gioi tinh (Nam/Nu): ").strip().title()
            diem_tb = nhap_diem_thuc("Nhap diem trung binh (0 - 10): ")
            them_sinh_vien(ma_sv, ten_sv, gioi_tinh, diem_tb)
        elif lua_chon == "3":
            ma_sv = input("Nhap ma sinh vien can sua: ").strip().upper()
            sua_sinh_vien(ma_sv)
        elif lua_chon == "4":
            ma_sv = input("Nhap ma sinh vien can xoa: ").strip().upper()
            xoa_sinh_vien(ma_sv)
        elif lua_chon == "5":
            tim_kiem_sinh_vien()
        elif lua_chon == "6":
            thong_ke_doanh_thu_tam = thong_ke_diem()
        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    chay_chuong_trinh()