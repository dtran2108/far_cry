SELECT match_id,
       player_name,
       Sum(kill_count) as kill_count,
       sum(sucide_count) as sucide_count,
       sum(death_count) as death_count,
       round (100.0 * sum(kill_count) / (sum(kill_count) + sum(death_count) + sum(sucide_count)), 2) as efficiency
FROM 
    (select match_id,
            killer_name as player_name,
            count(killer_name) as kill_count,
            (count(*) - count(victim_name)) as sucide_count,
            0 as death_count
    from match_frag
    group by killer_name
    union
    select match_id,
           victim_name as player_name,
           0 as kill_count,
           0 as sucide_count,
           count(victim_name) as death_count 
    from match_frag
    where victim_name is not null
    group by player_name)
GROUP BY match_id, player_name