
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


#CATEGORIES: 

columns_personal =  ['employee_number', 
                    'gender', 
                    'birth_year', 
                    'age', 
                    'marital_status',
                    'dist_home']

columns_job =   ['job_title',
                'department',
                'terminated',
                'year_at_comp',
                'year_current_role',
                'standard_hours',
                'remote',
                'business_travel',
                'over_time', 
                'job_level', 
                'stock_opt_level', 
                'traning_times_last_year', 
                'perf_rate',
                'year_last_promotion',
                'year_current_mngr']

columns_education = ['education',
                    'education_scale']


columns_income =    ['annual_salary',
                    'monthly_income',
                    'daily_rate',
                    'hourly_rate',
                    'monthly_rate',
                    'perc_salary_hike']

columns_satisfaction =  ['env_sat_rate',
                        'job_involvement',
                        'job_sat_rate',
                        'relationship_sat_rate',
                        'work_life_balance']

columns_emp_bgd =   ['num_comp_worked',
                    'tot_working_year']

#COLUMN REORDER:

def columnreorder (dataframe):
    new_order_columns = []
    new_order_columns.append(columns_personal,columns_job,columns_education,columns_income,columns_satisfaction,columns_emp_bgd)
    dataframe = dataframe[new_order_columns]