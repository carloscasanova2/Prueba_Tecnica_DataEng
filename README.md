# Prueba_Tecnica_DataEng

## Caso técnico para análisis – Data Engineer

*Para estudiar el fenómeno de preferencia y recambio de automóviles en Chile, se entrega el siguiente set de datos anonimizados de tendencia de vehículos histórica:* 

[Datos anonimizados de vehículos histórica](https://github.com/carloscasanova2/Prueba_Tecnica_DataEng/blob/70e80723d3d79a130049c2f7e1aae29562b1d00e/bbdd%20prueba%20corp.Csv)

A modo de ejemplo, el formato es el siguiente:

![image](https://user-images.githubusercontent.com/95709562/178803322-415f7e77-c97c-4135-809e-e69bdf23617e.png)

Para evaluar las habilidades técnicas requeridas por el cargo, se pide aplicar técnicas de ETL, exploración, descubrimiento y analítica para explicar y caracterizar los fenómenos que en los datos se pueden observar

Por favor cree un dashboard con los hallazgos encontrados, ejemplo: comportamiento de Derco vs el mercado total. (Consulta nuestras marcas: [Derco Center](https://www.dercocenter.cl/)) por región, numero de vehículos, valor de los mismos.

Para la homologación de los nombres de la comuna/region, se puede consultar la siguiente API: [División político administrativa](https://apis.digital.gob.cl/dpa/)


## DESARROLLO

imagen 1. Head de la base de datos: 
![image](https://user-images.githubusercontent.com/95709562/178804940-de082142-435a-4c76-8eaa-0bcd84246370.png)


imagen 2. Regiones suministradas por la API:

![image](https://user-images.githubusercontent.com/95709562/178812578-42395c80-7e4c-4f7a-b093-b7c6f77d0b4f.png)

# VISUALIZACIÓN DE DATOS

## POR SEXO: 

***IMAGEN 3. CANTIDAD DE CLIENTES DERCO VS CANTIDAD DE CLIENTES OTRAS MARCAS***

![SexoClientesDerco](https://user-images.githubusercontent.com/95709562/178814756-d87ea558-619a-4002-a02f-9b577e02d604.png)
![SexoClientesOtrasMarcas](https://user-images.githubusercontent.com/95709562/178814782-e1e54730-d654-4733-acde-182d7077b322.png)

***IMAGEN 4. PORCENTAJE DE CLIENTES DERCO VS PORCENTAJE DE CLIENTES OTRAS MARCAS***

![PorcentajeClientesDercoXSexo](https://user-images.githubusercontent.com/95709562/178815800-a7f31dd2-526b-4d1f-8c27-6798594134ee.png)
![PorcentajeClientesOtrasMarcasXSexo](https://user-images.githubusercontent.com/95709562/178815498-3d93252b-13cb-40c9-9adb-5a6db62c7ee0.png)


## POR EDAD:

***IMAGEN 5. CANTIDAD DE CLIENTES DERCO VS CANTIDAD DE CLIENTES OTRAS MARCAS***

![EdadClientesDerco](https://user-images.githubusercontent.com/95709562/178815662-193765f0-4e4b-4b44-b067-be5fa4191338.png)
![EdadClientesOtrasMarcas](https://user-images.githubusercontent.com/95709562/178816340-2ed8e698-4e65-4ead-aa0e-4993e60363fd.png)

***IMAGEN 6. DISTRIBUCIÓN DE CLIENTES DERCO VS DISTRIBUCIÓN DE CLIENTES OTRAS MARCAS***

![DistribucionEdadClientesDerco](https://user-images.githubusercontent.com/95709562/178816186-a4d1788d-537a-475c-a7f7-54b59eaf6c9e.png)
![DistribucionEdadClientesOtrasMarcas](https://user-images.githubusercontent.com/95709562/178816208-ba18c5e8-c453-4b19-80b7-da192019a88f.png)


## POR CANTIDAD DE VEHÍCULOS:

***IMAGEN 7. CANTIDAD DE VEHICULOS DERCO VS CANTIDAD DE VEHICULOS OTRAS MARCAS***

![CantidadDeVehiculos](https://user-images.githubusercontent.com/95709562/178816879-f1d5af80-f65e-463f-aa51-984f2cf63d17.png)

***IMAGEN 8. PORCENTAJE CANTIDAD DE VEHICULOS DERCO VS PORCENTAJE CANTIDAD DE VEHICULOS OTRAS MARCAS***

![PorcentajeCantidadDeVehiculos](https://user-images.githubusercontent.com/95709562/178817881-e85c249d-2f13-4924-adeb-f9f0742554bd.png)

## POR MARCA:

***IMAGEN 9. PORCENTAJE DE VEHICULOS PERTENECIENTES A DERCO SEGÚN SU MARCA***

![PorcentajeDeMarcasVehiculosDerco](https://user-images.githubusercontent.com/95709562/178817377-fa628272-90e0-46af-bf30-49deba544840.png)


***IMAGEN 10. CANTIDAD DE VEHICULOS POR SU MARCA, SI PERTENECEN O NO A DERCO***

![CantidadDeVehiculosXPropietario](https://user-images.githubusercontent.com/95709562/178818088-5d2d5ce1-8c2c-4390-90be-d0b1f70fa1d3.png)


## POR REGIÓN: 

***IMAGEN 11. CANTIDAD DE VEHICULOS POR REGIÓN, SI PERTENECEN O NO A DERCO***

![CantidadDeVehiculosXRegionYPropietario](https://user-images.githubusercontent.com/95709562/178818630-bdc1521e-f1ac-46c9-911f-44a799a4040d.png)

## POR VALOR:

***IMAGEN 12. Distribución del valor de los vehiculos de los clientes Derco***

![DistribucionValorVehiculosClientesDerco](https://user-images.githubusercontent.com/95709562/178824701-e1f1aa2d-b56c-4f79-b29b-308c676a2071.png)

***IMAGEN 13. Distribución del valor de los vehiculos de los clientes otras marcas**

![DistribucionValorVehiculosClientesOtrasMarcas](https://user-images.githubusercontent.com/95709562/178824894-6d796bb1-f193-4210-80c5-37396c266921.png)


***IMAGEN 14. Distribución del valor de los vehiculos de los clientes Derco por región***

![DistribucionValorVehiculosClientesDercoXRegion](https://user-images.githubusercontent.com/95709562/178825281-e0de3241-168a-4032-b16c-81d2a50fb7fe.png)


***IMAGEN 15. Distribución del valor de los vehiculos de los clientes otras marcas por región***

![DistribucionValorVehiculosClientesOtrasMarcasXRegion](https://user-images.githubusercontent.com/95709562/178825378-e26fd4c5-3b51-4dbc-9924-ae63db14f2ac.png)



# CONCLUSIONES 

1. Como visualizamos en la imagen 3, predominan el sexo masculino por encima del femenino tanto en las otras marcas como en Derco. Sin embargo, en los dos casos (Derco y otras marcas) el porcentaje del sexo masculino y femenino es el mismo, respectivamente 55% y 45%.
2. Las edades que más tienden a preferir a Derco estan entre los intervalos 30-40 y 40-50 años. Mientras que la edad de los clientes que prefieren otras marcas es mas perceptible en el intervalo de 40-50 años. 
3. La diferencia entre la cantidad de vehiculos que hacen parte de otras marcas y los vehiculos de Derco es de 671.603. Los vehiculos que mas predominan entre las otras marcas es el Hyundai, mientras que en Derco los que mas predominan son los Suzuki. La región que mas presenta cantidad de vehiculos tanto para otras marcas como para Derco es la region metropolitana de Santiago. 



