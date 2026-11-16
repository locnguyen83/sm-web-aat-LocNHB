# Fixture F2-3 – Đoạn SRS SM-WEB: Giỏ hàng & Checkout (10 yêu cầu)

> Trích từ `02_Requirements/02_SRS_Storefront.md` (hư cấu – đào tạo). Danh sách req_id hợp lệ: REQ-SF-01, 02, 03, 04, 07, 10, 11, 12, 14, 22.

| ID | Yêu cầu | Tiêu chí chấp nhận |
|---|---|---|
| REQ-SF-01 | Khách thêm sản phẩm vào giỏ từ trang chi tiết sản phẩm với số lượng chọn được. | Given trang chi tiết sản phẩm còn hàng, When chọn số lượng N và bấm "Thêm vào giỏ", Then giỏ có thêm N đơn vị và biểu tượng giỏ hiển thị số lượng mới. |
| REQ-SF-02 | Sản phẩm hết hàng không được thêm vào giỏ. | Nút thêm vào giỏ bị vô hiệu hoặc hệ thống báo lỗi, giỏ không thay đổi. |
| REQ-SF-03 | Số lượng mỗi sản phẩm trong giỏ từ 1 đến 10. | Nhập số lượng < 1 hoặc > 10 → không chấp nhận, hiển thị thông báo. |
| REQ-SF-04 | Khách thay đổi số lượng hoặc xóa dòng sản phẩm; tổng tiền cập nhật ngay. | Thành tiền dòng và tổng giỏ được tính lại đúng. |
| REQ-SF-07 | Giỏ của khách đã đăng nhập được giữ lại khi đăng xuất và đăng nhập lại. | Đăng xuất rồi đăng nhập lại, giỏ còn nguyên. |
| REQ-SF-10 | Checkout gồm 4 bước: Giỏ hàng → Đăng nhập → Địa chỉ thanh toán → Phương thức thanh toán. | Không thể sang bước sau khi bước trước chưa hợp lệ. |
| REQ-SF-11 | Khách chưa đăng nhập phải đăng nhập hoặc đăng ký trước khi nhập địa chỉ. | Ở bước 2 hiển thị form đăng nhập/đăng ký. |
| REQ-SF-12 | Địa chỉ thanh toán bắt buộc: địa chỉ, thành phố, tỉnh/bang, quốc gia, mã bưu chính. | Thiếu một trường → không sang bước 4, hiển thị lỗi tại trường. |
| REQ-SF-14 | Thanh toán thành công tạo hóa đơn có mã duy nhất và thông báo xác nhận. | Khách thấy thông báo và mã hóa đơn; hóa đơn xuất hiện trong mục Hóa đơn. |
| REQ-SF-22 | Thẻ tín dụng: số thẻ định dạng 0000-0000-0000-0000; ngày hết hạn MM/YYYY không ở quá khứ; CVV 3–4 chữ số; tên chủ thẻ. | Trường sai định dạng → không thanh toán, hiển thị lỗi. |
