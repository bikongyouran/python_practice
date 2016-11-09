function add(a, b) {
    return a + b;
}

function mul(a, b) {
    return a * b;
}

function sub(a, b) {
    return a - b;
}

function identify(x) {
    return function() {
        return x;
    };
}

var three = identify(3);


function addf(x) {
    return function(y) {
        return x + y;
    };
}

function curry(binary, x) {
    return function(y) {
        return binary(x, y);
    };
}
//var add3 = curry(add,3);

function curryr(binary, x) {
    return function(y) {
        return binary(y, x);
    }
}
var sub3 = curryr(sub, 3);
//alert(sub3(11))

//first
//function liftf(binary){
//  return function(x){
//    return curry(binary,x);
//  }
//}

//second
function liftf(binary) {
    return function(x) {
        return function(y) {
            return binary(x, y)
        }
    }
}

var addf = liftf(add);
//alert(addf(3)(4))

//var inc = liftf(add)(1)
//var inc = addf(1)
//var inc = curry(add,1)
var inc = curryr(add, 1)
    //alert(inc(5))

function twice(binary) {
    return function(x) {
        return binary(x, x)
    }
}

var double = twice(add);
//alert(double(11));
var square = twice(mul);
//alert(square(11));

function reverse(binary) {
    return function(x, y) {
        return binary(y, x);
    }
}

// function reverse(binary){
//   return function(...args) {
//     return binary(...args.reverse());
//   }
// }
var bus = reverse(sub);
//alert(bus(3,2))

function composeu(func1, func2) {
    return function(x) {
        return func2(func1(x));
    }
}
//alert(composeu(double,square)(5));

function composeb(func1, func2) {
    return function(x, y, z) {
        return func2(func1(x, y), z);
    }
}
//alert(composeb(add,mul)(2,3,7));

function limit(func, n) {
    temp = 0;
    return function(x, y) {
        if (temp < n) {
            temp += 1;
            return func(x, y);
        }
        return undefined
    }
}
var add_ltd = limit(add, 1)
    //alert(add_ltd(3,4))
    //alert(add_ltd(3,5))
    //alert(add_ltd(3,6))

function from(n) {
    return function() {
        var temp = n
        n += 1
        return temp
    }
}
//var gen = from(0);
//alert(gen());
//alert(gen());
//alert(gen());

function to(func, n) {
    return function() {
        var temp = func()
        if (temp < n) {
            return temp
        }
    }
}
//var gen = to(from(3),5)
//alert(gen());
//alert(gen());
//alert(gen());

//function fromTo(a, b){
//  return function(){
//    if(a < b){
//      var temp = a
//      a += 1
//      return temp
//    }
//  }
//}

function fromTo(a, b) {
    return to(from(a), b);
}
//var gen = fromTo(0,3);
//alert(gen());
//alert(gen());
//alert(gen());

function element(array, func) {
    return function() {
        var index = func();
        if (index !== undefined) {
            return array[index];
        }
    }
}
//var gen = element(['a','b','c','d'],fromTo(1,3))
//alert(gen());
//alert(gen());
//alert(gen());

function element(array, func) {
    if (func === undefined) {
        func = fromTo(0, array.length);
    }
    return function() {
        var index = func();
        if (index !== undefined) {
            return array[index];
        }
    }
}
//var gen = element(['a','b','c','d'])
//alert(gen());
//alert(gen());
//alert(gen());
//alert(gen());
//alert(gen());

function collect(func, array) {
    return function() {
        var temp = func()
        if (temp !== undefined) {
            array.push(temp)
        }
        return temp;
    }
}
// var array =[]
// var gen = collect(fromTo(0,2),array);
// console.log(gen());
// console.log(gen());
// console.log(gen());
// console.log(array)

//TODO
function filter(func1, func2) {
    return function recur() {
        var temp = func1();
        if (func2(temp) === true) {
            return temp;
        }
    }
}
// var gen = filter(fromTo(1,5), function third(value){return (value % 3) === 0;});
// console.log(gen());
// console.log(gen());
// console.log(gen());

function concat(func1, func2) {
    return function() {
        var temp1 = func1()
        if (temp1 !== undefined) {
            return temp1;
        }
        var temp2 = func2();
        return temp2;
    }
}
// var gen = concat(fromTo(0,3),fromTo(0,2));
// console.log(gen());
// console.log(gen());
// console.log(gen());
// console.log(gen());
// console.log(gen());
// console.log(gen());

function gensymf(prefix) {
    var temp = from(1);
    return function() {
        return prefix + temp();
    }
}
// var geng =gensymf('G');
// console.log(geng());
// console.log(geng());
// var genh =gensymf('H');
// console.log(genh());
// console.log(genh());

function fibonaccif(a, b) {
    var t1 = a;
    var t2 = b;
    var index = 0;
    return function() {
        if (index == 0) {
            index += 1
            return t1
        }
        if (index == 1) {
            index += 1
            return t2
        }
        var t3 = t1 + t2;
        t1 = t2;
        t2 = t3;
        return t3;
    }
}
// var fib = fibonaccif(0,1);
// console.log(fib());
// console.log(fib());
// console.log(fib());
// console.log(fib());
// console.log(fib());
// console.log(fib());

function counter() {
    var temp = 0;
    return {
        up: function() {
            temp += 1;
            return temp;
        },

        down: function() {
            temp -= 1;
            return temp;
        }
    };
}
// var object = counter();
// var up = object.up;
// var down = object.down;
// console.log(up())
// console.log(down())
// console.log(down())
// console.log(up())

function revocable(f) {
    return {
        invoke: function(x, y) {
            if (f !== undefined) {
                return f(x, y);
            }
        },
        revoke: function() {
            f = undefined;
        }
    }
}
// var rev = revocable(add);
// var add_rev = rev.invoke;
// console.log(add_rev(3,4));
// rev.revoke();
// console.log(add_rev(3,7));

function continuize(f){
    return function(callback,a){
        return callback(f(a));
    }
}
sqrtc = continuize(Math.sqrt);
sqrtc(console.log,81);

