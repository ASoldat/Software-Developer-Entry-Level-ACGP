const express = require('express')
// const bodyParser = require("body-parser"); 
const app = express()
// Puerto en el que se ejecutará el servidor
const port = 9090

// Para parsear JSON
app.use(express.json());
// Middleware para acceder al formulario
app.use(express.static("public"));

// Ruta raíz que responde con "Hello World!"
app.get('/', (req, res) => {
  res.send('Hello World!')
})

// Se importa la ruta
const bookRoutes = require('./routes/book');

// Rutas
app.use('/api/createBook', bookRoutes);
app.use('/api/listBooks', bookRoutes);


// Se inicia el servidor en el puerto 9090
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
