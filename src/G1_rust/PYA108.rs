use std::io;

fn main(){
    let mut input: String = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let x1: f64 = input.trim().parse().unwrap();
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let x2: f64 = input.trim().parse().unwrap();
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let y1: f64 = input.trim().parse().unwrap();
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let y2: f64 = input.trim().parse().unwrap();
    
    let x_pow: f64 = (x1-x2).powi(2);
    let y_pow: f64 = (y1-y2).powi(2);
    let sum: f64 = x_pow + y_pow;
    let out: f64 = sum.sqrt();

    println!("( {} , {} )",x1,y1);
    println!("( {} , {} )",x2,y2);
    println!("Distance = {:.4}",out);
}