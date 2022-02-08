Test de Ingeniero DevOps

Sobre la aplicacion ⚙️

La aplicación está desarrollada en Flask(python) y realiza un request sobre el endpoint proporcionado, el resultado de este request es parseado a json el cual es utilizado para construir el HTML con dicha información.

Sobre CI-CD 📦

Se implemento un pipeline (Jenkinsfile) en suite de Jenkins, la cual se compone de tres stages:
   
    * Stage Build: Descargamos el código desde su repositorio en Github
    * Test Stage: Ejecuta las pruebas unitarias para la aplicación Flask, validando que la respuesta al endpoint de "/seguro" sea un 200
    * Deploy Stage: Ejecuta la aplicación Flask en nohup y agregue la salida a log.txt


Sobre el flujo de Git. 🚀

Para esta prueba no se implementó gitflow ya que la funcionalidad a desarrollar era solo una, el pipeline se ejecuta con cualquier commit que se haga sobre main.
