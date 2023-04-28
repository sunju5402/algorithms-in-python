-- 코드를 입력하세요
SELECT user_id, nickname, 
concat(city, ' ', street_address1, ' ', street_address2) 전체주소,
concat(left(tlno, 3), '-', mid(tlno, 4, 4), '-', right(tlno, 4)) 전화번호
from used_goods_board a join used_goods_user b on a.writer_id = b.user_id
group by writer_id
having count(*) >= 3
order by user_id desc;
