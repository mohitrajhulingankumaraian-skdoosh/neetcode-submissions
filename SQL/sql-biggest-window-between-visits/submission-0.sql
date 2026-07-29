with prev_visit as (
    select user_id, 
    visit_date,
    lead(visit_date,1) over (partition by user_id order by visit_date) as next_visit_date
    from user_visits
)
select user_id, max(coalesce(next_visit_date, '2021-01-01'::date) - visit_date) as biggest_window
from prev_visit
group by user_id
order by user_id;