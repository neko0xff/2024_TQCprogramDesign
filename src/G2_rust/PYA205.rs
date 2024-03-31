use std::io;

fn main(){
    let mut input: String= String::new();
    io::stdin().read_line(&mut input).unwrap();
    let in1: char=input.trim().parse().unwrap();

    if in1.is_alphabetic(){
        println!("{:} is an alphabet.",in1);
    }else if in1.is_numeric(){
        println!("{:} is a number.",in1);
    }else{
        println!("{:} is a symbol.",in1);
    }
    
}