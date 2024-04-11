### SQL injection testing with SQLmap 

SQLMap is a powerful tool for automating SQL injection testing. 
It allows you to scan web applications for SQL injection vulnerabilities, identify and exploit these vulnerabilities, and perform additional database analysis.

#### Installing SQLMap:

1. Clone the SQLMap repository from GitHub using the following command:

    ```git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev```

2. Change to the sqlmap-dev directory using the command:

    ```cd sqlmap-dev```

#### Running SQLMap:

Example command to run SQLMap:

```python sqlmap.py -u "http://127.0.0.1:8000/searchProtected/" --data="search_query=admin" --level=5 --risk=3```

**In this comand:**

* u http://localhost:8000/ specifies the URL of your application that you want to test.

* --data="search_query=admin" specifies the POST request data used to send data to the server.

* --level=5 and --risk=3 set the scanning level and risk. The higher the values, the more in-depth and intensive the analysis will be performed by SQLMap.

#### Testing Vulnerable page

**_The command:_** ```python sqlmap.py -u "http://127.0.0.1:8000/searchVulnerable/" --data="search_query=admin" --level=1 --risk=1```

**_Result of testing:_**
```
Parameter: search_query (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause (MySQL comment)
    Payload: search_query=admin' AND 5175=5175#

    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: search_query=admin' AND GTID_SUBSET(CONCAT(0x717a6b7871,(SELECT (ELT(8009=8009,1))),0x71786a7671),8009)-- GtAh

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: search_query=admin' AND (SELECT 6265 FROM (SELECT(SLEEP(5)))Utqh)-- QElk

    Type: UNION query
    Title: MySQL UNION query (NULL) - 4 columns
    Payload: search_query=admin' UNION ALL SELECT NULL,NULL,NULL,CONCAT(0x717a6b7871,0x426d544d517a4758686562684253744e736e795869486162456d725968536e686a6d5a716366666c,0x71786a7671)#
```
This log shows that the 'search_query' parameter is susceptible to various types of SQL injection attacks, such as boolean-based blind, error-based, time-based blind and UNION query. This indicates insufficient or non-existent use of SQL injection protection mechanisms in your application. Such vulnerabilities can lead to serious consequences, including data compromise and application corruption.
#### Testing Protected page

**_The command:_** ```python sqlmap.py -u "http://127.0.0.1:8000/searchProtected/" --data="search_query=admin" --level=2 --risk=2```

**_Result of testing:_**
```
[22:09:32] [WARNING] POST parameter 'search_query' does not seem to be injectable
[22:09:32] [CRITICAL] all tested parameters do not appear to be injectable.
```

SQLMap was unable to detect SQL injection vulnerabilities in the 'search_query' parameter of your application. This may indicate that the application is protected from SQL injection by Django through the use of parameterized queries or other security mechanisms.