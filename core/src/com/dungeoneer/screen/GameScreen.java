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
import com.badlogic.gdx.InputProcessor;

//> TESTING
import com.dungeoneer.helper.Const;
import com.dungeoneer.Dungeoneer;
import com.dungeoneer.objects.Test;

//> Map
import com.dungeoneer.objects.DungeonMap;

public class GameScreen extends ScreenAdapter {

    private OrthographicCamera camera;
    private SpriteBatch batch;
    private World world;
    private Box2DDebugRenderer box2DDebugRenderer;

    // game objects
    private DungeonMap map;

    public GameScreen(OrthographicCamera camera) {

        this.camera = camera;
        this.camera.position.set(new Vector3(Dungeoneer.INSTANCE.getScreenWidth() / 2, Dungeoneer.INSTANCE.getScreenHeight() / 2, 0));
        this.batch = new SpriteBatch();
        this.world = new World(new Vector2(0, 0), false);
        this.box2DDebugRenderer = new Box2DDebugRenderer();

        // object init
        this.map = new DungeonMap(this);
    }

    private void update() {
        world.step(1 / 60f, 6, 2);

        this.camera.update();
        this.map.update();

        batch.setProjectionMatrix(camera.combined);

        if (Gdx.input.isKeyPressed(Input.Keys.ESCAPE)) {
            Gdx.app.exit();
        }

        if(Gdx.input.isKeyPressed(Input.Keys.LEFT))
            this.camera.translate(-32,0);
        if(Gdx.input.isKeyPressed(Input.Keys.RIGHT))
            this.camera.translate(32,0);
        if(Gdx.input.isKeyPressed(Input.Keys.UP))
            this.camera.translate(0,32);
        if(Gdx.input.isKeyPressed(Input.Keys.DOWN))
            this.camera.translate(0,-32);

    }

    @Override
    public void render(float delta) {

        update();

        Gdx.gl.glClearColor(0,0,0,1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        batch.begin();

        this.map.render(batch);

        batch.end();

        this.box2DDebugRenderer.render(world, camera.combined.scl(Const.PPM));

    }

    public World getWorld() {
        return world;
    }

}
