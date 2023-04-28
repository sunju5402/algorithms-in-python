-- 코드를 입력하세요
select a.member_name, b.review_text, date_format(b.review_date, '%Y-%m-%d') as review_date
from member_profile a join rest_review b on a.member_id = b.member_id
where a.member_id in (SELECT a.member_id
from member_profile a join rest_review b on a.member_id = b.member_id
group by a.member_id
having count(*) = (select count(*)
                  from member_profile a join rest_review b on a.member_id = b.member_id
                  group by a.member_id
                  order by count(*) desc
                  limit 1)) 
order by review_date, b.review_text
                  