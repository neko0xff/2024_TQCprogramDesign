use std::io;

fn main(){
    let mut input: String = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let num1: f64 = input.trim().parse().unwrap();
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let num2: f64 = input.trim().parse().unwrap();
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let num3: f64 = input.trim().parse().unwrap();
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let num4: f64 = input.trim().parse().unwrap();
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let num5: f64 = input.trim().parse().unwrap();
    input.clear();

    let sum: f64 = num1+num2+num3+num4+num5;
    let avg: f64 = sum/5.0;

    println!("{} {} {} {} {}",num1,num2,num3,num4,num5);
    println!("Sum = {:.1}",sum);
    println!("Average = {:.1}",avg);

}