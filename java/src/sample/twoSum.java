package sample;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class twoSum{

	Integer count;
	int target;

	public static void main(String[] args){


		twoSum testSum = new twoSum();

		ArrayList<Integer> testArray = new ArrayList<>();
		testArray.add(3);
		testArray.add(10);

		System.out.println(testSum.sum("../2-SUM-test.txt", testArray));

		twoSum sum = new twoSum();

		ArrayList<Integer> array = new ArrayList<>();
		array.add(-10000);
		array.add(10000);

		System.out.println(testSum.sum("../2-SUM.txt", array));
	}

	private Integer sum(String filePath, ArrayList<Integer> range){

		count = 0;

		try {
			File myObj = new File(filePath);
			Scanner myReader = new Scanner(myObj);
			Hashtable<Double, Double> hashtable = new Hashtable<>();

			while (myReader.hasNextLine()) {
				double doubleLine = Double.parseDouble(myReader.nextLine());
				hashtable.put(doubleLine, doubleLine);
			}
			myReader.close();

			Set<Double> set = hashtable.keySet();

			Iterator<Double> iterator;

			for(target = range.get(0); target <= range.get(1); target++){

				iterator = set.iterator();
				while(iterator.hasNext()){

					if (set.contains(target - iterator.next())){

						count++;
						System.out.println("Count: " + count);
						break;
					}
				}
			}

			System.out.println(set);


		} catch (FileNotFoundException e) {
			System.out.println("An error occurred.");
			e.printStackTrace();
		}

		return count;
	}
}
