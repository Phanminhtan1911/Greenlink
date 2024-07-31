<?php
if (isset($_POST['submit'])) {
    $target_dir = "uploads/"; // Thư mục bạn muốn lưu file
    $target_file = $target_dir . "input.jpg"; // Đường dẫn file với tên cố định
    $uploadOk = 1;
    $imageFileType = strtolower(pathinfo($_FILES["fileToUpload"]["name"],PATHINFO_EXTENSION));

    // Kiểm tra xem file tải lên có phải là ảnh thực sự hay không
    if(isset($_POST["submit"])) {
        $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
        if($check !== false) {
            echo "File là một ảnh - " . $check["mime"] . ".";
            $uploadOk = 1;
        } else {
            echo "File không phải là ảnh.";
            $uploadOk = 0;
        }
    }

    // Kiểm tra kích thước file
    if ($_FILES["fileToUpload"]["size"] > 500000) {
        echo "Xin lỗi, file của bạn quá lớn.";
        $uploadOk = 0;
    }

    // Chỉ cho phép một số định dạng file nhất định
    if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg") {
        echo "Xin lỗi, chỉ JPG, JPEG, PNG được phép.";
        $uploadOk = 0;
    }

    // Nếu file đã tồn tại, đổi tên file cũ
    if (file_exists($target_file)) {
        $existing_files = count(glob($target_dir . "*"));
        rename($target_file, $target_dir . "input_" . $existing_files . ".jpg");
    }

    // Thử tải file lên
    if ($uploadOk == 1) {
        if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
            echo "File ". htmlspecialchars( basename( $_FILES["fileToUpload"]["name"])). " đã được tải lên.";
        } else {
            echo "Xin lỗi, đã có lỗi xảy ra khi tải file của bạn lên.";
        }
    }
}
?>