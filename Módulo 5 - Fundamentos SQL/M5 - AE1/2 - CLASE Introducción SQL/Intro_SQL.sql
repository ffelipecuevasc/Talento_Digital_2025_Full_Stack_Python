-- 1. INSERCIÓN (INSERT)
-- ¡Llegó un usuario nuevo! Vamos a guardarlo.
INSERT INTO Netflix_Usuarios (id, nombre, plan) 
VALUES (1, 'Pedro Pascal', 'Premium');
-- Traducción: "Base de datos, inserta en la tabla Usuarios a Pedro con el plan Premium".

-- 2. CONSULTA (SELECT)
-- Queremos ver quiénes tienen el plan más caro.
SELECT nombre 
FROM Netflix_Usuarios 
WHERE plan = 'Premium';
-- Traducción: "Muéstrame solo el NOMBRE de los usuarios DONDE el plan sea 'Premium'".

-- 3. ACTUALIZACIÓN (UPDATE)
-- Pedro quiere ahorrar dinero y baja su plan.
UPDATE Netflix_Usuarios 
SET plan = 'Básico' 
WHERE nombre = 'Pedro Pascal';
-- Traducción: "Actualiza la tabla y pon el plan en 'Básico', pero SOLO a Pedro".

-- 4. ELIMINACIÓN (DELETE)
-- Pedro se enojó porque no hay buenas series y canceló su cuenta.
DELETE FROM Netflix_Usuarios 
WHERE nombre = 'Pedro Pascal';
-- Traducción: "Borra de la tabla al usuario cuyo nombre sea Pedro Pascal".
-- ⚠️ ¡CUIDADO! Si olvidas el 'WHERE', ¡borrarías a TODOS los usuarios de Netflix!