dau_sql = """
WITH daily_active_users AS (
    SELECT distinct
        user_id,
        DATE(created_at) as date
    FROM
        kakaotalk_chat
    WHERE
        user_id != ""
)
SELECT
    date,
    COUNT(*) as cnt 
FROM
    daily_active_users 
GROUP BY
    1 
ORDER BY
    1;
""".strip()
