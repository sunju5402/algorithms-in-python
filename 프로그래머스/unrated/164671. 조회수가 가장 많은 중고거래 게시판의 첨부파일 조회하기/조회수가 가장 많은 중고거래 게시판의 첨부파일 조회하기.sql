-- 코드를 입력하세요
select concat('/home/grep/src/', a.board_id, '/', file_id, file_name, file_ext) file_path
from used_goods_file a join used_goods_board b on a.board_id = b.board_id
where views = (select max(views) from used_goods_board)
order by file_id desc;
