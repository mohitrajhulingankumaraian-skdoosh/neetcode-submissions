-- Write your query below
with high_score as (
    select student_id, exam_id, score,
    row_number() over (partition by student_id order by score desc, exam_id) as rnk
    from exam_results
)
select student_id, exam_id, score
from high_score
where rnk = 1
order by student_id;