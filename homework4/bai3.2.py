#Branch and Bound : Nhánh cận
#Bài toán:  Có thể định nghĩa khái niệm dãy ngoặc đúng dưới dạng đệ quy như sau:
        # 1. () là dãy ngoặc đúng
        # 2. C là dãy ngoặc đúng nếu C = (A) hay C = AB với A, B là các dãy ngoặc đúng.
        # Ví dụ dãy ngoặc đúng: (), (()), ()(), (())()
        # Ví dụ dãy ngoặc sai: )(, ((((, ()((, )))), )()(
        # Cho với n chẵn, in ra các dãy ngoặc đúng có chiều dài n. Tính số lượng đáp án đúng
#Cách làm: Ta sẽ sinh '(' trước. Với mỗi lần sinh '(' ta có thể tính được số lượng ')' cần phải sinh và số lượng ô còn trống. Từ đó cắt giảm các nhánh không cho kết quả
#Độ phức tạp O(2^n)

def Try(i,sum,out):
	global cnt, n
	if i==n:
		if sum==0:
			cnt+=1
			print(out)
	else:
        for x in [(1,'('),(-1,')')]:
			if sum+x[0]>=0:     #Đánh giá
				Try(i+1,sum+x[0],out+x[1])

#Test
n=10
cnt=0
Try(0,0,'')
print(cnt)