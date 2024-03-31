use std::io;

fn main(){
    let mut input: String = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n1: i32=input.trim().parse().unwrap();

    if n1%2 == 0 {
        println!("{} is an even number.",n1);
    }else if n1%2 == 1 {
        println!("{}is not an even number.",n1);
    }
}