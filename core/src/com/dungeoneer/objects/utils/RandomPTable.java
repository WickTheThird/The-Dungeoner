package com.dungeoneer.objects.utils;

import java.util.Random;
import java.util.ArrayList;


public class RandomPTable {

  public ArrayList<Integer> int_randoms = new ArrayList<>();
  public ArrayList<Double> double_randoms = new ArrayList<>();;
  public ArrayList<Float> float_randoms = new ArrayList<>();;

  public Random rand;

  public RandomPTable() {
    this.rand = new Random();
  }

  public ArrayList<Integer> getRandomInt(int limit) {

    for(int i = 0; i <= limit; ++i) {
      int int_random = this.rand.nextInt(255);
      this.int_randoms.add(int_random);
    }
    
    return this.int_randoms;
  }

  public ArrayList<Double> getRandomDouble(int limit) {

    for (int i = 0; i <= limit; ++i) {
      double double_random = this.rand.nextDouble();
      this.double_randoms.add(double_random);
    }
    
    return this.double_randoms;
  }

  public ArrayList<Float> getRandomFloat(int limit) {

    for (int i = 0; i <= limit; ++i) {
      float float_random = this.rand.nextFloat();
      this.float_randoms.add(float_random);
    }
    
    return this.float_randoms;
  }
}
