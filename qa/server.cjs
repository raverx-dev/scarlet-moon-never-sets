// Development inspection server only. No dependencies; not part of shipped game.
const http=require('http'),fs=require('fs'),path=require('path');
const ignorable=/^\/(favicon\.ico|apple-touch-icon[^/]*)$/i;
http.createServer((req,res)=>{
  const u=new URL(req.url,'http://localhost');
  if(ignorable.test(u.pathname)){res.writeHead(204);return res.end()}
  let f=u.pathname==='/'?'generated.html':u.pathname==='/baseline'?'../index.html':u.pathname.slice(1);
  if(f.includes('..')&&f!=='../index.html'){res.writeHead(403);return res.end()}
  fs.readFile(path.join(__dirname,f),(e,b)=>{
    if(e){console.error('404',u.pathname);res.writeHead(404);res.end();return}
    res.setHeader('Content-Type',f.endsWith('.html')?'text/html':'application/octet-stream');
    res.end(b);
  });
}).listen(4173,'127.0.0.1',()=>console.log('listening on http://127.0.0.1:4173/'));
