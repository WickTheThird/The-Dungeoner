package com.dungeoneer.objects;

import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.physics.box2d.Body;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.math.Vector2;

// Internal  
import com.dungeoneer.screen.GameScreen;
import com.dungeoneer.helper.BodyTester;
import com.dungeoneer.helper.Const;
import com.dungeoneer.helper.ContactType;
import com.dungeoneer.objects.utils.Pair;
// import com.dungeoneer.objects.utils.RandomPTable;

// Assets
import com.dungeoneer.helper.Const;
import com.dungeoneer.Dungeoneer;
import com.dungeoneer.objects.Test;

// Deps
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.lang.Math;

public class DungeonMap{

  protected int x, y;
  protected int width, height;
  protected float tile_x, tile_y;
  protected int height_half, width_half;
  Map<Pair, Texture> map = new HashMap<>();
  ArrayList<Pair> tile_keys = new ArrayList<>();
  protected GameScreen gameScreen;
  protected Texture tiles;
  
  public DungeonMap(GameScreen gameScreen) {
    
    this.gameScreen = gameScreen;

    this.x = 0;
    this.y = 0;
    this.tile_x = 0;
    this.tile_y = 0;

    this.height = 132;
    this.width = 115;

    this.height_half = 66;
    this.width_half = 77;

    this.tiles = new Texture("landscape_22.png");

    this.create();
  }

  public void create() {

    float rc_x = 0.85f;
    float rc_y = 0.85f;
    int layers = 0;

    float screenX;
    float screenY;

    // Generatig grid
    for (int i = 0; i < 128; i++) {

        if (i % 32 == 0 && i != 0) {
            
            layers++;
            
            this.tile_x = 0;
            this.tile_y = layers * rc_y;

            // System.out.println("Starting a new layer at iteration " + i);
        }

        screenX = (this.tile_x + this.tile_y) * this.height_half;
        screenY = (this.tile_x - this.tile_y) * this.width_half;

        Pair tile_object = new Pair(screenX, screenY);
        
        map.put(tile_object, this.tiles);
        this.tile_keys.add(tile_object);

        // System.out.println(String.valueOf(screenX) + " " + String.valueOf(screenY));

        int X = (int) Math.floor(screenX) & 0xFF;
        int Y = (int) Math.floor(screenY) & 0xFF;

        // System.out.println(String.valueOf(X) + " " + String.valueOf(Y));

        double xf = screenX - (long) screenX;
        double yf = screenY - (long) screenY;

        // System.out.println(String.valueOf(xf) + " " + String.valueOf(yf));

        Vector2 topRight = new Vector2((float)(xf-1.0), (float)(yf-1.0));
        Vector2 topLeft = new Vector2((float)xf, (float)(yf-1.0));
        Vector2 bottomRight = new Vector2((float)(xf-1.0), (float)yf);
        Vector2 bottomLeft = new Vector2((float)xf, (float)yf);  

        ArrayList<Integer> permutationTable = this.PermutationArray();

        int valueTopRight = permutationTable.get(permutationTable.get(X + 32) + Y + 32);
        int valueTopLeft = permutationTable.get(permutationTable.get(X) + Y + 32);
        int valueBottomRight = permutationTable.get(permutationTable.get(X + 32) + Y);
        int valueBottomLeft = permutationTable.get(permutationTable.get(X) + Y);

        Vector2 constantTopRight = this.GetConstantVector(valueTopRight);
        Vector2 constantTopLeft = this.GetConstantVector(valueTopLeft);
        Vector2 constantBottomRight = this.GetConstantVector(valueBottomRight);
        Vector2 constantBottomLeft = this.GetConstantVector(valueBottomLeft);

        float dotTopRight = this.dotProduct(topRight, constantTopRight);
        float dotTopLeft = this.dotProduct(topLeft, constantTopLeft);
        float dotBottomRight = this.dotProduct(bottomRight, constantBottomRight);
        float dotBottomLeft = this.dotProduct(bottomLeft, constantBottomLeft);

        double u = this.Fade(xf);
        double v = this.Fade(yf);

        double output = this.Lerp(u, 
                                  this.Lerp(v, (double) dotBottomLeft, (double) dotTopLeft),
                                  this.Lerp(v, (double) dotTopRight, (double) dotBottomRight)
                                 );

        System.out.println(String.valueOf(output));

        this.tile_x += rc_x;
        this.tile_y += rc_y;
    }

    // resetting variables
    this.tile_x = 0;
    this.tile_y = 0;
  }

  public float dotProduct(Vector2 vectorA, Vector2 vectorB) {
    return vectorA.x * vectorB.x + vectorA.y * vectorB.y;
  }

  public Vector2 GetConstantVector(int v) {

    int h = v & 3;
    if (h == 0) {
      return new Vector2(1.0f, 1.0f);
    } else if (h == 1) {
      return new Vector2(-1.0f, 1.0f);
    } else if (h == 2) {
      return new Vector2(-1.0f, -1.0f);
    } else {
      return new Vector2(1.0f, -1.0f);
    }

  }

  public double Fade(double t) {
    return ((6*t - 15)*t + 10)*t*t*t;
  }

  public double Lerp(double t, double a1, double a2) {
    return a1 + t*(a2-a1);
  }

  public ArrayList<Integer> Shuffle(ArrayList<Integer> arrayToShuffle) {
      for (int e = arrayToShuffle.size() - 1; e >= 0; e--) {
          int index = (int) (Math.random() * (e - 1));
          int temp = arrayToShuffle.get(e);

          arrayToShuffle.set(e, arrayToShuffle.get(index));
          arrayToShuffle.set(index, temp);
      }

      return arrayToShuffle;
  }

  public ArrayList<Integer> PermutationArray() {
        ArrayList<Integer> perm1 = new ArrayList<>();
        ArrayList<Integer> perm2 = new ArrayList<>(); // Fixed typo here

        for (int i = 0; i < 256; ++i) {
            perm1.add(i);
            perm2.add(i);
        }

        perm1 = this.Shuffle(perm1);
        perm2 = this.Shuffle(perm2);

        ArrayList<Integer> combinedPerm = new ArrayList<>(perm1);
        combinedPerm.addAll(perm2);

        return combinedPerm;
  }

  public void update() {}

  public void render(SpriteBatch batch) {
     
     for (Pair tile: this.tile_keys) {

        batch.draw(this.map.get(tile),
                tile.getX(), 
                tile.getY(), 
                this.width, 
                this.height);
        }
    
     }
  }
