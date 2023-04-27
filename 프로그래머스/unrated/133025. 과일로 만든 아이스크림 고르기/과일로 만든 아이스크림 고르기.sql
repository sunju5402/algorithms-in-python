-- 코드를 입력하세요
SELECT a.flavor
from first_half a join icecream_info b on a.flavor = b.flavor
where b.ingredient_type = 'fruit_based' and a.total_order >= 3000
