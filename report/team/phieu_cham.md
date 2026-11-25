# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Nhom123 (L3B), làm cá nhân: Đỗ Thị Thu Hằng
- Nhóm được chấm: **không có**

> **Chưa duyệt chéo:** lab này làm một mình nên không được xếp nhóm n + 1 để chấm, cũng không có nhóm hội đồng chấm hồ sơ của mình. Phiếu chấm nhóm khác để trống, không bịa điểm. Nếu coach xếp nhóm để duyệt chéo bổ sung, sẽ điền phiếu dưới đây bằng một commit mới.

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | — | Chưa có nhóm được chấm |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | — | Chưa có nhóm được chấm |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | — | Chưa có nhóm được chấm |
| **Tổng** | | | | **— / 30** | |

## Tự rà hồ sơ của mình theo thang hội đồng (không thay cho điểm hội đồng)

Để bù cho phần duyệt chéo, tự đặt mình vào vai hội đồng và rà `ho_so_launch_v0.md` theo đúng thang trên. Đây là tự đánh giá, không phải điểm chấm chính thức.

| Tiêu chí | Tự đánh giá | Bằng chứng trong hồ sơ |
| --- | --- | --- |
| Đề xuất khớp bằng chứng | Mức 10 | Go có điều kiện khớp 0,38–0,48× chi phí nhân viên [simulated]; nêu hai con số bất lợi (xem lại 100% → 1,03×; power 0,64 ở mức 5 điểm) kèm cách xử lý |
| Số giả lập và phạm vi | Mức 10 | Mọi số từ cột `_simulated` có nhãn; phạm vi thu hẹp về noi_dia + hang_nang vì quoc_te 1,88× và doi_tac 0,85× [simulated] |
| Pilot ra được quyết định | Mức 10, rủi ro ở cỡ mẫu | 20 + 20 cụm ngẫu nhiên có đối chứng cùng thời gian; 4 luật dừng có ngưỡng, thời hạn, người dừng; chỉ đủ mẫu cho MDE 6 điểm (ghi rõ đánh đổi) |

**Câu hỏi khó nhất mà hội đồng có thể hỏi và câu trả lời chuẩn bị sẵn:**

- *Hỏi:* Chi phí mỗi việc thành công là bao nhiêu nếu tuần đầu phải xem lại 100%? *Đáp:* 11.743 đ = 0,98×, hoặc 12.415 đ = 1,03× với 15,3 phút làm lại như dữ liệu [simulated]. Vì thế điều kiện 4 bắt buộc giảm xem lại theo bậc và đặt mục tiêu ≤ 5 phút mỗi lần xem lại (hoà vốn 5,1 / 4,8 phút).
- *Hỏi:* Với tỉ lệ mở lại 4,25% hiện tại, ngưỡng an toàn có làm pilot dừng ngay tuần đầu không? *Đáp:* Không. Ngưỡng so với đối chứng (chênh ≥ 2 điểm), kèm trần tuyệt đối 6%, cao hơn mức 3,97% hiện tại trong phạm vi.
