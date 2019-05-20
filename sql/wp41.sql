select match_id, killer_name as player_name, count(killer_name) as kill_count from match_frag
where victim_name is not null
group by killer_name
order by match_id, kill_count desc