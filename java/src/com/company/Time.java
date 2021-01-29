package com.company;



import java.util.List;

abstract public class Time {

    private static long time;

    public Time() {
        time = System.currentTimeMillis();
    }

    static public void incrementAges(List<Human> allHumans){

        for (Human human : allHumans){
            human.getOlder();
        }
    }

    static public void displayCurrentTime(){
        System.out.println(time);
    }
}
