// Controlador para manejar la lógica de libros
// Importar las dependencias necesarias

// Trabajo con archivos
// Se utiliza para leer y escribir información relacionada con los libros en la aplicación.
const fs = require("fs");
const path = require("path");
const filePath = path.join(__dirname, "../data/book.json");

// Controlador para listar todos los libros
const listBooks = (req, res) => {
  // Leer los datos de los libros desde el archivo JSON
  // Si el archivo no existe, devolver un array vacío
  if (!fs.existsSync(filePath)) return [];
  // Si el archivo existe, leer su contenido y devolver los datos en formato JSON
  else {
    const data = fs.readFileSync(filePath);
    const booksData = JSON.parse(data);
    res.json(booksData);
  }
};

// Controlador para crear un nuevo libro
const createBook = (req, res) => {
  // Datos del libro que se reciben en el cuerpo de la solicitud (req.body)
  const { id, titulo, autor } = req.body;
  // Validar que se proporcionen todos los campos necesarios
  if (!id || !titulo || !autor) {
    return res
      .status(400)
      .json({ message: "ID, Título y autor son requeridos" });
  }
  // Leer los datos existentes del archivo JSON, si existe
  // Si el archivo no existe, inicializar un array vacío
  booksData = [];
  if (fs.existsSync(filePath)) {
    const data = fs.readFileSync(filePath);
    booksData = JSON.parse(data);
  }

  // Crear un nuevo objeto de libro y agregarlo al array de libros
  const newBook = { id, titulo, autor };
  booksData.push(newBook);

  // Escribir los datos actualizados de los libros en el archivo JSON
  fs.writeFileSync(filePath, JSON.stringify(booksData, null, 2));
  res.status(201).json({ message: "Libro creado exitosamente", book: newBook });
};

module.exports = {
  createBook,
  listBooks,
};
