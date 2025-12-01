-- ==========================================
--   BASE DE DATOS: Sistema de Encuestas
--   Archivo: encuestas_completa.sql
--   Motor: MySQL
-- ==========================================

-- Crear base de datos (puedes cambiar el nombre si quieres)
CREATE DATABASE IF NOT EXISTS encuestas
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE encuestas;

-- Eliminar tablas si ya existen (para empezar de cero)
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS respuesta;
DROP TABLE IF EXISTS participante;
DROP TABLE IF EXISTS pregunta;
DROP TABLE IF EXISTS encuesta;
SET FOREIGN_KEY_CHECKS = 1;

-- 1) Tabla ENCUESTA
CREATE TABLE encuesta (
    id_encuesta      INT PRIMARY KEY AUTO_INCREMENT,
    nombre           VARCHAR(100) NOT NULL,
    descripcion      TEXT,
    fecha_creacion   DATETIME DEFAULT CURRENT_TIMESTAMP,
    activa           TINYINT(1) DEFAULT 1
) ENGINE=InnoDB;

-- 2) Tabla PREGUNTA
CREATE TABLE pregunta (
    id_pregunta   INT PRIMARY KEY AUTO_INCREMENT,
    id_encuesta   INT NOT NULL,
    texto         VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_encuesta) REFERENCES encuesta(id_encuesta) ON DELETE CASCADE
) ENGINE=InnoDB;

-- 3) Tabla PARTICIPANTE
CREATE TABLE participante (
    id_participante        INT PRIMARY KEY AUTO_INCREMENT,
    nombre                 VARCHAR(100) NOT NULL,
    correo                 VARCHAR(150) NOT NULL,
    username               VARCHAR(50)  NOT NULL UNIQUE,
    password               VARCHAR(50)  NOT NULL,
    id_encuesta_asignada   INT NULL,
    FOREIGN KEY (id_encuesta_asignada) REFERENCES encuesta(id_encuesta) ON DELETE SET NULL
) ENGINE=InnoDB;

-- 4) Tabla RESPUESTA
CREATE TABLE respuesta (
    id_respuesta     INT PRIMARY KEY AUTO_INCREMENT,
    id_pregunta      INT NOT NULL,
    id_participante  INT NOT NULL,
    valor            ENUM('Regular','Bueno','Excelente','No Responde') NOT NULL,
    fecha_respuesta  DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_pregunta)     REFERENCES pregunta(id_pregunta) ON DELETE CASCADE,
    FOREIGN KEY (id_participante) REFERENCES participante(id_participante) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ==========================================
--   DATOS INICIALES
-- ==========================================

-- 3 encuestas de ejemplo, cada una con 5 preguntas
INSERT INTO encuesta (nombre, descripcion) VALUES
('Encuesta 1', 'E1'),
('Encuesta 2', 'E2'),
('Encuesta 3', 'E3');

INSERT INTO pregunta (id_encuesta, texto) VALUES
(1, 'P1 - Pregunta 1 E1'),
(1, 'P2 - Pregunta 2 E1'),
(1, 'P3 - Pregunta 3 E1'),
(1, 'P4 - Pregunta 4 E1'),
(1, 'P5 - Pregunta 5 E1'),
(2, 'P1 - Pregunta 1 E2'),
(2, 'P2 - Pregunta 2 E2'),
(2, 'P3 - Pregunta 3 E2'),
(2, 'P4 - Pregunta 4 E2'),
(2, 'P5 - Pregunta 5 E2'),
(3, 'P1 - Pregunta 1 E3'),
(3, 'P2 - Pregunta 2 E3'),
(3, 'P3 - Pregunta 3 E3'),
(3, 'P4 - Pregunta 4 E3'),
(3, 'P5 - Pregunta 5 E3');

-- Participantes (sin duplicados de 'edido')
INSERT INTO participante (nombre, correo, username, password) VALUES
('Adriana Romero', 'adrianaromero@latinmail.com', 'aromero', 'aromero'),
('Alan Brito', 'alanbrito@latinmail.com', 'abrito', 'abrito'),
('Alejandra Vega', 'alejandravega@gmail.com', 'avega', 'avega'),
('Alejandro Ortega', 'alejandroortega@hotmail.com', 'aortega', 'aortega'),
('Ana HernÃ¡ndez', 'anahernandez@gmail.com', 'ahernandez', 'ahernandez'),
('AndrÃ©s Molina', 'andresmolina@latinmail.com', 'amolina', 'amolina'),
('Antonio Vargas', 'antoniovargas@gmail.com', 'avargas', 'avargas'),
('Armando Paredes', 'armandopardes@latinmail.com', 'aparedes', 'aparedes'),
('Carlos RodrÃ­guez', 'carlosrodriguez@gmail.com', 'crodriguez', 'crodriguez'),
('Carmen Ruiz', 'carmenruiz@hotmail.com', 'cruiz', 'cruiz'),
('Claudia JimÃ©nez', 'claudiajimenez@gmail.com', 'cjimenez', 'cjimenez'),
('Daniel Mendoza', 'danielmendoza@latinmail.com', 'dmendoza', 'dmendoza'),
('Dolores Fuertes', 'doloresfuertes@hotmail.com', 'dfuertes', 'dfuertes'),
('Eduardo Rojas', 'eduardorojas@latinmail.com', 'erojas', 'erojas'),
('Elena Torres', 'elenatorres@gmail.com', 'etorres', 'etorres'),
('Esteban Dido', 'estebandido@gmail.com', 'edido', 'edido'),
('Fernando GuzmÃ¡n', 'fernandoguzman@hotmail.com', 'fguzman', 'fguzman'),
('Francisco RamÃ­rez', 'franciscoramirez@latinmail.com', 'framirez', 'framirez'),
('Gabriela Silva', 'gabrielasilva@hotmail.com', 'gsilva', 'gsilva'),
('Gloria PeÃ±a', 'gloriapena@hotmail.com', 'gpena', 'gpena'),
('Isabel SÃ¡nchez', 'isabelsanchez@hotmail.com', 'isanchez', 'isanchez'),
('Jorge Castillo', 'jorgecastillo@gmail.com', 'jcastillo', 'jcastillo'),
('JosÃ© MartÃ­nez', 'josemartinez@latinmail.com', 'jmartinez', 'jmartinez'),
('Juan LÃ³pez', 'juanlopez@hotmail.com', 'jlopez', 'jlopez'),
('Laura GarcÃ­a', 'lauragarcia@latinmail.com', 'lgarcia', 'lgarcia'),
('Lola Mento', 'lolamento@hotmail.com', 'lmento', 'lmento'),
('Lucia Herrera', 'luciaherrera@latinmail.com', 'lherrera', 'lherrera'),
('Manuel Salazar', 'manuelsalazar@gmail.com', 'msalazar', 'msalazar'),
('Marcela RÃ­os', 'marcelaarios@hotmail.com', 'marios', 'marios'),
('MarÃ­a GonzÃ¡lez', 'mariagonzalez@hotmail.com', 'mgonzalez', 'mgonzalez'),
('Miguel PÃ©rez', 'miguelperez@gmail.com', 'mperez', 'mperez'),
('Monica Reyes', 'monicareyes@hotmail.com', 'mreyes', 'mreyes'),
('Nora Paredes', 'noraparedes@gmail.com', 'nparedes', 'nparedes'),
('Oscar Delgado', 'oscardelgado@hotmail.com', 'odelgado', 'odelgado'),
('Patricia DÃ­az', 'patriciadiaz@latinmail.com', 'pdiaz', 'pdiaz'),
('Pedro Acosta', 'pedroacosta@gmail.com', 'pacosta', 'pacosta'),
('Rafael Morales', 'rafaelmorales@gmail.com', 'rmorales', 'rmorales'),
('Ricardo NÃºÃ±ez', 'ricardonunez@latinmail.com', 'rnunez', 'rnunez'),
('Roberto Flores', 'robertoflores@hotmail.com', 'rflores', 'rflores'),
('Rosa Ortiz', 'rosaortiz@latinmail.com', 'rortiz', 'rortiz'),
('Sergio Campos', 'sergiocampos@hotmail.com', 'scampos', 'scampos'),
('Sofia Castro', 'sofiacastro@gmail.com', 'scastro', 'scastro'),
('Susana Horia', 'susanahoria@gmail.com', 'shoria', 'shoria'),
('Teresa Cruz', 'teresacruz@latinmail.com', 'tcruz', 'tcruz'),
('Veronica Medina', 'veronicamedina@gmail.com', 'vmedina', 'vmedina');
