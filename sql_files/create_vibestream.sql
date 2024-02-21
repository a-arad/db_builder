DROP TABLE IF EXISTS users;
CREATE TABLE users (user_id integer, user_name varchar(50), PRIMARY KEY (user_id));
\copy users FROM '../synthetic_datasets/vibestream/users.csv' DELIMITER ',' CSV HEADER NULL AS ''
DROP TABLE IF EXISTS posts;
CREATE TABLE posts (user_id integer, post_id integer, content varchar(255), post_date date, PRIMARY KEY (post_id));
\copy posts FROM '../synthetic_datasets/vibestream/posts.csv' DELIMITER ',' CSV HEADER NULL AS ''
DROP TABLE IF EXISTS likes;
CREATE TABLE likes (like_id integer, post_id integer, user_id integer);
\copy likes FROM '../synthetic_datasets/vibestream/likes.csv' DELIMITER ',' CSV HEADER NULL AS ''
DROP TABLE IF EXISTS algo_update_failure;
CREATE TABLE algo_update_failure (fail_date date, PRIMARY KEY (fail_date));
\copy algo_update_failure FROM '../synthetic_datasets/vibestream/algo_update_failure.csv' DELIMITER ',' CSV HEADER NULL AS ''
DROP TABLE IF EXISTS algo_update_success;
CREATE TABLE algo_update_success (success_date date, PRIMARY KEY (success_date));
\copy algo_update_success FROM '../synthetic_datasets/vibestream/algo_update_success.csv' DELIMITER ',' CSV HEADER NULL AS ''
DROP TABLE IF EXISTS follows;
CREATE TABLE follows (follower_id integer, followee_id integer);
\copy follows FROM '../synthetic_datasets/vibestream/follows.csv' DELIMITER ',' CSV HEADER NULL AS ''
