select match_id,
       victim_name as player_name,
       count(victim_name) as death_count from match_frag
where victim_name is not null
group by player_name
order by match_id, death_count desc