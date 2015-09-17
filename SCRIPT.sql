create procedure get_ciclo_by_id(
	P_ID IN NUMBER, 
	P_ABREV OUT NVARCHAR2
) as
begin
  SELECT ABREV INTO P_ABREV 
  FROM carga_ciclo 
  WHERE id = P_ID;
end;

-- PARA EJECUTAR UN SP
DECLARE
p_abrev  VARCHAR2(100);
BEGIN
   get_ciclo_by_id(49,p_abrev);
END;
/
