package tsp.python.java;

import java.awt.geom.Point2D;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class tsp {

    String path;
    int numCities;
    double expectedAnswer;
    static long startTime;

    public static void main(String[] args){

        startTime = System.nanoTime();
        tsp tsp = new tsp();
        String[] data = tsp.readFile("dat/tsp/tsp.txt");
        Double[][] euclideanDistances = tsp.calculateEuclideanDistances(data);

        Double answer = tsp.tsp(euclideanDistances);

        System.out.println("Answer: " + answer);
        System.out.println("Time Elapsed: " + (System.nanoTime() - startTime) + " Nanoseconds");
    }

    private Double tsp(Double[][] distances){


        // Destination city index, path length indexed by bitmap value of cities leading to destination
        // No reason to include number of hops, since inherent in bitmap, and sets will insure I solve smalled subproblems first
        // Can I save memory here? Each city inherently has an even distribution. I think it's smaller than this (this.numCities -1?). Even -1 would half the memory used.
        // Cannot use index as bitmask maps if this is case. Look into hashmap solution
        // Can also throw away solutions after they're not needed. Solving 1 requires 0, solving 2 requires 1, etc.
        // Will make sense to wait to allocate only the memory needed, so create new array each loop, with the number of subproblems solved for that pathlength and a hashmap
        Double[][] pathLengths = new Double[this.numCities - 1][1 << this.numCities];

        // Generate sets
        Integer[][] sets = this.generateSets();

        // Storing final path lengths for each city for convenience
        Double[] finalLengths = new Double[numCities-1];

        // Set up base cases
        for (int i = 0; i < pathLengths.length; i++){
            // Setting all cities with path index 0 to be equal to distance from origin city
            pathLengths[i][0] = distances[0][i+1];
        }
        System.out.println("Finished paths with length: " + 1);
        System.out.println("Time Elapsed: " + (System.nanoTime() - startTime) + " Nanoseconds");

        // Index path based on bitmap representation
        // Iterate over increasing path lengths
        for (int i = 0; i < sets.length; i++){
            // Iterate over destination cities
            for (int j = 0; j < pathLengths.length; j++){
                // Calculate shortest path and enter it into pathLengths
                for (int k = 0; k < sets[i].length; k++){

                    // Get bitmask
                    int bitmask = sets[i][k];

                    // Get bit representation of current city
                    int mask = (1<<j);

                    // Skip bitmask if it contains destination city
                    if ((mask & bitmask) == mask) {
                        continue;
                    }

                    // Init min path length
                    Double min = Double.POSITIVE_INFINITY;
                    // Init counter to break loop when lengths is full
                    int counter = 0;
                    // Iterate through cities in bitmask
                    for (int l = 31; l >= 0; l--) {
                        // If lengths is full, break this loop
                        if (counter == i + 1){
                            break;
                        }
                        int bit = (bitmask >> l) & 1;
                        if (bit == 1){

                            // 1 << j will be bitwise representation of single city. Invert and call and to get set excluding current city
                            // final hop distance indexes are +1 because distances includes starting city
                            // Combine path length and final hop to get total distance
                            min = Math.min(min, pathLengths[l][(~(1<<l) & bitmask)] + distances[l+1][j+1]);
                        }
                    }

                    // Adding index based on mask used to create path length
                    pathLengths[j][bitmask] = min;

                    // Overriding per city - we only care about last value here
                    finalLengths[j] = min;
                }
            }
            System.out.println("finished paths with length: " + (i + 2));
            System.out.println("Time Elapsed: " + (System.nanoTime() - startTime) + " Nanoseconds");
        }

        // Calculate final hop for each city
        for (int i = 0; i < finalLengths.length; i++){
            finalLengths[i] = finalLengths[i] + distances[i+1][0];
        }

        System.out.println("finished paths with length: " + numCities);


        // Get shortest distance overall
        List<Double> dList = Arrays.asList(finalLengths);
        Double finalMin = Collections.min(dList);

        return finalMin;
    }

    private Integer[][] generateSets() {
        // Sort bitmask sets by bitcount (Hamming Weight)
        // Next, we'll iterate through them for each city, ignoring sets that have their own city flipped

        // Cities excluding starter
        int n = this.numCities - 1;
        int numCombos = (1 << n);

        // Combinations sorted by number of hops
        // 3d array - number of hops, destination city, combination of cities leading to destination city
        Integer[][] combinations = new Integer[n -1][0];

        // Allocate combinations memory
        // Combinations are maxed by n choose k, and k is number of hops
        for (int i = 0; i < n -1; i++){
                combinations[i] = new Integer[choose(n,i + 1)];
        }

        System.out.println("Memory Allocated");
        System.out.println("Time Elapsed: " + (System.nanoTime() - startTime) + " Nanoseconds");

        // Run a loop from 1 to 2^n
        for (int i = 1; i < (1 << n) - 1; i++) {

            // Index by path length. -1 because no 0 length paths
            int lengthIndex = Integer.bitCount(i) - 1;
            for(int k = 0; k<numCombos; k++) {
                // Fill first available slot
                if(combinations[lengthIndex][k] == null)
                {
                    combinations[lengthIndex][k] = i;
                    break;
                }
            }
        }

        System.out.println("Sets calculated");
        System.out.println("Time Elapsed: " + (System.nanoTime() - startTime) + " Nanoseconds");

        return combinations;
    }

    // Returns n choose k
    private int choose(int n, int k){
        if (k == 0){
            return 1;
        }
        else{
            return (n * choose(n - 1, k - 1)) / k;
        }
    }
    private String[] readFile(String path){

        BufferedReader reader;
        List<String> list = new ArrayList<String>();

        try {
            reader = new BufferedReader(new FileReader(path));
            String line = reader.readLine();

            while (line != null) {
                list.add(line);

                // read next line
                line = reader.readLine();
            }

            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        String[] arr = list.toArray(new String[list.size()]);

        return arr;
    }

    private Double[][] calculateEuclideanDistances(String[] data){

        numCities = Integer.parseInt(data[0]);
        try {
            expectedAnswer = Double.parseDouble(data[data.length-1].replaceAll("[^\\d.]", ""));
            System.out.println("Expected Answer: " + expectedAnswer);
        }
        catch(Exception e) {
            System.out.println("Expected Answer Unknown");
        }

        List<Point2D> city_coords = new ArrayList<Point2D>();

        Double[][] allDistances = new Double[data.length - 2][data.length - 2];

        // Get all coordinates
        for (int i = 1; i < data.length - 1; i++){

            String[] coords = data[i].split(" ");
            Double x = Double.parseDouble(coords[0]);
            Double y = Double.parseDouble(coords[1]);

            city_coords.add(new Point2D.Double(x,y));
        }

        for (int i = 0; i < city_coords.size(); i++){

            // Store values per city
            Double[] cityDistances = new Double[data.length -2];

            for (int j = 0; j < city_coords.size(); j++){
                double distance = city_coords.get(i).distance(city_coords.get(j));
                cityDistances[j] = distance;
            }

            allDistances[i] = cityDistances;
        }

        return allDistances;
    }

}
