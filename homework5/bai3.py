# Bài toán : 	Cho n quả bóng bay đặt lần lượt từ 1 tới n và có độ cao là Hi.
# 		        Bạn được giao cho nhiệm vụ bắn bóng từ vị trí 0 với độ cao bất kỳ để phá hết bóng.
# 		        Biết rằng với mỗi lần mũi tên bắn trúng bóng thì mũi tên giảm 1 độ cao.
# 		        Đưa ra số mũi tên tối thiểu cần dùng.
# Giải thuật :	Vì mỗi lần bắn mũi tên giảm 1 độ cao, nên ta sẽ bắn lần lượt các bóng từ 0 → n với độ
                # cao tương ứng, khi đấy các mũi tên của ta sẽ giảm độ cao và phá vỡ các bóng ở vị trí
                # phía sau và làm giảm số mũi tên phải bắn ra. Nếu 1 bóng ở vị trí thứ i+1 không được phá 
                # vỡ sau i lần bắn thì lần i+1 sẽ bắn ở độ cao H(i+1) để phá vỡ bóng ở i+1. Các bóng ở đô
                # cao H bất kỳ nếu sau i lần bắn đã vỡ thì sẽ không cần bắn ở độ cao này. 
# Độ phức tạp:	O(n)

def process(highs):
    ans = 0
    while len(highs) != 0:
        h = highs.pop(0)-1
        ans = ans + 1
        tmp = []
        while len(highs) != 0:
            hj = highs.pop(0)
            if h == hj:
                h = h-1
            else:
                tmp.append(hj)
        highs = tmp.copy()
    
    print(ans)


n = 5
highs = [5, 3, 4, 2, 1]
process(highs)

        