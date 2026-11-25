## 1. Thông tin nhóm

- Tên nhóm: Nhom123
- Lớp: L3B
- Thành viên: Đỗ Thị Thu Hằng (làm cá nhân), xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để Gate 2a duyệt kế hoạch pilot, trả lời bốn câu: có đáng chạy, nhân viên có dùng, khi hỏng thì sao, pilot có ra được quyết định không. Mọi số do `src/lab13.py` tính trên hai file CSV giả lập; số từ cột `_simulated` ghi nhãn simulated. Mỗi nhiệm vụ dùng lại số của nhiệm vụ trước: A3 chọn phạm vi, B cho rủi ro và luật dừng, D3 cho ngưỡng an toàn.

## 3. Giải pháp

- **A** ([bang_chi_phi.md](bang_chi_phi.md)): ba hàm A1 theo công thức (1 − (1 − p)^k)/p; `mo_hinh` cộng token + tool trên mọi lần chạy (kể cả lỗi), cộng phút xem lại / làm lại × 2.000 đ, chia cho số việc `thanh_cong`. Gọi lại theo `loai` (A3) và cộng cố định 40 triệu/tháng (A4).
- **B** ([bang_chi_phi.md](bang_chi_phi.md)): gọi lại `mo_hinh` với tham số đổi cho 9 kịch bản, một cặp, giới hạn 1/2/3 lần chạy và chi phí cả hệ thống, xem lại 100% cho phạm vi pilot.
- **C** ([bang_loi.md](bang_loi.md)): gắn nhãn 20 ca theo năm loại PAIR kèm lý do từng ca, chốt trước rồi mới so với bảng tham khảo (khớp 20/20), quy tắc phân biệt theo nguyên nhân gốc, bảng khắc phục 5 ca có ngưỡng đo được và một vai trò phụ trách.
- **D** ([pilot_plan.yaml](pilot_plan.yaml)): tính năm câu D1 trước, chọn chia theo nhân viên 20 + 20 với MDE 6 điểm, kiểm tra năm câu D2, đặt bốn luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ.
- **E** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): tính thử ba chỉ số, 10 event có trace_id, bốn dòng rủi ro kinh tế, hồ sơ bảy mục.

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ**, gấp **16,3×** hoá đơn token chia số yêu cầu; làm lại chiếm 51,8% [simulated].
- Cả hệ thống **5.865 đ/yêu cầu = 0,49×** của 12.000 đ [simulated]. Theo loại: noi_dia 0,22× · hang_nang 0,69× · doi_tac 0,85× · quoc_te 1,88× [simulated]; quoc_te chạy lại lần 3 chỉ đúng 2,2%.
- Yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương (+23,1%) [simulated]. Giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ) [simulated].
- Con số bất lợi: xem lại 100% → 0,98× (1,03× với 15,3 phút làm lại) [simulated]; pilot 20 + 20 nhân viên chỉ đủ mẫu cho mức chênh 6 điểm, power 0,64 ở mức 5 điểm.
- Chỉ số trong đợt chạy thử: chính 82,83% · bỏ qua gợi ý 27,12% · mở lại 7 ngày 4,25%.
- **Đề xuất: Go có điều kiện** cho pilot noi_dia + hang_nang, bốn điều kiện có người phụ trách và ngày kiểm tra.
- Duyệt chéo: chưa có, vì làm cá nhân nên không có nhóm hội đồng và nhóm n + 1. Thay bằng tự rà theo thang hội đồng trong [phieu_cham.md](phieu_cham.md).

## 5. Khó khăn và cách xử lý

- Làm một mình nên không đáp ứng được hai yêu cầu dành cho nhóm: hai người gắn nhãn độc lập (C) và duyệt chéo Gate 2a. Xử lý: chốt bộ nhãn kèm lý do trước khi so với bảng tham khảo, ghi rõ đây không phải đồng thuận giữa hai người; phiếu chấm để trống và thay bằng tự rà theo thang hội đồng.
- Môi trường làm bài không cài được `statsmodels` (không có mạng); D1 tính bằng `statistics.NormalDist` với cùng công thức, power tính theo Cohen's h giống `NormalIndPower`. Code tự dùng statsmodels nếu máy có.

- So sánh 4.472 đ với 12.000 đ dễ gây hiểu nhầm vì 4.472 đ chưa tính 222 ca nhân viên làm thay; nhóm thêm chỉ số chi phí cả hệ thống 5.865 đ/yêu cầu.
- Đề cho 9 phút làm lại nhưng dữ liệu trung bình 15,3 phút/ca; nhóm báo cả hai kết quả B4 và mức hoà vốn 5,1 / 4,8 phút.
- Không có cách chia nào đủ mẫu cho 5 điểm với 40 nhân viên; nhóm chọn MDE 6 điểm và ghi power 0,64 là con số bất lợi.
- Ngưỡng an toàn tuyệt đối 3% sẽ dừng pilot ngay tuần đầu (hiện 3,97% trong phạm vi); nhóm đổi sang chênh so với đối chứng ≥ 2 điểm kèm trần 6%.

## 6. Tổng hợp đóng góp

Toàn bộ bài do Đỗ Thị Thu Hằng làm, đảm nhận cả bốn vai. Chi tiết trong `TEAM.md` và báo cáo cá nhân.

## 7. Hạn chế và hướng cải thiện

- Chi phí xem lại / làm lại dựa trên phút giả lập; cần thay bằng phút đo thật từ `staff_review_decision` và `staff_rework_completed` sau tuần 1.
- Mẫu 1.200 yêu cầu chỉ có 20 nhân viên, 6 depot; ICC 0,02 là giả định, cần ước lượng lại từ dữ liệu pilot.
- Mô hình cộng tuyến tính, chưa mô tả tương tác (ví dụ giảm xem lại có thể làm tăng làm lại).

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu statsmodels, `stats.power.NormalIndPower`.
- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, `docs/du_lieu_va_cong_thuc.md`.
