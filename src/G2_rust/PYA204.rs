use std::io;

fn main(){
    let mut input: String= String::new();
    io::stdin().read_line(&mut input).unwrap();
    let in1: i32 = input.trim().parse().unwrap();
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let in2: i32 = input.trim().parse().unwrap();
    io::stdin().read_line(&mut input).unwrap();
    let op: String = input.trim().parse().unwrap();
    let mut out: i32 = 0;

    // rust無整數除法
    if op == "+" {
        out=in1+in2;    
    }else if op == "-" {
        out=in1-in2;
    }else if op == "*" {
        out=in1*in2;
    }else if op == "/" {
        out=in1/in2;
    }else if op == "%" {
        out=in1%in2;
    }

    println!("{}",out);
}