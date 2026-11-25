# Báo cáo cá nhân — DoThiThuHang-MSSV

> Đổi tên file thành `<MSSV>_DoThiThuHang.md` và điền MSSV, email ở mục 1 trước khi nộp. File mẫu `MSSV_HoTen.md` giữ nguyên.

## 1. Thông tin thành viên

- Họ tên: Đỗ Thị Thu Hằng
- MSSV: 2A202603840
- Email: dothuhang2604@gmail.com
- Vai trong nhóm: làm cá nhân, đảm nhận cả bốn vai (người viết code, người kiểm số, người gắn nhãn, người giữ hồ sơ)

## 2. Phần việc phụ trách

Toàn bộ Lab 13: mô hình chi phí (A), bảng độ nhạy (B), bảng lỗi (C), kế hoạch pilot (D), chỉ số, rủi ro và hồ sơ launch v0 (E), cùng `TEAM.md`, `group_report.md`.

## 3. Đóng góp cụ thể

- **A:** viết ba hàm A1 theo công thức E[số lần chạy] = (1 − (1 − p)^k)/p; hàm `mo_hinh` cộng token + tool trên **mọi** lần chạy (kể cả lần lỗi), cộng phút xem lại / làm lại × 2.000 đ, rồi chia cho số việc `thanh_cong`. Kết quả: 4.472 đ/việc, gấp 16,3× hoá đơn token chia số yêu cầu [simulated]. Tách theo loại để chọn phạm vi noi_dia + hang_nang (0,22× và 0,69×) và loại quoc_te (1,88×, lần chạy thứ 3 chỉ đúng 2,2%) [simulated].
- **B:** chín kịch bản độ nhạy, xếp hạng làm lại (+51,8%) > xem lại (+40,7%) > lương (+23,1%) [simulated]. Chỉ ra giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ), khác với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần) [simulated]. Phát hiện dữ liệu làm lại trung bình 15,3 phút chứ không phải 9 phút, khiến xem lại 100% thành 1,03× [simulated].
- **C:** gắn nhãn 20 ca theo nguyên nhân gốc, khớp bảng tham khảo 20/20; bảng khắc phục 5 ca có ngưỡng đo được.
- **D:** tính năm câu D1, chọn chia theo nhân viên 20 + 20 với MDE 6 điểm và ghi rõ đánh đổi (power 0,64 nếu tác động thật là 5 điểm); đặt ngưỡng an toàn so với đối chứng vì tỉ lệ mở lại hiện tại 3,97% đã vượt mức 3%.
- **E:** đặc tả 5 chỉ số, 10 event có trace_id, 4 dòng rủi ro, hồ sơ bảy mục với đề xuất Go có điều kiện.

## 4. Bằng chứng

- `src/lab13.py`: chạy `cd src && python3 lab13.py` in ba phép thử ĐẠT và toàn bộ bảng A2, A3, A4, B1–B4, D1, E1.
- `report/team/bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`, `phieu_cham.md`, `group_report.md`.
- Số kiểm tay: 4.373.585 ÷ 978 = 4.472 đ; (4.373.585 + 222 × 12.000) ÷ 1.200 = 5.865 đ; D1e: 2,82m ≥ 841,82 → m ≥ 299.

## 5. Công cụ AI đã dùng

- **Claude (Anthropic):** hỗ trợ viết code `lab13.py`, soạn nháp các file hồ sơ và gắn nháp nhãn 20 ca kèm lý do.
- **Cách tự kiểm tra:**
  - Chạy ba phép thử A1 trước khi tính tiếp.
  - Đối chiếu từng số A2, A3, B1–B4, D1, E1 với bảng số trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`; tất cả lệch dưới 2% (B4 với 15,3 phút ra 12.415 đ so với 12.414 đ, do làm tròn).
  - Kiểm tra quy tắc "giảm một nửa = nửa mức tăng của gấp đôi" ở B1, và B2 bằng tổng hai tác động riêng.
  - Tính tay ba con số ở mục 4.
  - Rà lại từng nhãn lỗi theo năm câu hỏi nhận diện của PAIR trước khi so với bảng tham khảo.
  - Chạy `yaml.safe_load`, `grep` dấu `?` và lệnh grep kiểm tra từ bị cấm theo quy tắc 5.
- Mọi con số trong hồ sơ đều do `lab13.py` tính ra hoặc tính tay có ghi cách tính, không lấy số do AI tự đưa ra.

## 6. Tự đánh giá

- **Làm tốt:** A, B, D khớp đáp án; hồ sơ nêu rõ các con số bất lợi (xem lại 100% thì 1,03×, power 0,64) thay vì chỉ nêu số đẹp; mọi số giả lập có nhãn.
- **Hạn chế:** làm một mình nên không có hai người gắn nhãn độc lập ở C và không có duyệt chéo Gate 2a; phần này được thay bằng bộ nhãn có lý do và tự rà theo thang hội đồng, nên có thể bị trừ điểm C3 và C6–C8.
- **Hiểu được:**
  - Tử số tính mọi lần chạy vì lần lỗi vẫn tốn tiền, còn mẫu số chỉ đếm việc thành công.
  - Khi chia theo cụm, số cụm quyết định cỡ mẫu hiệu dụng (tối đa c ÷ ICC), không phải tổng số yêu cầu.
  - Chỉ được viết "chỉ số trong đợt chạy thử là…" vì đợt chạy thử không có đối chứng.
