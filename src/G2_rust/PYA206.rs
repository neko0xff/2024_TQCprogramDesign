use std::io;

fn main(){
    let mut input: String=String::new();
    io::stdin().read_line(&mut input).unwrap();
    let in1: i32=input.trim().parse().unwrap();

    if in1>=80 {
        println!("A");
    }else if in1>=70 {
        println!("B");
    }else if in1>=60 {
        println!("C");
    } else {
        println!("F");
    }
    
}