# Problem Solving Questions and Answers in Python, Java, and SQL (Full Code)

# ----------------------------
# PYTHON QUESTIONS WITH FULL CODE
# ----------------------------

# [Existing Python problems remain unchanged]

# ----------------------------
# SQL EXAMPLES (as strings to use in databases)
# ----------------------------

sql_queries = {
    "1. Second Highest Salary": """
    SELECT MAX(salary) FROM employees
    WHERE salary < (SELECT MAX(salary) FROM employees);
    """,

    "2. Count Employees per Department": """
    SELECT department_id, COUNT(*) FROM employees GROUP BY department_id;
    """,

    "3. Find Duplicates": """
    SELECT name, COUNT(*) FROM users GROUP BY name HAVING COUNT(*) > 1;
    """,

    "4. Top 3 Salaries": """
    SELECT * FROM (
      SELECT name, salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
      FROM employees
    ) t WHERE rnk <= 3;
    """,

    "5. Employees Joined Last Year": """
    SELECT * FROM employees WHERE YEAR(join_date) = YEAR(CURDATE()) - 1;
    """,

    "6. Find All Managers": """
    SELECT DISTINCT manager_id FROM employees WHERE manager_id IS NOT NULL;
    """,

    "7. Find Highest Paid in Each Department": """
    SELECT department_id, MAX(salary) FROM employees GROUP BY department_id;
    """,

    "8. Find Employees Without Department": """
    SELECT * FROM employees WHERE department_id IS NULL;
    """,

    "9. Find Employee with Nth Highest Salary": """
    SELECT * FROM (
      SELECT name, salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
      FROM employees
    ) t WHERE rnk = 4; -- Change 4 to desired N
    """,

    "10. Find Employees with Same Salary": """
    SELECT salary, COUNT(*) FROM employees GROUP BY salary HAVING COUNT(*) > 1;
    """,

    "11. Join Employee and Department Tables": """
    SELECT e.name, d.department_name FROM employees e
    JOIN departments d ON e.department_id = d.department_id;
    """,

    "12. Find Total Salary Per Department": """
    SELECT department_id, SUM(salary) FROM employees GROUP BY department_id;
    """,

    "13. Find Employees with No Manager": """
    SELECT * FROM employees WHERE manager_id IS NULL;
    """,

    "14. Find Department with Most Employees": """
    SELECT department_id FROM employees GROUP BY department_id
    ORDER BY COUNT(*) DESC LIMIT 1;
    """,

    "15. Count Employees by Job Title": """
    SELECT job_title, COUNT(*) FROM employees GROUP BY job_title;
    """,

    "16. Find Employees with Name Starting with A": """
    SELECT * FROM employees WHERE name LIKE 'A%';
    """,

    "17. Average Salary by Department": """
    SELECT department_id, AVG(salary) FROM employees GROUP BY department_id;
    """,

    "18. List Departments with No Employees": """
    SELECT * FROM departments WHERE department_id NOT IN (
      SELECT DISTINCT department_id FROM employees
    );
    """,

    "19. List Managers and Their Team Count": """
    SELECT manager_id, COUNT(*) as team_size FROM employees
    WHERE manager_id IS NOT NULL GROUP BY manager_id;
    """,

    "20. Find Duplicate Emails": """
    SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1;
    """,

    "21. List Employees in Multiple Projects": """
    SELECT employee_id FROM project_assignments
    GROUP BY employee_id HAVING COUNT(DISTINCT project_id) > 1;
    """
}

for title, query in sql_queries.items():
    print(f"\n-- {title} --")
    print(query)

# Note: For Java code, use a separate .java file with main method and run these logics similarly.
