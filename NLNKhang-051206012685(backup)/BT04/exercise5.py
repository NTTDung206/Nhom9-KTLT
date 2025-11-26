str = 'X-DSPAM-Confidence:0.8475'
colon_pos = str.find(':')
# Tìm vị trí dấu hai chấm
number_str = str[colon_pos + 1:]
# Cắt chuỗi từ sau dấu hai chấm
number = float(number_str)
# Chuyển thành số thực
print(number)