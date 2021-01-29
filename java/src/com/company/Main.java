package com.company;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Human human1 = new Human("Yangtao", "Male", 21);
        Human human2 = new Human("Tim", "Male", 18);

        List<Human> humanList = new ArrayList<>();
        humanList.add(human1);
        humanList.add(human2);

//        System.out.println(humanList);

        Time.incrementAges(humanList);

//        System.out.println(humanList);


        Time.displayCurrentTime();
    }
}
