SELECT * FROM members
-- SEE JOIN
;


SELECT
    *
FROM members
WHERE
    surname ILIKE '%sm%'
  AND
    CAST(zipcode AS TEXT) ILIKE '%2%'
;


SELECT
    (m.firstname || ' ' || surname) AS fullname,
    *
FROM members AS m
WHERE
        m.surname IN('Rownam', 'Smith')
--    OR
--     firstname ILIKE 'Tim'
;


SELECT
    (firstname || ' ' || surname) AS fullname
FROM members
WHERE surname ILIKE 's%'
ORDER BY fullname
;


SELECT
    COUNT(*), surname, ARRAY_AGG(firstname), MAX(memid), ARRAY_AGG(memid)
FROM members
GROUP BY surname
-- ORDER BY first_name_count DESC
-- LIMIT 1
;

