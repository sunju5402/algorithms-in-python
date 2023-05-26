-- 코드를 입력하세요
SELECT c.animal_id, c.animal_type, c.name
from (select a.animal_id, a.animal_type, a.name, b.sex_upon_outcome
      from animal_ins a join animal_outs b on a.animal_id = b.animal_id
        where a.sex_upon_intake like 'Intact%') as c
where c.sex_upon_outcome like 'Spayed%' or c.sex_upon_outcome like 'Neutered%'
order by c.animal_id;

SELECT a.animal_id, a.animal_type, a.name
from animal_ins a join animal_outs b on a.animal_id = b.animal_id
where a.sex_upon_intake like 'Intact%' and (b.sex_upon_outcome like 'Spayed%' or b.sex_upon_outcome like 'Neutered%')
order by a.animal_id;

SELECT a.animal_id, a.animal_type, a.name
from animal_ins a join animal_outs b on a.animal_id = b.animal_id
where a.sex_upon_intake like 'Intact%' and b.sex_upon_outcome not in ('Intact Male', 'Intact Female')
order by a.animal_id;


