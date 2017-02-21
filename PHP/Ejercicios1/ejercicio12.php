 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> 
<html>
<head meta chrset=utf-8/>
<body>
<?php
	//creamos un vector y guardamos en ella los indices y valores correspondientes
    $v[1]=90;
    $v[30]=7;
    $v['e']=99;
    $v['hola']=43;
    foreach($v as $indice => $valor){
        echo "<p>";
        echo $indice." = ".$valor;//mostramos los indices y valores del vector
        echo"</p>";
    }
?>  
</body>
</html>
