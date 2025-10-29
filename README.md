# tpArquitectura_ing2

Trabajo Práctico – Unidad 3: Diseño Arquitectónico
Consigna: A partir del siguiente enunciado, deberás realizar un esquema o breve explicación escrita.

Enunciado: Imaginá que estás diseñando un sistema de gestión para una biblioteca (préstamo de libros, registro de socios, devoluciones, etc.).

Identificá las tres capas principales del sistema (presentación, lógica de negocio, datos) y escribí qué tipo de funciones tendría cada una.
Elegí un problema sencillo del sistema (por ejemplo: acceso centralizado a la base de datos, control de usuarios o manejo de configuración) y explicá con tus palabras qué patrón de diseño podría ayudar a resolverlo (por ejemplo: Singleton, MVC, etc.).
Entrega:

Esquema gráfico (UML).
Validación del modelo en el lenguaje de programación que usted elija.

1_ Las tres capas principales del sistema y sus funciones son:
Capa de presentación o Interfaz de Usuario: Es la capa más externa, la responsable de interactuar con el usuario. Muestra los datos al usuario, captura la entrada del usuario, envía las peticiones a la capa de Lógica de Negocios y produce las validaciones básicas del lado del cliente, como por ejemplo; campos obligatorios, formatos de email y demás. Es donde interactúan los usuarios (bibliotecarios o socios).
Capa de Lógica de Negocios: Es la capa que contiene las reglas y la lógica esencial del sistema, en este caso del negocio de la biblioteca. Esta capa se encarga de validar y procesar las peticiones de la Capa de Presentación. Implementa las reglas del sistema y coordina las operaciones entre las capas de Presentación y la capa de Datos. Es decir, cómo funciona la biblioteca.
Capa de Datos: Esta capa es la responsable de la persistencia de la información del sistema. Se encarga de conectar la base de datos, de realizar operaciones “CRUD” de las entidades del sistema y de abstraer la lógica de acceso a la base de datos de la Capa de Lógica de Negocios.

2_ El problema que elegí para este trabajo es el de “Acceso centralizado a la Base de Datos”, ya que es un aspecto fundamental el hecho de que la conexión a la base de datos y el objeto que gestiona las operaciones de bajo nivel sean únicos y que se acceda a él de forma controlada desde la capa de Datos, evitando las conexiones múltiples y simultáneas, inconsistencias y/o sobrecarga de recursos.
Y el patrón que elegí a raíz de esto es el patrón Singleton, ya que garantiza que una clase una a una única instancia y proporciona un punto de acceso global a ella. La forma en la que se implementa es con la creación de una clase de gestor de conexión, que implemente el patrón Singleton, esta clase manejaría la configuración, como credenciales, url, etc. Y la conexión física a la base de datos. Todas las clases dentro de la capa de Datos, que necesiten interactuar con la persistencia, obtendrían la misma y única instancia de la clase de gestor de conexión.

 En este diagrama de UML de clases, represento cómo utilizo el patrón Singleton, con una única instancia, constructor privado, método getInstance() estático y punto de acceso global. En la capa de presentación, utilizo la clase “BibliotecaUI” para manejar la interacción con el usuario (formularios, menús, vistas, etc), que llama a la capa de negocios para realizar acciones cómo registrar socios o prestar libros. Utilizo la clase de BibliotecaService cómo la capa de lógica de Negocios, esta clase contiene la lógica de validaciones, control de disponibilidad, fechas de préstamos, etc que se comunican con los DAO para acceder a la base de datos. En la capa de datos utilico las clases de LibroDAO y SocioDAO para encargarse de las operaciones CRUD sobre la base de datos, que utilizan la clase de ConexionBD como único punto de conexión global. Finalmente se encuentra la clase ConexionBD, que es la gestión de la conexión a la base de datos, es decir que las demás clases acceden a esta conexión por medio del método getInstancia().

 

 
