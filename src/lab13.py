"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D dùng statsmodels nếu có, không có thì dùng statistics.NormalDist)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
Mọi con số tính từ cột *_simulated in kèm nhãn [simulated].
"""
import math
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000   # chi phí cố định của trợ lý, đồng / tháng
YC_THANG = 45_000            # khoảng 45.000 yêu cầu / tháng
PHAM_VI = ['noi_dia', 'hang_nang']
SIM = '[simulated]'


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy.
    = E[số lần chạy] / P(thành công) = 1/p, không phụ thuộc k."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')
    print(f'  E[lần chạy] p=0,8 k=2  = {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'  E[lần chạy] p=0,8 k=∞  = {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'  Hệ số CPS   p=0,8 k=3  = {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, khong_thanh_cong,
    cps (chi phí mỗi việc thành công), hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × lương phút. Số GIẢ LẬP → nhãn simulated.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong' (mẫu số).
    - max_lan_chay: bỏ lần chạy có attempt > giới hạn; yêu cầu có so_lan_chay > giới hạn
      coi là chuyen_nhan_vien, phút xem lại / làm lại = 0.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        khong_thanh_cong=len(reqs) - thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


def in_a2(runs, reqs):
    kq = mo_hinh(runs, reqs)
    print('\n== A2 · Mô hình chi phí từ trace (1.200 yêu cầu) ==')
    nhan = dict(token='đo từ trace', tool='đo từ trace', chay_lai='đo từ trace',
                xem_lai=SIM, lam_lai=SIM, tong='có phần ' + SIM, thanh_cong='',
                khong_thanh_cong='', cps=SIM, hoa_don_moi_yc='đo từ trace')
    for ten, gia_tri in kq.items():
        print(f'{ten:17s} {gia_tri:>14,.1f}  {nhan[ten]}')
    print(f'Số lần gọi tool: {runs.tool_calls.sum():,}; phút xem lại {reqs.phut_xem_lai_simulated.sum():,}, '
          f'phút làm lại {reqs.phut_lam_lai_simulated.sum():,} {SIM}')
    print(f'CPS / hoá đơn mỗi yêu cầu = {kq["cps"] / kq["hoa_don_moi_yc"]:.1f} lần')
    for k in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f'  tỉ trọng {k:8s} {kq[k] / kq["tong"] * 100:5.1f}%')
    print(f'  giờ nhân viên  {(kq["xem_lai"] + kq["lam_lai"]) / kq["tong"] * 100:5.1f}% {SIM}')
    he_thong = kq['tong'] + kq['khong_thanh_cong'] * BASELINE
    print(f'Chi phí cả hệ thống / yêu cầu (cộng {kq["khong_thanh_cong"]} ca nhân viên làm thay): '
          f'{he_thong / len(reqs):,.0f} đ = {he_thong / len(reqs) / BASELINE:.2f}× của 12.000 đ {SIM}')
    return kq


def in_a3(runs, reqs):
    print('\n== A3 · Tách theo loại yêu cầu ==')
    print(f'{"loai":10s} {"n":>5s} {"thành công":>10s} {"lần/yc":>7s} {"CPS [sim]":>10s} {"×12k":>6s}')
    bang = {}
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs.loai == loai]
        kq = mo_hinh(runs, r)
        n_run = runs.request_id.isin(r.request_id).sum()
        bang[loai] = kq
        print(f'{loai:10s} {len(r):5d} {kq["thanh_cong"] / len(r) * 100:9.1f}% {n_run / len(r):7.2f} '
              f'{kq["cps"]:10,.0f} {kq["cps"] / BASELINE:6.2f}')
    # Chạy lại có giúp không: tỉ lệ ok theo lần thử
    m = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    m['ok'] = (m.status == 'ok').astype(float)
    bang_ok = m.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
    so_run = m.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='count')
    print('Tỉ lệ ok theo lần thử (%):')
    print((bang_ok * 100).round(1).to_string())
    print('Số lần chạy theo lần thử:')
    print(so_run.to_string())
    return bang


def in_a4(runs, reqs):
    print('\n== A4 · Chi phí cố định, phạm vi noi_dia + hang_nang ==')
    r = reqs[reqs.loai.isin(PHAM_VI)]
    kq = mo_hinh(runs, r)
    ti_le = kq['thanh_cong'] / len(reqs)          # việc thành công trong phạm vi / 1.200 yêu cầu mẫu
    print(f'Phạm vi: {len(r)} yêu cầu, {kq["thanh_cong"]} việc thành công; tổng {kq["tong"]:,.0f} đ; '
          f'CPS {kq["cps"]:,.0f} đ {SIM}')
    for ten, khoi_luong in [('45.000 yc/tháng', YC_THANG), ('Một nửa khối lượng', YC_THANG / 2)]:
        tc_thang = khoi_luong * ti_le
        co_dinh = CO_DINH_THANG / tc_thang
        tong = kq['cps'] + co_dinh
        print(f'{ten:20s} việc TC/tháng {tc_thang:9,.0f}  cố định/việc {co_dinh:7,.0f}  '
              f'CPS+cố định {tong:7,.0f} = {tong / BASELINE:.2f}× {SIM}')
    return kq


# ---------- Nhiệm vụ B · Độ nhạy ----------
KICH_BAN = {
    'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
    'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
    'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2),
    'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
    'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2),
    'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
    'Lương nhân viên tăng 25%': dict(luong_phut=2500),
    'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
    'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
}


def in_b(runs, reqs):
    goc = mo_hinh(runs, reqs)['cps']
    print('\n== B1 · Đổi từng yếu tố (CPS [simulated]) ==')
    print(f'{"Gốc (A2)":30s} {goc:8,.0f}')
    for ten, kw in KICH_BAN.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:30s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')

    print('\n== B2 · Đổi một cặp ==')
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    rieng = (mo_hinh(runs, reqs, gia_vao=52, gia_ra=260)['cps'] - goc) + \
            (mo_hinh(runs, reqs, he_so_xem_lai=2)['cps'] - goc)
    print(f'Token ×2 + xem lại ×2: {cap:,.0f} đ ({(cap / goc - 1) * 100:+.1f}%); '
          f'tổng hai tác động riêng {rieng / goc * 100:+.1f}% {SIM}')

    print('\n== B3 · Giới hạn số lần chạy: chi phí cả hệ thống ==')
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        he_thong = kq['tong'] + kq['khong_thanh_cong'] * BASELINE
        print(f'{k} lần: trợ lý {kq["tong"]:12,.0f}  không TC {kq["khong_thanh_cong"]:4d}  '
              f'cả hệ thống {he_thong:12,.0f}  CPS {kq["cps"]:7,.0f} {SIM}')


def b4_xem_lai_100(runs, reqs, phut_xem=5, phut_lam_lai=9):
    r = reqs[reqs.loai.isin(PHAM_VI)]
    ru = runs[runs.request_id.isin(r.request_id)]
    co_ok = ru[ru.status == 'ok'].request_id.nunique()
    so_lam_lai = int((r.ket_qua == 'lam_lai').sum())
    tok_tool = (ru.tokens_in / 1000 * GIA_VAO + ru.tokens_out / 1000 * GIA_RA + ru.tool_calls * GIA_TOOL).sum()
    xem = co_ok * phut_xem * LUONG_PHUT
    lam = so_lam_lai * phut_lam_lai * LUONG_PHUT
    tc = int((r.ket_qua == 'thanh_cong').sum())
    tong = tok_tool + xem + lam
    return dict(n=len(r), co_ok=co_ok, so_lam_lai=so_lam_lai, tok_tool=tok_tool, xem=xem, lam=lam,
                tong=tong, thanh_cong=tc, cps=tong / tc)


def in_b4(runs, reqs):
    print('\n== B4 · Xem lại 100% (noi_dia + hang_nang) ==')
    phut_ll_tb = reqs.loc[reqs.ket_qua == 'lam_lai', 'phut_lam_lai_simulated']
    for phut_ll in [9, round(phut_ll_tb.mean(), 1)]:
        kq = b4_xem_lai_100(runs, reqs, phut_lam_lai=phut_ll)
        # hoà vốn: phút xem lại tối đa để CPS ≤ 12.000 đ
        hoa_von = (BASELINE * kq['thanh_cong'] - kq['tok_tool'] - kq['lam']) / (kq['co_ok'] * LUONG_PHUT)
        print(f'làm lại {phut_ll} phút/ca: {kq["co_ok"]} yc có lần ok × 5 phút = {kq["xem"]:,.0f}; '
              f'{kq["so_lam_lai"]} ca làm lại = {kq["lam"]:,.0f}; token+tool {kq["tok_tool"]:,.0f}; '
              f'tổng {kq["tong"]:,.0f} / {kq["thanh_cong"]} = {kq["cps"]:,.0f} đ = {kq["cps"] / BASELINE:.2f}× '
              f'(hoà vốn ≤ {hoa_von:.1f} phút xem lại) {SIM}')
    print(f'Phút làm lại thực tế mỗi ca lam_lai: TB {phut_ll_tb.mean():.1f}, trung vị {phut_ll_tb.median():.1f} {SIM}')


# ---------- Nhiệm vụ D · Cỡ mẫu ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=0.02):
    return 1 + (m - 1) * icc


def power_hai_ti_le(p1, p2, n, alpha=0.05):
    """Power theo Cohen's h (giống statsmodels NormalIndPower + proportion_effectsize)."""
    try:
        from statsmodels.stats.power import NormalIndPower
        from statsmodels.stats.proportion import proportion_effectsize
        return NormalIndPower().power(proportion_effectsize(p2, p1), nobs1=n, alpha=alpha, ratio=1)
    except ImportError:
        h = abs(2 * math.asin(math.sqrt(p2)) - 2 * math.asin(math.sqrt(p1)))
        z = NormalDist().inv_cdf(1 - alpha / 2)
        se = math.sqrt(2 / n)
        return NormalDist().cdf(h / se - z) + NormalDist().cdf(-h / se - z)


def in_d(reqs, icc=0.02):
    print('\n== D1 · Cỡ mẫu (baseline 0,70; alpha 0,05; power 0,8; ICC 0,02) ==')
    n5 = co_mau(0.70, 0.75)
    print(f'a) Chia theo yêu cầu: {n5:,} yêu cầu mỗi nhóm')
    de75 = he_so_thiet_ke(75, icc)
    n_b = math.ceil(n5 * de75)
    print(f'b) Theo nhân viên m=75: DE = {de75:.2f}; n = {n_b:,} mỗi nhóm → {math.ceil(n_b / 75)} người/nhóm, '
          f'tổng {2 * math.ceil(n_b / 75)} > 40 → không đủ người')
    print(f'c) 20 nhân viên/nhóm: hiệu dụng tối đa c/ICC = {20 / icc:,.0f} < {n5:,} → không đạt')
    print(f'd) 6 depot/nhóm: hiệu dụng tối đa {6 / icc:,.0f}')
    n6 = co_mau(0.70, 0.76)
    # 20m / (1 + (m-1)icc) ≥ n6  →  m ≥ n6(1-icc) / (20 - n6·icc)
    m_min = math.ceil(n6 * (1 - icc) / (20 - n6 * icc))
    print(f'e) Mức chênh 6 điểm: {n6:,} mỗi nhóm; 20 người/nhóm cần m ≥ {m_min} yêu cầu/người '
          f'(DE {he_so_thiet_ke(m_min, icc):.2f}; hiệu dụng {20 * m_min / he_so_thiet_ke(m_min, icc):,.0f})')
    print(f'Power nếu tác động thật chỉ 5 điểm với n hiệu dụng {n6}: {power_hai_ti_le(0.70, 0.75, n6):.2f}')
    print('\n== D3 · Tỉ lệ mở lại 7 ngày hiện tại ==')
    r = reqs[reqs.loai.isin(PHAM_VI)]
    print(f'Toàn mẫu: {reqs.mo_lai_trong_7_ngay.mean() * 100:.2f}% ({reqs.mo_lai_trong_7_ngay.sum()}/{len(reqs)}); '
          f'noi_dia+hang_nang: {r.mo_lai_trong_7_ngay.mean() * 100:.2f}% ({r.mo_lai_trong_7_ngay.sum()}/{len(r)})')
    print(f'Tỉ lệ lam_lai trong phạm vi: {(r.ket_qua == "lam_lai").mean() * 100:.1f}% '
          f'({(r.ket_qua == "lam_lai").sum()}/{len(r)})')
    print(f'Nhân viên trong mẫu: {reqs.staff_id.nunique()}; depot: {reqs.depot.nunique()}; '
          f'yêu cầu/nhân viên trung bình: {len(reqs) / reqs.staff_id.nunique():.1f}')


# ---------- Nhiệm vụ E1 · Chỉ số ----------
def in_e(reqs):
    print('\n== E1 · Tính thử ba chỉ số trên 1.200 yêu cầu ==')
    chinh = (reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0)
    xem = reqs[reqs.duoc_xem_lai == 1]
    bo_qua = xem.quyet_dinh_xem_lai.isin(['sua', 'bo'])
    an_toan = reqs.mo_lai_trong_7_ngay == 1
    print(f'Chính: {chinh.mean() * 100:.2f}% ({chinh.sum()}/{len(reqs)})')
    print(f'Dùng (bỏ qua gợi ý): {bo_qua.mean() * 100:.2f}% ({bo_qua.sum()}/{len(xem)})')
    print(f'An toàn (mở lại 7 ngày): {an_toan.mean() * 100:.2f}% ({an_toan.sum()}/{len(reqs)})')
    print(f'Tỉ lệ được xem lại: {len(xem) / len(reqs) * 100:.1f}% ({len(xem)}/{len(reqs)})')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_a2(runs, reqs)        # CP1 · A2
    in_a3(runs, reqs)        # CP1 · A3
    in_a4(runs, reqs)        # CP1 · A4
    in_b(runs, reqs)         # CP2 · B1, B2, B3
    in_b4(runs, reqs)        # CP2 · B4
    in_d(reqs)               # CP4 · D1, D3
    in_e(reqs)               # CP5 · E1
