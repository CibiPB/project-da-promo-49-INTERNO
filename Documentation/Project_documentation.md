La empresa ABC Corporation nos ha encargado desarrollar un proyecto de análisis de datos para conocer el grado de satisfacción de sus empleados. Para ello nos ha proporcionado una base de datos con información sobre sus empleados como departamento al que pertenecen, puesto, salario, años en la empresa y nivel educativo, entre otras.

Hemos comenzado el proyecto realizando un EDA para conocer los datos y la relación entre ellos y poder hacer una limpieza que nos permita tener una visualización más limpia y fácil de manejar. Tras una primera exploración encontramos algunas columnas que no nos aportan información relevante para el objetivo de nuestro análisis, por lo que tomamos la decisión de eliminarlas con el fin de tener datos con información clave para el estudio. Hemos renombrado las columnas para unificar el formato y darles un nombre más intuitivo en función del dato que contienen. Así mismo, encontramos filas con información duplicada basándonos en el employee_number, que es la primary key de la tabla, hemos eliminado la duplicidad quedándonos con el primer dato introducido. También hemos asignado categorías a las columnas para poder filtrar por su tipo  de información.

Tras realizar una primera limpieza general hemos comenzado con un análisis inicial de los datos para posteriormente analizarlos en profundidad por las categorías que hemos formado.
En el análisis general hemos observado la cantidad de nulos que tiene cada columna y analizado en profundidad estos datos para tomar las decisiones oportunas sobre su tratamiento. Otro paso importante ha sido la realización y análisis de un Heatmap que nos ha permitido conocer el grado de correlación entre las diferentes variables, este gráfico tendrá relevancia para la gestión de nulos y el conocimiento de la correlación de veriables que nos pueda aportar una visión clara sobre el objetivo del estudio.
También hemos visualizado y comprendido la información estadística sobre las columnas por categorías: personal, trabajo, salario, educación, satisfacción y experiencia laboral. 

Comenzamos una limpieza en profundidad tomando decisiones basadas en el análisis previo de los datos: 
- Modificamos el formato de algunas columnas para que sea adecuado a la información que contienen, como convertir a tipo numérico columnas como 'employee_number','age' o 'education_scale'. Y a tipo categórico valores que tenían una escala como 'gender' y 'remote'.
- Modificamos errores tipográficos en la columna 'marital_status'.
- Cambiamos a positivos valores numéricos de la columna 'dist_home' que estaban erróneos.

Pasamos al tratamiento de los valores nulos, en este paso hemos tenido que analizar en profundidad la información de las columnas y su relación con otras para tomar decisiones sobre cómo gestionarlos.
- En la columna 'department' tratamos en un principio de rellenarlos con la columna 'RoleDepartment' separando su información en dos, sin éxito ya que tenía exactamente los mismos nulos. Tras analizar otras columnas para ver si podíamos conocer el departamento de alguna manera vimos que no era posible, por lo que tomamos la decisión de cambiarlo por 'unknown'. Seguimos este mismo método para los nulos en 'marital_status', 'business_travel', 'over_time' y 'education_field'.
Para alguna columnas pudimos realizar una imputación de los datos con el método KNNI, como es el caso de la columna 'age' que pudimos completar sus nulos con la columna 'birth_year'. De la misma manera que pudimos completar los datos nulos de salario con las columnas 'monthly_income', 'daily_rate', 'annual_salary', ya que todas tenían una relación directa entre sí.

En este punto ya contamos con una base de datos limpia y completa y un profundo conocimiento de esta, por lo que procedemos a extraer información concluyente sobre nuestro objetivo: el grado de satisfacción de los empleados.
Para ello creamos una serie de hipótesis sobre qué variables pueden tener relación con el grado de satisfacción:
- Tiempo en la empresa, experiencia total, jornada completa o media jornada, el salario, la distancia del trabajo a casa


