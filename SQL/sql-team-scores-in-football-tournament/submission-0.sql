-- Write your query below
select t.team_id, t.team_name, coalesce(sum(a.points),0) as num_points 
from (
select host_team as team, sum(1) as points
from matches
where host_goals = guest_goals
group by team
union all
select guest_team as team, sum(1) as points
from matches
where host_goals = guest_goals
group by team
union all
select case
when host_goals > guest_goals then host_team
else guest_team
end as team, sum(3) as points
from matches
where host_goals <> guest_goals
group by team
) a
right join teams t
on a.team = t.team_id
group by t.team_id, t.team_name
order by num_points desc, t.team_id;
