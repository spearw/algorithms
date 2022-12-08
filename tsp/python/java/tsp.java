package tsp.python.java;

import sun.security.util.Length;

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
        Integer[][][] sets = tsp.generateSets();

        Double answer = tsp.tsp(euclideanDistances, sets);

        System.out.println("Answer: " + answer);
        System.out.println("Time Elapsed: " + (System.nanoTime() - startTime) + " Nanoseconds");
    }

    private Double tsp(Double[][] distances, Integer[][][] sets){

        // Create array large enough to avoid overflowing
        // Destination city index, path length indexed by bitmap value of cities leading to destination
        // No reason to include number of hops, since inherent in bitmap, and sets will insure I solve smalled subproblems first
        Double[][] pathLengths = new Double[this.numCities - 1][1 << this.numCities];

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
            for (int j = 0; j < sets[i].length; j++){
                // Calculate shortest path and enter it into pathLengths
                for (int k = 0; k < sets[i][j].length; k++){

                    // Get bitmask set
                    int set = sets[i][j][k];
                    // Init array for holding possible path lengths
                    Double[] lengths = new Double[i + 1];
                    // Iterate through cities in bitmask
                    for (int l = 31; l >= 0; l--) {
                        int bit = (set >> l) & 1;
                        if (bit == 1){

                            // 1 << j will be bitwise representation of single city. Invert and call and to get set excluding current city
                            // final hop distance indexes are +1 because distances includes starting city
                            // Combine path length and final hop to get total distance
                            double len = pathLengths[l][(~(1<<l) & set)] + distances[l+1][j+1];

                            // Fill first available slot
                            for (int p = 0; p < lengths.length; p++){
                                if(lengths[p] == null){
                                    lengths[p] = len;
                                    break;
                                }
                            }

                        }
                    }

                    List<Double> dList = Arrays.asList(lengths);
                    Double min = Collections.min(dList);

                    // Adding index based on mask used to create path length
                    pathLengths[j][set] = min;

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

    private Integer[][][] generateSets() {
        // Sort bitmask sets by bitcount (Hamming Weight)
        // Next, we'll iterate through them for each city, ignoring sets that have their own city flipped

        // Cities excluding starter
        int n = this.numCities - 1;
        int numCombos = (1 << n);

        // Combinations sorted by number of hops
        // 3d array - number of hops, destination city, combination of cities leading to destination city
        Integer[][][] combinations = new Integer[n-1][n][0];

        // Allocate combinations memory
        // Combinations are maxed by n1 choose r, where n1 is n - 1, and k is number of hops
        for (int i = 0; i < n-1; i++){
            for (int j = 0; j < n; j++){
                combinations[i][j] = new Integer[choose(n-1,i + 1)];
            }
        }

        System.out.println("Memory Allocated");
        System.out.println("Time Elapsed: " + (System.nanoTime() - startTime) + " Nanoseconds");

        // Run a loop from 1 to 2^n
        for (int i = 1; i < (1 << n); i++) {

            // Create set for each destination city
            for (int j = 0; j < n; j++){
                // Discount sets that have destination city included in combination of cities leading to destination
                int bitwiseCity = (1 << j);
                if ((bitwiseCity & i) == bitwiseCity){
                    continue;
                }

                // Index by path length. -1 because no 0 length paths
                int lengthIndex = Integer.bitCount(i) - 1;
                for(int k = 0; k<numCombos; k++) {
                    // Fill first available slot
                    if(combinations[lengthIndex][j][k] == null)
                    {
                        combinations[lengthIndex][j][k] = i;
                        break;
                    }
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
