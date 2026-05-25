# 1
# input: raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT " có kiểu dữ liệu là chuỗi (string)
# output: menu gồm các chức năng 
    # 1 hthi chuỗi dữ liệu gốc
    # 2 hthi dữ liệu đã đc chuẩn hóa và in ra báo cáo
    # 3 sau khi tìm kiếm thì hthi ra nhân viên thoe mã id
    # 4 nếu ng dùng chọn tháot ctrinh thì hthi "Thoát chương trình"
# giải pháp: sdung split("|") để tách các nhân viên và split(";") để tách dữ liệu
    # sdung strip() để xóa khoảng trắng
    # upper() để viết hoa 
    # title() chuẩn hóa họ tên
    # replace("-", "") để xóa dấu - 
# thuật toán: sdung vòng lặp while để hiển thị ra menu và cho ng dùng lựa chọn
    # nếu ng dùng chọn 1 thì in ra dữ liệu gốc
    # chọn 2 thì in ra tên đã đc chuẩn hóa và in báo cáo
    # chọn 3 thì tìm kiếm theo id ng dùng và in ra kqua
    # chọn 4 sẽ thoát ctrinh và hthi “Thoát chương trình” 
    # nếu nhập các số khác thì báo lỗi và cho ng dùng nhập lại 

# 2
raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:

    print("===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ")

    if choice == "1":
        print("Dữ liệu gốc:")
        print(raw_data)

    elif choice == "2":

        employees = raw_data.split("|")
        print("ID", "HỌ TÊN", "SỐ ĐIỆN THOẠI", "PHÒNG")

        for employee in employees:
            employee_info = employee.split(";")
            emp_id = employee_info[0].strip().upper()
            full_name = employee_info[1].strip().title()
            phone = employee_info[2].strip()
            phone = phone.replace("-", "")
            department = employee_info[3].strip().upper()

            if phone.isdigit():
                phone = "******" + phone[-4:]
            else:
                phone = "Invalid Format"

            print(f"{emp_id} {full_name} {phone} {department}")

    elif choice == "3":
        search_id = input("Nhập mã nhân viên cần tìm: ")
        search_id = search_id.strip().upper()
        employees = raw_data.split("|")
        found = False

        for employee in employees:
            employee_info = employee.split(";")
            emp_id = employee_info[0].strip().upper()
            full_name = employee_info[1].strip().title()
            phone = employee_info[2].strip()
            phone = phone.replace("-", "")
            department = employee_info[3].strip().upper()

            if phone.isdigit():
                phone = "******" + phone[-4:]
            else:
                phone = "Invalid Format"

            if search_id == emp_id:
                print("===== THÔNG TIN NHÂN VIÊN =====")
                print(f"ID: {emp_id}")
                print(f"Họ tên: {full_name}")
                print(f"Điện thoại: {phone}")
                print(f"Phòng ban: {department}")

                found = True
                break

        if found == False:
            print("Không tìm thấy nhân viên")

    elif choice == "4":
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
    
