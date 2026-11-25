# Team

## Thông tin nhóm

- Tên nhóm: Nhom123 
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Nhom123-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/ThuHang2604/K5-L3B-DAY13-Nhom123-LaunchEconomics · nhánh `main` · commit chốt: ghi sau khi push

> Lab thiết kế cho nhóm 4 người, nhưng bài này làm một mình. Một người đảm nhận cả bốn vai. Hai phần cần nhiều người không làm đúng như đề được, đã ghi rõ trong hồ sơ: gắn nhãn độc lập (C, xem `report/team/bang_loi.md`) và duyệt chéo Gate 2a (xem `report/team/phieu_cham.md`).

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Đỗ Thị Thu Hằng | (điền MSSV) | (điền email) | ThuHang2604 | Cả bốn vai: người viết code, người kiểm số, người gắn nhãn, người giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

## Cá nhân

Báo cáo cá nhân: `report/team/MSSV_DoThiThuHang.md` (thay `MSSV` bằng mã số sinh viên trong tên file).

## DoThiThuHang-MSSV

### Phần việc phụ trách

- Toàn bộ năm nhiệm vụ A–E, ở cả bốn vai.

### Đóng góp cụ thể

- **A, B (người viết code):** viết ba hàm A1, hàm `mo_hinh`, các hàm in A2, A3, A4, B1–B4, D1 và E1 trong `src/lab13.py`; ba phép thử in ĐẠT.
- **Kiểm số:** tính tay chi phí mỗi việc thành công 4.373.585 ÷ 978 = 4.472 đ [simulated], chi phí cả hệ thống (4.373.585 + 222 × 12.000) ÷ 1.200 = 5.865 đ [simulated], và câu D1e: 20m ≥ 859 × (0,98 + 0,02m) → m ≥ 299.
- **C (gắn nhãn):** gắn nhãn 20 ca kèm lý do theo nguyên nhân gốc, so với bảng tham khảo (khớp 20/20), viết bảng khắc phục 5 ca.
- **D:** chọn chia theo nhân viên 20 + 20 với MDE 6 điểm, viết `pilot_plan.yaml` với 4 luật dừng.
- **E (giữ hồ sơ):** `chi_so.md` (5 chỉ số, 10 event, 4 dòng rủi ro), `ho_so_launch_v0.md` (đề xuất Go có điều kiện), `group_report.md`, tự rà theo thang hội đồng trong `phieu_cham.md`.

### Bằng chứng

- `cd src && python3 lab13.py`: in "Ba phép thử đáp án biết trước: ĐẠT" và mọi bảng số.
- `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"` chạy không lỗi; không còn `?` ngoài chú thích; lệnh grep từ bị cấm (quy tắc 5) không in gì.
- Các file trong `report/team/` và lịch sử commit trên repo.
