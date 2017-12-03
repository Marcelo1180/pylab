// var exec = require('child_process').exec;
// exec("perl splitwords.pl biz.txt words", function(err, stdout, stderr) {
//   console.log("prueba de datos ",stdout);
// });
// var exec = require('child_process').exec;
// exec("python alg2.py hola como estan todos", function(err, stdout, stderr) {
//   console.log("xxxxxxxxxx",stdout.trim(),"xxx");
// });

// import util from 'util'

function resolverPython(x){
  return new Promise(resolve => {
    var exec = require('child_process').exec;
    exec(`python alg2.py ${x}`, (err, stdout, stderr) => {
      resolve(stdout);
    });
  });
}

// function resolverDespuesDe2Segundos(x) {
//   return new Promise(resolve => {
//     setTimeout(() => {
//       resolve(x);
//     }, 2000);
//   });
// }
//
// async function añadir1(x) {
//   var a = resolverDespuesDe2Segundos(20);
//   var b = resolverDespuesDe2Segundos(30);
//   return x + await a + await b;
// }
//
// añadir1(10).then(v => {
//   console.log(v);  // muestra en consola 60 después de 2 segundos.
// });
async function añadir2(x) {
  // var a = await resolverDespuesDe2Segundos(20);
  // var b = await resolverDespuesDe2Segundos(30);
  // return x + a + b;
  xout = await resolverPython(x)
  return xout
}

añadir2("hola como estan todos").then(v => {
  console.log(v);  // muestra en consola 60 después de 4 segundos.
});
