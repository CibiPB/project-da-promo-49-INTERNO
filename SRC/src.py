
#COLUMN RENAMES:

title_mapping = {"employeenumber": "employee_number",
                "gender": "gender",
                "datebirth": "birth_year",
                "age": "age",
                "maritalstatus": "marital_status",
                "jobrole": "job_title",
                "department": "department",
                "attrition": "terminated",
                "standardhours": "standard_hours",
                "monthlyincome": "monthly_income",
                "remotework": "remote",
                "businesstravel": "business_travel",
                "dailyrate": "daily_rate",
                "distancefromhome": "dist_home",
                "education": "education_scale",
                "educationfield": "education",
                "environmentsatisfaction": "env_sat_rate",
                "hourlyrate": "hourly_rate",
                "jobinvolvement": "job_involvement",
                "joblevel": "job_level",
                "jobsatisfaction": "job_sat_rate",
                "monthlyrate": "monthly_rate",
                "numcompaniesworked": "num_comp_worked",
                "overtime": "over_time",
                "percentsalaryhike": "perc_salary_hike",
                "performancerating": "perf_rate",
                "relationshipsatisfaction": "relationship_sat_rate",
                "stockoptionlevel": "stock_opt_level",
                "totalworkingyears": "tot_working_year",
                "trainingtimeslastyear": "traning_times_last_year",
                "worklifebalance": "work_life_balance",
                "yearsatcompany": "year_at_comp",
                "yearsincurrentrole": "year_current_role",
                "yearssincelastpromotion": "year_last_promotion",
                "yearswithcurrmanager": "year_current_mngr",
                "salary": "annual_salary",
                "roledepartament": "role_department"}

#COLUMN REORDER:




new_order_columns: ['employee_number', 
                   'gender', 
                   'birth_year', 
                   'age', 
                   'marital_status',
                   'job_level', 
                    'over_time', 
                    'perf_rate',
                    'stock_opt_level', 
                    'traning_times_last_year', 
                    'year_at_comp', 
                    'year_current_role', 
                    'year_last_promotion',
                    'year_current_mngr',
                    'education_scale',
                    'education',
                    'monthly_rate',
                    'perc_salary_hike', 
                    'annual_salary',
                    'env_sat_rate',
                    'job_involvement',
                    'job_sat_rate',
                    'relationship_sat_rate',
                    'work_life_balance',
                    'columns_emp_bgd']

#CATEGORIES: 

columns_personal =   ['employee_number', 
                   'gender', 
                   'birth_year', 
                   'age', 
                   'marital_status']

columns_job =   ['job_level', 
               'over_time', 
               'perf_rate',
               'stock_opt_level', 
               'traning_times_last_year', 
               'year_at_comp', 
               'year_current_role', 
               'year_last_promotion',
               'year_current_mngr']

columns_education = ['education_scale',
                     'education']



columns_income = ['monthly_rate',
                  'perc_salary_hike', 
                  'annual_salary']

columns_satisfaction = ['env_sat_rate',
                        'job_involvement',
                        'job_sat_rate',
                        'relationship_sat_rate',
                        'work_life_balance',
                        'columns_emp_bgd']