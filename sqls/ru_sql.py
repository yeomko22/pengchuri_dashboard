ru_sql = """
WITH registered_date AS (
    SELECT
        user_id,
        MIN(DATE(created_at)) as date
    FROM
        kakaotalk_chat
    WHERE
        user_id != ""
    GROUP BY
        1
)
SELECT
    date,
    COUNT(*) as cnt 
FROM
    registered_date
GROUP BY
    1
ORDER BY
    1;
""".strip()
