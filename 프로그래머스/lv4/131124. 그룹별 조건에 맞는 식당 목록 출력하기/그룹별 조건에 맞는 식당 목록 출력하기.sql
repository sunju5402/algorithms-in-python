-- 코드를 입력하세요
select b.member_name, a.review_text, date_format(a.review_date, '%Y-%m-%d') as review_date
from rest_review a join (
    select a.member_id, a.member_name
    from member_profile a join rest_review b on a.member_id = b.member_id
    group by a.member_id
    having count(*) = (
        select count(*)
        from rest_review
        group by member_id
        order by count(*) desc
        limit 1)) b on a.member_id = b.member_id
order by a.review_date, a.review_text;

# SELECT B.MEMBER_NAME, A.REVIEW_TEXT, DATE_FORMAT(A.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
# FROM REST_REVIEW A
# JOIN (
#     SELECT R.MEMBER_ID, M.MEMBER_NAME, RANK() OVER(ORDER BY CNT DESC) AS RANKING
#     FROM (
#         SELECT *, COUNT(MEMBER_ID) AS CNT
#         FROM REST_REVIEW
#         GROUP BY MEMBER_ID) AS R
#     JOIN MEMBER_PROFILE M ON R.MEMBER_ID = M.MEMBER_ID) B
# ON A.MEMBER_ID = B.MEMBER_ID
# WHERE B.RANKING = 1
# ORDER BY A.REVIEW_DATE, A.REVIEW_TEXT;