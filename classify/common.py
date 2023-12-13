import random

from matplotlib import pyplot as plt

class ScatterY:
	"""
	Trực quan hóa mức độ giao nhau giữa 2 nhãn (Phân loại nhị phân)
	Args:
		len_of_x: Int, độ dài của tập X
		y1: Tuple/List/NdArray, chứa nhãn thực (Phải là mảng 1 chiều !)
		y2: Tuple/List/NdArray chứa nhãn dự đoán (Phải là mảng 1 chiều !)
	Returns:
		Đồ thị trực quan hóa mức độ giao nhau giữa 2 nhãn
	"""

	def __init__(
		self,
		len_of_x=None,
		y1=None,
		y2=None
	):
		self.len_of_x = range(len_of_x)
		self.y1 = y1
		self.y2 = y2

		plt.scatter(self.len_of_x, self.y1, color='b', label='Nhãn thực')
		plt.scatter(self.len_of_x, self.y2, color='r', label='Nhãn dự đoán')
		plt.title('Tỉ lệ giữa nhãn thực & nhãn dự đoán')
		plt.legend()
		plt.show()

def random_color_str(num_colors=1):
	"""
	Trình tạo màu ngẫu nhiên
	:param num_colors: Số lượng màu cần tạo (Mặc định: 1)
	:return: Tuple/List chứa màu là chuỗi HEX, số lượng tương ứng với tham số num_colors truyền vào
	"""
	if type(num_colors) is not int:
		raise TypeError('Tham số num_colors phải là kiểu Int !')
		return

	if num_colors < 1:
		raise ValueError('Tham số num_colors phải lớn hơn hoặc bằng 1 !')
		return

	colors = ["#" + ''.join([random.choice('0123456789ABCDEF') for i in range(6)])
	    for j in range(num_colors)]
	return colors
