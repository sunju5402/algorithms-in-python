-- 코드를 입력하세요
select apnt_no, pt_name, pt_no, d.mcdp_cd, dr_name, apnt_ymd
from doctor d join 
(
    select mddr_id, pt_name, p.pt_no, apnt_no, mcdp_cd, apnt_ymd
    from patient p join appointment a on p.pt_no = a.pt_no
    where apnt_cncl_yn = 'N' and date_format(apnt_ymd, '%Y-%m-%d') = '2022-04-13' and mcdp_cd = 'CS'
) pa on d.dr_id = pa.mddr_id
order by apnt_ymd