<html>
<head ></head>
<title>EUROCONVERSOR 2.0</title>
<body>
<p>
    <?php
    
    $euros=$_POST['entrada'];//obtenemos el valor introducido
        
    if($_REQUEST['radio1']=="libras"){//si hemos seleccionado libras, pasamos el valor a libras
        echo $euros;
        echo "€";
        echo " = ";
        echo $euros*0.850784;
        echo " libras";    
    }if($_REQUEST['radio1']=="dolares"){//si hemos seleccionado libras, pasamos el valor a dolares
        echo $euros;
        echo "€";
        echo " = ";
        echo $euros*1.08;
        echo " dolares";
    }
    
    ?>
</p>
</body>
</html>
