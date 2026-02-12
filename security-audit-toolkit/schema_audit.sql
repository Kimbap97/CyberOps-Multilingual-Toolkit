-- src/schema_audit.sql
-- 1. Identificar usuarios con privilegios excesivos
SELECT grantee, privilege_type 
FROM information_schema.user_privileges 
WHERE privilege_type = 'SUPER';

-- 2. Procedimiento para prevenir SQL Injection (Parametrización)
CREATE PROCEDURE GetUserSafe(IN userId INT)
BEGIN
    PREPARE stmt FROM 'SELECT username, email FROM users WHERE id = ?';
    SET @id = userId;
    EXECUTE stmt USING @id;
    DEALLOCATE PREPARE stmt;
END;