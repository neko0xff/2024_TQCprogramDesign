use std::io;
use std::f64::consts::PI;

fn main(){
    let mut input: String = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let s: f64 = input.trim().parse().unwrap();

    let n: f64 = 5 as f64;
    let tan_n: f64 = (PI/n).tan();
    let area: f64 = (n*s).powi(2)/(4.0*tan_n);

    println!("Area = {:.4}",area);
}