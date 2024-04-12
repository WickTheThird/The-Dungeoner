package com.dungeoneer.objects;

import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.physics.box2d.Body;
import com.badlogic.gdx.Gdx;

// Internal  
import com.dungeoneer.screen.GameScreen;
import com.dungeoneer.helper.BodyTester;
import com.dungeoneer.helper.Const;
import com.dungeoneer.helper.ContactType;
import com.dungeoneer.objects.utils.Pair;

// Assets
import com.dungeoneer.helper.Const;
import com.dungeoneer.Dungeoneer;
import com.dungeoneer.objects.Test;

// Deps
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;

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

    for (int i = 0; i < 128; i++) {

        if (i % 32 == 0 && i != 0) {
            
            layers++;
            
            this.tile_x = 0;
            this.tile_y = layers * rc_y;

            System.out.println("Starting a new layer at iteration " + i);
        }

        screenX = (this.tile_x + this.tile_y) * this.height_half;
        screenY = (this.tile_x - this.tile_y) * this.width_half;

        Pair tile_object = new Pair(screenX, screenY);
        
        map.put(tile_object, this.tiles);
        this.tile_keys.add(tile_object);
        

        this.tile_x += rc_x;
        this.tile_y += rc_y;
    }

    this.tile_x = 0;
    this.tile_y = 0;
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
