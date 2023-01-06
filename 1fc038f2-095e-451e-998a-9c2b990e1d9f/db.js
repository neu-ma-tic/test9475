const sqlite3 = require('sqlite3').verbose()

const create = () => {
  let db = new sqlite3.Database('./fries-db.sqlite')
  db.close()
}

const select = () => {
  let db = new sqlite3.Database('./fries-db.sqlite')
  let final = []
  const wrap = () => {
    return new Promise((resolve, reject) => {
      db.all("SELECT * FROM keyv", [], (err, rows) => {
        rows.forEach(row => {
          final.push(row)
        })
        resolve(final)
      })
    })
  }
  return wrap()
}

module.exports = {
  create,
  select
}
