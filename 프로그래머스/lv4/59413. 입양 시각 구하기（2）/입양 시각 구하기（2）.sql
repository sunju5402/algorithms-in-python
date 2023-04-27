-- 코드를 입력하세요
set @hour = -1;
select (@hour := @hour +1) as hour,
    (SELECT count(*)
     from animal_outs
     where hour(datetime)=@hour) as count
from animal_outs
where @hour < 23;