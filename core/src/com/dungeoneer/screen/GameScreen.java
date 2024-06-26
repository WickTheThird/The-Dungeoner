package com.dungeoneer.screen;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.ScreenAdapter;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.math.Vector3;
import com.badlogic.gdx.physics.box2d.Box2DDebugRenderer;
import com.badlogic.gdx.physics.box2d.World;
import com.badlogic.gdx.Input;

//> TESTING
import com.dungeoneer.helper.Const;
import com.dungeoneer.Dungeoneer;
import com.dungeoneer.objects.Test;

public class GameScreen extends ScreenAdapter {

    private OrthographicCamera camera;
    private SpriteBatch batch;
    private World world;
    private Box2DDebugRenderer box2DDebugRenderer;

    // game objects
    private Test test;

    public GameScreen(OrthographicCamera camera) {

        this.camera = camera;
	this.camera.position.set(new Vector3(Dungeoneer.INSTANCE.getScreenWidth() / 2, Dungeoneer.INSTANCE.getScreenHeight() / 2, 0));
        this.batch = new SpriteBatch();
        this.world = new World(new Vector2(0, 0), false);
        this.box2DDebugRenderer = new Box2DDebugRenderer();

        // object init
        this.test = new Test(32, Dungeoneer.INSTANCE.getScreenHeight() / 2, this);

    }

    private void update() {
        world.step(1 / 60f, 6, 2);

        this.camera.update();
        this.test.update();

        batch.setProjectionMatrix(camera.combined);

        if (Gdx.input.isKeyPressed(Input.Keys.ESCAPE)) { // executes the key while it is pressed
            Gdx.app.exit();
        }

    }

    @Override
    public void render(float delta) {

        update();

        Gdx.gl.glClearColor(0,0,0,1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        batch.begin();

        this.test.render(batch);

        batch.end();

        this.box2DDebugRenderer.render(world, camera.combined.scl(Const.PPM));

    }

    public World getWorld() {
        return world;
    }

}
