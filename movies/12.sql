SELECT title FROM movies
WHERE id IN (SELECT movie_id FROM stars
WHERE person_id IN (SELECT id FROM people WHERE name = "Jhonny Depp") AND WHERE
person_id IN (SELECT id FROM people WHERE name = "Bonham Carter"));

SELECT title FROM movies JOIN stars ON stars.movie_id = movies.id JOIN people ON people.id = stars.person_id WHERE people.name = "Jhonny Depp" AND title IN (SELECT title FROM movies JOIN stars ON stars.movie_id = movies.id JOIN people ON people.id = stars.person_id WHERE people.name = "Helena Bonham Carter");