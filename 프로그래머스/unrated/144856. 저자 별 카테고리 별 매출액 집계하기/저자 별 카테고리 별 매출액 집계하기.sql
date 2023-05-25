-- 코드를 입력하세요
SELECT b.author_id, b.author_name, a.category, sum(c.sales * a.price) as total_sales
from book a join author b on a.author_id = b.author_id 
join book_sales c on a.book_id = c.book_id
where date_format(c.sales_date, "%Y-%m") = "2022-01"
group by a.category, a.author_id
order by a.author_id, a.category desc