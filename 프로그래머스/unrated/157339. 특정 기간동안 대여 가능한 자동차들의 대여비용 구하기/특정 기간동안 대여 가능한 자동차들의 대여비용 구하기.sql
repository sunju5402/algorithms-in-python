-- 코드를 입력하세요
select a.car_id, a.car_type, round(daily_fee * 30 * (100 - c.discount_rate) / 100, 0) as fee
from car_rental_company_car a join CAR_RENTAL_COMPANY_discount_PLAN c
    on a.car_type = c.car_type
where a.car_id not in (
    select car_id
    from car_rental_company_rental_history
    where start_date < '2022-12-01' and end_date >= '2022-11-01'
) and (a.car_type = '세단' or c.car_type = 'suv')
and c.duration_type = '30일 이상'
group by a.car_id
having fee >= 500000 and fee < 2000000
order by fee desc, car_type
