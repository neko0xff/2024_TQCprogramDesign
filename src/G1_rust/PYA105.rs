use std::io;

fn main(){
    let mut input = String::new();

    io::stdin().read_line(&mut input).unwrap();
    let h: f64 = input.trim().parse().unwrap();
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let w: f64 = input.trim().parse().unwrap();

    let perimeter: f64 = (h+w)*2.0;
    let area: f64 = h*w;

    println!("Height = {:.2}",h);
    println!("Width = {:.2}",w);
    println!("Perimeter = {:.2}",perimeter);
    println!("Area = {:.2}",area);

}