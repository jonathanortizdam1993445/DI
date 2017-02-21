 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> 
<html>
<head meta charset=utf-8/>
<body>
<table>
     <?php
     
    //definimos una constante con el valor de nuestra tabla
    define(TAM,4);
    //declaramos la funcion con los argumentos
    function potencia($base, $exp){
    //pow funcion que eleva a la potencia 
    $res=pow($base,$exp);
    //devolvemos los valores
    return $res;
    }
    
    
 //Iniciamos el bucle de las filas
 for($t=1;$t<=TAM;$t++){
  echo "<tr>";
  //Iniciamos el bucle de las columnas
  for($y=1;$y<=TAM;$y++)
    //decimos que las celdas de las filas se rellenen y autoincrementen el valor hasta ocuparlas todas
    echo "<td>". potencia($t,$y)."</td>";
   //Cerramos columna
   echo "</tr>";
  }
 ?>
 <!-- Cerramos tabla -->
</table>
</body>
</html>
