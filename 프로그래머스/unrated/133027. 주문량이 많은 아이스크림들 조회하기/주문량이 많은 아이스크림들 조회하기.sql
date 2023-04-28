-- 코드를 입력하세요
select a.flavor
from (
    select flavor, sum(total_order) as total
    from first_half
    group by flavor
    ) as a join (
    select flavor, sum(total_order) as total
    from july
    group by flavor
    ) as b on a.flavor = b.flavor
order by a.total + b.total desc
limit 3;