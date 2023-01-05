const mongoose = require('mongoose')
const con = process.env.mongo;
const db = mongoose.connection;
mongoose.connect(con,{
  useNewUrlParser: true,
  useUnifiedTopology: true
}).catch(e => console.log(e))
db.once('open', _ => {
  console.log('nos conectamos correctamente a la db :)')
});
db.on('error', e =>{
  console.log('ocurrio un problema: '+e)
});