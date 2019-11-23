var express = require("express");
var formidable = require("formidable");
var fs = require("fs");
var util = require("util");
var ws = require("ws");
var http = require("http");
var app = express();

app.use(express.urlencoded({extended:true}));
const { spawn } = require('child_process');


// ls.stderr.on('data', (data) => {
//   console.error(`stderr: ${data}`);
// });

// ls.on('close', (code) => {
//   console.log(`child process exited with code ${code}`);
// });

app.post("/upload",(req,res,next)=>{
    var form = new formidable.IncomingForm();
    form.uploadDir = __dirname+"/upload";
    form.keepExtensions = true;
    form.parse(req,function(err,fields,files){
        if(err){
            throw err;
        }
        console.log(files.file.path);

        // var newPath = form.uploadDir+"/"+files.file.name
        // fs.rename(oldPath,newPath,function(err){
        //     if(err){
        //           console.error("改名失败"+err);
        //     }
        // });
        const ls = spawn('python3', ['../python/test.py',files.file.path]);
        ls.stdout.on('data', (data) => {
            res.setHeader("Access-Control-Allow-Origin","*")
            res.json({ result: data.toString()});  
            console.log(`stdout: ${data}`);
        });

        // ls.stderr.on('data', (data) => {
        //     console.error(`stderr: ${data}`);
        // });
    });
});



app.use(express.static(__dirname+"/static"));

var server = http.createServer(app);


server.listen(8080);