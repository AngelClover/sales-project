//连接数据库
var mysql = require('mysql');
var connection = mysql.createConnection({
            host: 'localhost',
                user: 'root',
                    password: 'root',
                        database:'dev_sales'
                        });

connection.connect();
//查询
/*
connection.query('SELECT * from equipment', function(err, rows, fields) {
            if (err) throw err;
                //console.log('The solution is: ', rows[0].solution);
            console.log(rows)
            for (var i in rows){
            console.log(i, rows[i], rows[i].info)
            }
            for (var i in fields){
            console.log(i, fields[i].table)
            }
                });
                */
//关闭连接
connection.end();
