const express = require('express');
const router = express.Router();
const bookController = require('../controllers/bookController');

// Crear un nuevo libro
router.post('/', bookController.createBook);
// Listar todos los libros
router.get('/', bookController.listBooks);

module.exports = router;