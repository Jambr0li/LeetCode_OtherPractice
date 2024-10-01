fn main() {
	let mut vector: Vec<usize> = vec![5,4,6,3,7,8,10];
	println!("{:?}", vector);
	quicksort(&mut vector);
	println!("{:?}", vector);
}

fn quicksort(vector: &mut [usize]){
	if vector.len() <= 1 {
		return;
	}
	let pivot_index = partition(vector);
	let (left, right) = vector.split_at_mut(pivot_index);
	quicksort(left);
	quicksort(right);
}

fn partition(vector: &mut [usize]) -> usize{
	let pivot = vector[vector.len() - 1];
	let mut i:usize = 0;
	for j in 0..vector.len() - 1 {
		if vector[j] > pivot{
			vector.swap(i, j);
			i += 1;
		}
	}
	vector.swap(i, vector.len() - 1);
	i
}