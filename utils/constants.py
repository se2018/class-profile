"""Important
If you're planning on changing a column name, make sure to change it for both
lists columns and columns_to_normalize
"""

columns = ['timestamp', 'email', 'gender', 'location', 'is_international', 'ethnicity',
           # Background
           'parents_edu', 'parents_technical', 'family_income', 'admission_avg', 'hs_extras',
           # Coding
           'code_start_age', 'fav_lang', 'text_editor', 'work_os', 'phone', 'num_hackathons', 'side_proj',
           # Jobs
           'coop_name_1', 'coop_salary_1', 'coop_loc_1',
           'coop_name_2', 'coop_salary_2', 'coop_loc_2',
           'coop_name_3', 'coop_salary_3', 'coop_loc_3',
           'coop_name_4', 'coop_salary_4', 'coop_loc_4',
           'coop_name_5', 'coop_salary_5', 'coop_loc_5',
           'coop_name_6', 'coop_salary_6', 'coop_loc_6',
           'fav_coop', 'ft_status',
           # Lifestyle
           'exercise', 'cooking', 'sleep_time',
           # School
           'uni_extras', 'is_se_orig', 'fav_course', 'least_fav_course', 'num_courses_failed',
           'term_avg_1a', 'class_attendance_1a',
           'term_avg_1b', 'class_attendance_1b',
           'term_avg_2a', 'class_attendance_2a',
           'term_avg_2b', 'class_attendance_2b',
           'term_avg_3a', 'class_attendance_3a',
           'term_avg_3b', 'class_attendance_3b',
           'term_avg_4a', 'class_attendance_4a',
           'hardest_term', 'easiest_term', 'preferred_program', 'soft_eng_rating',
           # Future
           'preferred_company_size', 'work_loc', 'se_friendships', 'career_motives', 'grad_school', 'num_years_soft_eng',
           'preferred_tech_discipline', 'school_debt', 'se_advice']

columns_to_normalize = ['gender', 'location',
           # Background
           'family_income', 'admission_avg', 'hs_extras',
           # Coding
           'code_start_age', 'fav_lang', 'text_editor',
           # Jobs
           'coop_name_1', 'coop_salary_1', 'coop_loc_1',
           'coop_name_2', 'coop_salary_2', 'coop_loc_2',
           'coop_name_3', 'coop_salary_3', 'coop_loc_3',
           'coop_name_4', 'coop_salary_4', 'coop_loc_4',
           'coop_name_5', 'coop_salary_5', 'coop_loc_5',
           'coop_name_6', 'coop_salary_6', 'coop_loc_6',
           'fav_coop',
           # Lifestyle
           'sleep_time',
           # School
           'uni_extras', 'fav_course', 'least_fav_course',
           'term_avg_1a',
           'term_avg_1b',
           'term_avg_2a',
           'term_avg_2b',
           'term_avg_3a',
           'term_avg_3b',
           'term_avg_4a',
           'hardest_term', 'easiest_term', 'preferred_program',
           # Future
           'career_motives',
           'preferred_tech_discipline', 'school_debt', 'se_advice']
columns_to_normalize = columns # This will just give me each column separately so that I can start processing data.
