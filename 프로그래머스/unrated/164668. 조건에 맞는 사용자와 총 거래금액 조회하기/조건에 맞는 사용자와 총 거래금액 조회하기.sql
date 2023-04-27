-- 코드를 입력하세요
SELECT user_id, nickname, sum(price) as total_sales
from used_goods_board a join used_goods_user b on a.writer_id = b.user_id
where status = 'DONE'
group by user_id
having total_sales >= 700000
order by total_sales