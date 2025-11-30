-- Database yaradılır (əgər artıq mövcud deyilsə)
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- İstifadəçi yaradılır (əgər artıq mövcud deyilsə)
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- İstifadəçiyə yalnız SELECT privilege verilir bu database üçün
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Dəyişiklikləri aktivləşdirmək üçün
FLUSH PRIVILEGES;
