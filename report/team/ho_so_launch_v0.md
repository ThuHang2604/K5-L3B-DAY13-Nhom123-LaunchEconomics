# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot.

Nhóm: Nhom123 (làm cá nhân: Đỗ Thị Thu Hằng) · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc toàn mẫu, gấp 16,3× hoá đơn token chia số yêu cầu (274,7 đ); phạm vi noi_dia + hang_nang 3.414 đ, cộng cố định 4.599 đ (45.000 yc/tháng) hoặc 5.784 đ (nửa khối lượng) [simulated]. Làm lại chiếm 51,8%, xem lại 40,7% | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. số ca làm lại ±51,8% · 2. tỉ lệ xem lại ±40,7% · 3. lương +23,1%; giá token gấp đôi chỉ +5,6%. Giới hạn 2 lần chạy rẻ nhất cho công ty: 6.901.220 đ [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ (đã cộng 222 ca nhân viên làm thay). Theo loại: noi_dia 0,22× · hang_nang 0,69× · doi_tac 0,85× · quoc_te 1,88×. **Bất lợi:** xem lại 100% thì 0,98×, và 1,03× với 15,3 phút làm lại như dữ liệu [simulated] | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · mở lại 7 ngày 4,25% (51/1.200), trong phạm vi 3,97%. 10 event có trace_id; cả 5 chỉ số tính được từ event | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, 5 loại PAIR (ND 4 · HT 5 · NC 4 · GH 4 · NG 3); bộ nhãn khớp bảng tham khảo 20/20 (làm cá nhân, không có hai người gắn nhãn độc lập). 5 dòng khắc phục có ngưỡng đo được; nặng nhất là ca 7 (báo đã hoàn khi sổ cái 503) và ca 20 (hoàn trùng) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot; MDE 6 điểm, n hiệu dụng 859/nhóm, DE 6,96, ≥ 299 yc/người. **Bất lợi:** không đủ mẫu cho 5 điểm (tối đa 1.000 < 1.251), power 0,64 nếu tác động thật 5 điểm. 4 luật dừng; ngày quyết định 2027-01-05 | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi → 6.787 đ (+51,8%); xem lại 100% → 0,98–1,03×; nửa khối lượng → +2.370 đ/việc cố định; lương +25% → 5.506 đ [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot chỉ noi_dia + hang_nang (loại quoc_te 1,88× và doi_tac 0,85× [simulated]). Lý do: phạm vi này 0,38–0,48× chi phí nhân viên kể cả cố định [simulated], nhưng lợi thế biến mất nếu phải xem lại 100% (1,03×) và pilot chỉ đủ mẫu cho mức chênh 6 điểm. Điều kiện:

- Sửa khoá chống trùng (ca 20) và đối soát sổ cái, chỉ báo "đã hoàn" khi sổ cái trả ok (ca 7); kiểm thử bằng 0 ca lệch trong 1 ngày chạy thử. Phụ trách: Kỹ sư trưởng agent · kiểm tra 2026-11-30.
- Ký chấp nhận MDE 6 điểm (power 0,64 nếu tác động thật 5 điểm) và chốt seed bốc thăm. Phụ trách: Giám đốc vận hành LogiX-VN · kiểm tra 2026-11-30.
- Bật đủ 10 event có trace_id; thay phút simulated bằng phút đo thật và tính lại chi phí mỗi việc thành công sau tuần 1. Phụ trách: PM trợ lý hoàn phí · kiểm tra 2026-12-08.
- Kế hoạch giảm xem lại theo bậc (khi sửa + bỏ < 15%) và mục tiêu ≤ 5 phút/lần xem lại, vì xem lại 100% không tiết kiệm. Phụ trách: Trưởng nhóm CSKH · kiểm tra 2026-12-15.
