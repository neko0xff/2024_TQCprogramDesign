use std::io;
use std::f64::consts::PI;

fn main(){
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let radius: f64 = input.trim().parse().unwrap();
    let perimeter: f64 = 2.0*PI*radius;
    let area = (PI*radius).powi(2);

    println!("Radius = {:.2}",radius);
    println!("Perimeter = {:.2}",perimeter);
    println!("Area = {:.2}",area);

}