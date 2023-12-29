chat_sql = """
SELECT
    id,
    CONVERT_TZ(created_at, '+00:00', 'Asia/Seoul') as created_at,
    user_id,
    question,
    answer
FROM
    kakaotalk_chat 
WHERE
    user_id not in ("", "Q0x8G-a_9cz3", "GHQ7hwxwYekr")
ORDER BY
    created_at DESC
LIMIT
    {pagesize}
OFFSET
    {offset}
""".strip()
