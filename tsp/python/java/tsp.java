package tsp.python.java;

import java.awt.geom.Point2D;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
public class tsp {

    String path;
    double num_cities;
    double answer;
    double[] euclidean_distances;

    public static void main(String[] args){

        tsp tsp = new tsp();
        String[] data = tsp.readFile("dat/tsp/t2.txt");
        tsp.calculateEuclideanDistances(data);


    }

    private String[] readFile(String path){

        BufferedReader reader;
        List<String> list
                = new ArrayList<String>();
        try {
            reader = new BufferedReader(new FileReader(path));
            String line = reader.readLine();

            while (line != null) {
                list.add(line);
                System.out.println(line);

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

    private double[] calculateEuclideanDistances(String[] data){

        num_cities = Double.parseDouble(data[0]);
        answer = Double.parseDouble(data[data.length-1].replaceAll("[^\\d.]", ""));

        List<Point2D> city_coords = new ArrayList<Point2D>();
        List<ArrayList<Double>> allDistances = new ArrayList<ArrayList<Double>>();

        // Get all coordinates
        for (int i = 1; i < data.length - 1; i++){

            String[] coords = data[i].split(" ");
            Double x = Double.parseDouble(coords[0]);
            Double y = Double.parseDouble(coords[1]);

            city_coords.add(new Point2D.Double(x,y));
        }

        for (int i = 0; i < city_coords.size(); i++){

            // Store values per city
            ArrayList<Double> cityDistances = new ArrayList<Double>();

            for (int j = 0; j < city_coords.size(); j++){
                double distance = city_coords.get(i).distance(city_coords.get(j));
                cityDistances.add(distance);
            }

            allDistances.add(cityDistances);
        }

        // Convert arraylist to list


        euclidean_distances = new double[]{1, 2, 3};

        return euclidean_distances;
    }
}
