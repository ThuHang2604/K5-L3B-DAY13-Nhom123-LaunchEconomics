# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Số tính bằng `src/lab13.py` (hàm `in_e`). Ba chỉ số dưới đây tính từ cột thật (không phải `_simulated`).

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200); trong phạm vi noi_dia + hang_nang 3,97% (39/982) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm can thiệp được mở bằng trợ lý | Số `refund_request_created` (arm = can_thiep) có ít nhất một `agent_suggestion_shown` cùng trace_id, chia tổng `refund_request_created` của nhóm can thiệp | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số `audit_sample_checked` có `so_tien_da_hoan ≠ so_tien_dung`, chia số đơn được kiểm tra trong tuần (100 đơn/tuần) | Không cần tính |

Chỉ số chính trong đợt chạy thử là 82,83%. Đợt chạy thử không có nhóm đối chứng, nên con số này không cho biết trợ lý làm chỉ số thay đổi bao nhiêu so với baseline 0,70; pilot có đối chứng mới trả lời được.

## Danh sách event

Mười event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, depot, staff_id, arm, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), trace_id | Khi bấm gửi / sửa / bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ hoàn tiền |
| `handoff_to_staff` | Agent | reason (thieu_du_lieu, ngoai_pham_vi, het_lan_chay…), tom_tat, trace_id | Khi chuyển cho nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, created_at, trace_id | Khi yêu cầu đóng |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần (100 đơn) |

**Kiểm tra chéo:** event dùng để tính từng chỉ số.

- Chính: `ticket_closed` (closed_at − created_at ≤ 24 giờ) và không có `ticket_reopened` trong 7 ngày, chia `refund_request_created`.
- Dùng (bỏ qua gợi ý): `staff_review_decision` với quyet_dinh ∈ {sua, bo}, chia tổng `staff_review_decision`.
- An toàn (mở lại 7 ngày): `ticket_reopened` trong 7 ngày kể từ `ticket_closed`, chia `refund_request_created`.
- Dùng (tự đề xuất): `agent_suggestion_shown` nối `refund_request_created` qua trace_id, lọc arm.
- An toàn (tự đề xuất): `audit_sample_checked`.
- Chi phí mỗi việc thành công (luật dừng chi phí): `agent_run_completed` (token, tool) + `staff_review_decision.phut_xem_lai` + `staff_rework_completed.phut_lam_lai`, chia số yêu cầu thành công. Phút đo thật thay cho cột simulated từ tuần 1.
- Hoàn trùng (luật dừng an toàn): đếm `refund_ledger_write` cùng request_id có ket_qua = ok hơn một lần.

Cả năm chỉ số trong bảng E1 đều tính được từ danh sách event trên.

## E2 · Rủi ro kinh tế

Số lấy từ `bang_chi_phi.md`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, chi phí mỗi việc thành công lên 6.787 đ [simulated] | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% = 48/982 trong phạm vi) | Thu hẹp về noi_dia, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu) [simulated]; hoà vốn ≤ 5,1 phút/lần xem lại | % yêu cầu được xem lại còn > 50% cuối bước 0.25, hoặc phút xem lại đo thật trung bình > 5 phút | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%; rút ngắn màn hình xem lại | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yc/tháng, +2.370 đ/việc (tổng 5.784 đ = 0,48×) nếu còn một nửa [simulated] | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot; xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
| Lương nhân viên tăng 25% | +23,1%, lên 5.506 đ [simulated] | Thay đổi bảng lương CSKH | Cập nhật `LUONG_PHUT` trong mô hình, tính lại ngưỡng luật dừng chi phí | Giám đốc vận hành LogiX-VN |
