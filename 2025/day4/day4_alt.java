package com.lukasabbe.dag4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<List<Character>> lines = new ArrayList<>();
        InputStream inputStream = Main.class.getResourceAsStream("/input.txt");
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream, StandardCharsets.UTF_8))) {

            reader.lines().forEach(line -> {
                List<Character> temp = new ArrayList<>();
                for (int i = 0; i < line.length(); i++) {
                    temp.add(line.charAt(i));
                }
                lines.add(temp);
            });

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        long timeStamp = System.currentTimeMillis();
        Thread t1 = new Thread(() -> part1(lines));
        Thread t2 = new Thread(() -> part2(lines));
        t1.start();
        t2.start();
        while(t1.isAlive() || t2.isAlive()){}
        System.out.println((System.currentTimeMillis()-timeStamp));
    }


    public static void part1(List<List<Character>> map){
        int total = 0;
        for(int y = 0; y < map.size(); y++){
            for(int x = 0; x < map.get(y).size(); x++){
                if(map.get(y).get(x) != '@') continue;
                int amount = getAmount(map, x, y);
                if(amount < 4) total++;
            }
        }
        System.out.println( total);
    }
    public static void part2(List<List<Character>> map){
        int total = 0;
        while(true){
            int tempValue = 0;
            for(int y = 0; y < map.size(); y++){
                for(int x = 0; x < map.get(y).size(); x++){
                    if(map.get(y).get(x) != '@') continue;
                    int amount = getAmount(map, x, y);
                    if(amount < 4) {
                        tempValue++;
                        total++;
                        map.get(y).set(x, '.');
                    }
                }
            }
            if (tempValue == 0) break;
        }
        System.out.println(total);
    }

    private static int getAmount(List<List<Character>> map, int x, int y) {
        int[][] dirs = new int[][] {{-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}, {-1, 0}};
        int amount = 0;
        for(var dir : dirs){
            int nx = dir[0] + x;
            int ny = dir[1] + y;
            if(nx < 0 || ny < 0) continue;
            if(nx >= map.get(y).size() || ny >= map.size()) continue;
            if(map.get(ny).get(nx) != '@') continue;
            amount++;
        }
        return amount;
    }
}