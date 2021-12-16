# ASM
## Task 1
<p> Tạo một chương trình Python mới có tên “lastname_firstname_grade_the_exams.py.” (Đảm bảo tệp mã nguồn của bạn nằm trong cùng thư mục với tệp dữ liệu bạn vừa tải xuống.) </p>
<p> Tiếp theo, viết một chương trình cho phép người dùng nhập tên của một tệp. Cố gắng mở tệp được cung cấp để truy cập đọc. Nếu tệp tồn tại, bạn có thể in ra một thông báo xác nhận. Nếu tệp không tồn tại, bạn nên cho người dùng biết rằng không thể tìm thấy tệp và nhắc lại họ. </p>
<p> Sử dụng try/except để thực hiện việc này (đừng chỉ sử dụng một loạt câu lệnh “if” — chúng tôi muốn chương trình này càng “chung chung” càng tốt). </p>

## Task 2
<p> Tiếp theo, bạn sẽ cần phân tích dữ liệu có trong tệp bạn vừa mở để đảm bảo rằng nó ở đúng định dạng. Mỗi tệp dữ liệu chứa một loạt câu trả lời của học sinh ở định dạng sau: </p>
<strong> N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D </strong>
<p> hoặc </p>
<strong> N12345678,B,,D,,C,B,,A,C,C,,B,A,B,A,,,,A,C,A,A,B,D, </strong>
<p> Giá trị đầu tiên là số ID của sinh viên. 25 chữ cái sau là câu trả lời của học sinh cho kỳ thi. Tất cả các giá trị được phân tách bằng dấu phẩy. Nếu không có chữ cái nào sau dấu phẩy, điều này có nghĩa là học sinh đã bỏ qua việc trả lời câu hỏi. </p>
<p> Lưu ý rằng một số dòng dữ liệu có thể bị hỏng! Ví dụ: dòng dữ liệu này không có đủ câu trả lời: </p>
<strong> N12345678,B,A,D,D,C,B </strong>
<p> Và dòng dữ liệu này có quá nhiều câu trả lời: </p>
<strong> N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D,A,B,C,D,E </strong>
<p> Nhiệm vụ của bạn cho phần này của chương trình là thực hiện như sau: </p>
    <ol>
        <li> Báo cáo tổng số dòng dữ liệu được lưu trữ trong tệp. </li>
        <li>  Phân tích từng dòng và đảm bảo rằng nó là "hợp lệ". </li>
            <ul>
                <li> Một dòng hợp lệ chứa danh sách 26 giá trị được phân tách bằng dấu phẩy </li>
                <li> N# cho một học sinh là mục đầu tiên trên dòng. Nó phải chứa ký tự “N” theo sau là 8 ký tự số. </li>
            </ul>
        <li> Nếu một dòng dữ liệu không hợp lệ, bạn nên báo cáo cho người dùng bằng cách in ra một thông báo lỗi. Bạn cũng nên đếm tổng số dòng dữ liệu hợp lệ trong tệp. </li>
    </ol>
<p> <i> Gợi ý: Sử dụng phương pháp split để tách dữ liệu ra khỏi tệp. Bạn có thể cần sử dụng phương pháp này một vài lần cùng với một hoặc hai vòng lặp. Hãy suy nghĩ về thứ tự mà bạn cần chia các mục của mình. Ví dụ: tệp của bạn được sắp xếp sao cho hồ sơ của một học sinh chiếm toàn bộ dòng trong tệp. Việc tách trước khi ngắt dòng sẽ tách biệt dữ liệu của từng học sinh. Sau đó, bạn sẽ cần phải chia nhỏ từng mục dựa trên ký tự phân tách để rút ra câu trả lời cho từng học sinh.</i></p>

## Task 3
<p> Tiếp theo, bạn sẽ viết một chương trình để chấm điểm các bài thi cho một phần nhất định. Kỳ thi gồm 25 câu hỏi, trắc nghiệm. Đây là một chuỗi đại diện cho các câu trả lời: </p>
<strong> answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D" </strong>
<p> Chương trình của bạn nên sử dụng những câu trả lời này để tính điểm cho mỗi dòng dữ liệu hợp lệ. Điểm có thể được tính như sau: </p>
  <ul>
  <li> +4 điểm cho mỗi câu trả lời đúng </li>
  <li> 0 điểm cho mỗi câu trả lời bị bỏ qua </li>
  <li> -1 điểm cho mỗi câu trả lời sai </li>
  </ul>
<p> Bạn cũng sẽ muốn tính toán các thống kê sau cho toàn bộ lớp: </p>
  <ul>
  <li> Điểm trung bình </li>
  <li> Điểm cao nhất </li>
  <li> Điểm thấp nhất </li>
  <li> Miền giá trị của điểm (cao nhất trừ thấp nhất) </li>
  <li> Giá trị trung vị (Sắp xếp các điểm theo thứ tự tăng dần. Nếu # học sinh là số lẻ, bạn có thể lấy giá trị nằm ở giữa của tất cả các điểm (tức là [0, 50, 100] — trung vị là 50). Nếu # học sinh là chẵn bạn có thể tính giá trị trung vị bằng cách lấy giá trị trung bình của hai giá trị giữa (tức là [0, 50, 60, 100] — giá trị trung vị là 55)). </li>
  </ul>
<p> <i> Gợi ý: Khi đã cho điểm các học sinh, bạn nên sử dụng một list để lưu trữ điểm số của từng học sinh; sau đó bạn có thể tính toán số liệu thống kê sau khi đã kiểm tra mọi học sinh trong tệp. </i> </p>

## Task 4
<p> Cuối cùng, yêu cầu chương trình của bạn tạo một tệp “kết quả” chứa các kết quả chi tiết cho từng học sinh trong lớp của bạn. Mỗi dòng của tệp này phải chứa số ID của học sinh, dấu phẩy và sau đó là điểm của họ. Bạn nên đặt tên tệp này dựa trên tên tệp gốc được cung cấp — ví dụ: nếu người dùng muốn phân tích “class1.txt”, bạn nên lưu trữ kết quả trong tệp có tên “class1_grades.txt”. </p>

## Task 5
Chỉ sử dụng pandas và numpy khi bạn triển khai task 1 đến task 4.
