dau_sql = """
WITH daily_active_users AS (
    SELECT distinct
        user_id,
        DATE(CONVERT_TZ(created_at, '+00:00', 'Asia/Seoul')) as date
    FROM
        kakaotalk_chat
    WHERE
        user_id not in ("", "Q0x8G-a_9cz3", "GHQ7hwxwYekr")
        AND question != "펭추리야 뭐하니?"
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
