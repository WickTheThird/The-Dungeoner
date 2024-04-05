package com.mygdx.game.objects;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.mygdx.game.GameScreen;

public class Test extends TestBody {
    public Test(float x, float y, GameScreen gameScreen) {
        super(x, y, gameScreen);
    }

    public void setPosition(float x, float y) {
        this.x = x;
        this.y = y;
    }

    public void update() {
        super.update();

        if (Gdx.input.isKeyPressed(Input.Keys.W)) {
            velY = 1;
        }

        if (Gdx.input.isKeyPressed(Input.Keys.S)) {
            velY = -1;
        }

        body.setLinearVelocity(0, velY * speed);

    }

    public float getX() {
        return this.x;
    }

    public float getY() {
        return this.y;
    }
}