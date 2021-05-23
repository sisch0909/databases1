ALTER TABLE members ADD FOREIGN KEY (email) REFERENCES members_info(email);
ALTER TABLE sports ADD FOREIGN KEY (professionalism_ID) REFERENCES professionalisms(professionalism_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE members_info ADD FOREIGN KEY (role_ID) REFERENCES roles(role_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE members_info ADD FOREIGN KEY (duration_group_ID) REFERENCES duration_groups(duration_group_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE members_info ADD FOREIGN KEY (membership_type_ID) REFERENCES memberships(membership_type_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE members_info ADD FOREIGN KEY (age_group_ID) REFERENCES age_groups(age_group_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE members_sports ADD FOREIGN KEY (member_ID) REFERENCES members_info(member_ID) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE members_sports ADD FOREIGN KEY (sport_ID) REFERENCES sports(sport_ID) ON DELETE CASCADE ON UPDATE CASCADE;

UPDATE members_info SET age_group_ID = 1 WHERE date_part('year', age(birthday)) <= 12;
UPDATE members_info SET age_group_ID = 2 WHERE date_part('year', age(birthday)) > 12 AND date_part('year', age(birthday)) <= 19;
UPDATE members_info SET age_group_ID = 3 WHERE date_part('year', age(birthday)) > 19 AND date_part('year', age(birthday)) <= 65;
UPDATE members_info SET age_group_ID = 4 WHERE date_part('year', age(birthday)) > 65;


UPDATE members_info SET duration_group_ID = 1 WHERE age_group_ID = 1;
UPDATE members_info SET duration_group_ID = floor(2*random()+1) WHERE age_group_ID = 2;
UPDATE members_info SET duration_group_ID = floor(4*random()+1) WHERE age_group_ID = 3 OR age_group_ID = 4;


