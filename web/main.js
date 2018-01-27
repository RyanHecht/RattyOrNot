

var http = require('http');
var url = require('url'); 
var fs = require('fs'); // file System
var sqlite3 = require('sqlite3');



var db = new sqlite3.Database('./testdb.db', function(err) {
    if(err){
        console.error(err.message);
    }
    console.log('Connected to the test database.');
});

function runSQL(name){
    console.log("HERE");
    db.serialize(function() { //serialization allows an internal representation
        // of the database
        db.each('SELECT * FROM table_one WHERE Name=?', [name], function(err, row){
            //db.each does this function for each row after the query
            if(err){
                console.error(err.message);
            }
            console.log(row.Name + "\t" + row.Age);
        });
    

    });
    
}

function requestFunction(req, res){
    console.log("HELP: "+req.query);

    var parsed = url.parse(req.url, true);
    console.log(parsed);
    var pathname = parsed.pathname; 
    console.log("pathname: "+pathname);
    if(pathname == "/"){
        console.log("FUCK YOU")
        pathname = "/index.html"
    }

    // Here is where you can have a function that deals
    // with the different pages, depending on the pathname

    fs.readFile("."+pathname, function(err, data){
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        res.end();


    });

    var q = parsed.query; 
    console.log(q)
    
    


};


var server = http.createServer(requestFunction);
server.listen(8080);
