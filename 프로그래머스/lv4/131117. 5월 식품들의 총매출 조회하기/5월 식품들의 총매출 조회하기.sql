-- 코드를 입력하세요
SELECT c.product_id, c.product_name, c.amount * c.price as total_sales
from (select a.product_id, a.product_name, sum(b.amount) as amount, a.price
      from food_product a join food_order b on a.product_id = b.product_id
    where date_format(produce_date, '%Y-%m') = '2022-05'
      group by a.product_id) c
order by total_sales desc, c.product_id;
