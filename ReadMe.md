文件: api/routes/modules.py, 行号: 27, 严重性: WARNING
漏洞类型: security
描述: Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead.
语言: Python
--------------------------------------------------
文件: api/routes/modules.py, 行号: 113, 严重性: WARNING
漏洞类型: maintainability
描述: code after return statement will not be executed
语言: Python
--------------------------------------------------
文件: core/db.py, 行号: 15, 严重性: WARNING
漏洞类型: best-practice
描述: `pass` is the body of function init_db. Consider removing this or raise NotImplementedError() if this is a TODO
语言: Python
--------------------------------------------------
文件: crud.py, 行号: 8, 严重性: ERROR
漏洞类型: security
描述: bcrypt hash detected
语言: Python
--------------------------------------------------
文件: main.py, 行号: 40, 严重性: ERROR
漏洞类型: best-practice
描述: time.sleep() call; did you mean to leave this in?
语言: Python
--------------------------------------------------
文件: main.py, 行号: 60, 严重性: WARNING
漏洞类型: security
描述: CORS policy allows any origin (using wildcard '*'). This is insecure and should be avoided.
语言: Python
--------------------------------------------------
文件: rbac/rbac.py, 行号: 135, 严重性: ERROR
漏洞类型: security
描述: Hardcoded JWT secret or private key is used. This is a Insufficiently Protected Credentials weakness: https://cwe.mitre.org/data/definitions/522.html Consider using an appropriate security mechanism to protect the credentials (e.g. keeping secrets in environment variables)
语言: Python
--------------------------------------------------
文件: rbac/rbac.py, 行号: 196, 严重性: WARNING
漏洞类型: maintainability
描述: Is "is_authenticated" a function or an attribute? If it is a function, you may have meant user.is_authenticated() because user.is_authenticated is always true.
语言: Python
--------------------------------------------------
文件: semgrepTest.py, 行号: 55, 严重性: ERROR
漏洞类型: security
描述: Detected subprocess function 'run' without a static string. If this data can be controlled by a malicious actor, it may be an instance of command injection. Audit the use of this call to ensure it is not controllable by an external resource. You may consider using 'shlex.escape()'.
语言: Python
--------------------------------------------------
