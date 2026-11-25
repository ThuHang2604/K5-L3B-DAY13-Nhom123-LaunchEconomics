# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

> **Ghi chú làm cá nhân:** lab này do một người làm (Đỗ Thị Thu Hằng), nên không có hai người gắn nhãn độc lập như đề yêu cầu. Thay vào đó:
> - **Bộ nhãn 1:** gắn theo nguyên nhân gốc, mỗi ca kèm một câu lý do. Bộ này làm với sự hỗ trợ của trợ lý AI (Claude) rồi tự rà lại từng ca theo năm câu hỏi nhận diện, và được chốt **trước** khi so với bảng tham khảo.
> - **Bộ nhãn 2:** bảng "Nhãn tham khảo cho 20 ca" trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
>
> Tỉ lệ dưới đây là mức khớp giữa bộ nhãn 1 và bảng tham khảo, không phải đồng thuận giữa hai người gắn nhãn độc lập.

Viết tắt: ND = Do người dùng · HT = Hệ thống · NC = Ngữ cảnh · GH = Giới hạn hệ thống · NG = Ngầm.

## Hai bộ nhãn

| Ca | Tóm tắt | Bộ nhãn 1 | Lý do (nguyên nhân gốc) | Bộ nhãn 2 (tham khảo) | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- | --- | --- |
| 1 | Khách nhập số tài khoản thiếu 2 chữ số | ND | Đầu vào của khách sai; trợ lý chỉ làm theo | ND | Có | ND |
| 2 | Hàng nặng 28 kg tra giá hàng thường, hoàn thiếu 45.000 đ, khách mở lại | HT | Trợ lý gọi tool sai tham số, vi phạm chính sách, khách đã thấy | HT | Có | HT |
| 3 | Hoàn về ví LogiX đúng thiết kế, khách chờ tiền về ngân hàng | NC | Làm đúng thiết kế, giả định "khách biết tiền về ví" không khớp | NC | Có | NC |
| 4 | Chặng do hãng nước ngoài giao, LogiX không có dữ liệu | GH | Thiếu dữ liệu, không thể trả lời dù có cố | GH | Có | GH |
| 5 | 14 đơn có mã giảm giá hoàn theo giá trước giảm, không ai báo | NG | Sai tiền nhưng chỉ lộ qua kiểm tra mẫu | NG | Có | NG |
| 6 | Khách chọn "giao trễ" nhưng mô tả hàng vỡ | ND | Khách chọn sai mục; việc trợ lý không đọc mô tả thuộc cột khắc phục | ND | Có | ND |
| 7 | Sổ cái 503, trợ lý vẫn báo "đã hoàn thành công" | HT | Trợ lý báo sai trạng thái so với thiết kế | HT | Có | HT |
| 8 | Dẫn "Điều 7.2" không tồn tại, số tiền vẫn đúng | HT | Trích dẫn sai nhìn thấy được (đã lộ), nên không phải ngầm | HT | Có | HT |
| 9 | Khách nhập mã đơn sàn TMĐT thay mã vận đơn | ND | Đầu vào của khách sai; thiếu gợi ý là việc cải thiện | ND | Có | ND |
| 10 | Từ chối vì bất khả kháng đúng chính sách, app hiện "cam kết 24 giờ" | NC | Đúng chính sách, khách thấy vô lý vì thông điệp app không khớp | NC | Có | NC |
| 11 | Tin nhắn thoại 40 giây, trợ lý không xử lý âm thanh | GH | Đầu vào hệ thống không xử lý được | GH | Có | GH |
| 12 | Tool D05 thiếu trường, token gấp 3 lần suốt 3 tuần | NG | Kết quả đúng nhưng sai về chi phí, không ai thấy | NG | Có | NG |
| 13 | Hỏi hoàn phí bảo hiểm đối tác, ngoài phạm vi | GH | Ngoài phạm vi là giới hạn, kể cả khi trợ lý báo giới hạn kém | GH | Có | GH |
| 14 | Khách bấm nhầm "Xác nhận đã nhận tiền" | ND | Thao tác sai của khách | ND | Có | ND |
| 15 | Trễ 26 giờ, chính sách 50%, trợ lý tính 100%, nhân viên bắt được | HT | Vi phạm chính sách, đã lộ khi xem lại nên không phải ngầm | HT | Có | HT |
| 16 | Gửi Zalo lúc 2:14 sáng theo thiết kế "gửi ngay" | NC | Đúng thiết kế, giả định giờ gửi không khớp hoàn cảnh khách | NC | Có | NC |
| 17 | Bảng giá cũ trong bộ nhớ đệm, 212 đơn lệch 1.000–2.000 đ, không ai mở lại | NG | Sai tiền, không khách nào và không cảnh báo nào nhận ra | NG | Có | NG |
| 18 | Hoàn đúng 15.000 đ nhưng không ghi cách tính, khách mở lại | NC | Số tiền đúng, chỉ giả định "khách hiểu cách tính" là sai | NC | Có | NC |
| 19 | Đơn 14 tháng trước, trợ lý chỉ truy được 12 tháng | GH | Thiếu dữ liệu; trợ lý xử lý đúng (báo rõ, chuyển kèm tóm tắt) | GH | Có | GH |
| 20 | Khách gửi lại sau 10 phút, hoàn hai lần vì không có khoá chống trùng | HT | Lỗi thiết kế hệ thống (thiếu idempotency), không phải lỗi khách | HT | Có | HT |

**Tỉ lệ khớp:** 20 / 20 = 100% (ngưỡng đề là ≥ 16/20 = 80%).

Phân bố: ND 4 (1, 6, 9, 14) · HT 5 (2, 7, 8, 15, 20) · NC 4 (3, 10, 16, 18) · GH 4 (4, 11, 13, 19) · NG 3 (5, 12, 17).

## Quy tắc phân biệt cho các ca dễ lẫn

Không có ca nào lệch giữa hai bộ nhãn. Dưới đây là các quy tắc đã dùng để tách những ca dễ lẫn:

- **Ca 6, 9, 20: gốc ở đâu?** Khách chọn sai mục hoặc nhập sai mã thì là Do người dùng (6, 9). Khách gửi lại sau 10 phút là hành vi bình thường, lỗi nằm ở việc hệ thống thiếu khoá chống trùng, nên là Hệ thống (20).
- **Ca 13 là Giới hạn:** ngoài phạm vi thì là giới hạn, kể cả khi trợ lý báo giới hạn kém.
- **Ca 8, 15 là Hệ thống, không phải Ngầm:** sai đã lộ ra (trích dẫn nhìn thấy được; nhân viên bắt được). Ngầm chỉ dùng khi không ai nhận ra cho tới lúc kiểm tra mẫu (5, 17).
- **Ca 3, 10, 16, 18 là Ngữ cảnh:** kết quả đúng thiết kế hoặc chính sách, chỉ giả định về hiểu biết hay hoàn cảnh của khách là không khớp.
- **Ca 12 là Ngầm:** "sai" có thể là sai về chi phí, không chỉ về câu trả lời.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (reason = ma_khong_hop_le, trace_id); cảnh báo khi > 2% số yêu cầu/ngày | Nhận diện mẫu mã đơn sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh chỗ tìm mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin "đã hoàn" không có bản ghi `refund_ledger_write` = ok cùng trace_id; ngưỡng **0 ca** | Chỉ báo "đã hoàn" khi sổ cái trả ok; 503 sau 3 lần thì báo "đang xử lý" và `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` với reason = so_tien mà `audit_sample_checked` thấy đúng, tính theo tuần; cảnh báo > 0,5% số ca đóng | Mẫu tin nhắn luôn ghi cách tính: "30.000 đ × 50% = 15.000 đ" kèm điều khoản áp dụng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với reason = thieu_du_lieu, đếm theo loại yêu cầu mỗi tuần (quoc_te đang thành công 27,3%) | Giữ cách chuyển nhân viên kèm tóm tắt; đưa quoc_te ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | `audit_sample_checked`: kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới; ghi phiên bản bảng giá vào trace; truy hoàn 212 đơn lệch | Kế toán trưởng |
