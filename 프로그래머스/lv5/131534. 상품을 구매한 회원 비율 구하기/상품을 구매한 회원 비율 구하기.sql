-- 코드를 입력하세요
SELECT year(sales_date) as year, month(sales_date) as month, count(distinct a.user_id) as puchased_users,
round(count(distinct a.user_id) / 
    (
    select count(*)
    from user_info
    where year(joined) = 2021), 1) as puchased_ratio
from online_sale a join user_info b on a.user_id = b.user_id
where year(b.joined) = 2021
group by year(sales_date), month(sales_date)
order by year, month
;