-- 코드를 입력하세요
select order_id, product_id, date_format(out_date, '%Y-%m-%d'), 
case 
    when out_date is null then '출고미정'
    when datediff('2022-05-01', out_date) >= 0 then '출고완료'
    else '출고대기'
end 출고여부
from food_order
order by order_id