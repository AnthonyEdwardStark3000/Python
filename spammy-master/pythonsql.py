import pyodbc
server = 'sqldb.database.windows.net'
database = 'AzureDB'
username = 'swathi'
password = 'VMswathi11!@#'
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM CustomerDetails
WHERE Geography = ‘Spain’ AND EstimatedSalary > 190000")
        row = cursor.fetchall()
        for i in range(10):
            print(row[i])