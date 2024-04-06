package com.dungeoneer.screen;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.ScreenAdapter;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.math.Vector3;
import com.badlogic.gdx.physics.box2d.World;
import com.badlogic.gdx.physics.box2d.Box2DDebugRenderer;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.math.Rectangle;

import com.dungeoneer.Dungeoneer;

public class TestScreen extends ScreenAdapter {

    private OrthographicCamera g_camera;
    private SpriteBatch        g_batch;
    private World              g_world;
    private Box2DDebugRenderer g_renderer;

    private Texture   g_player_tex;
    private Rectangle g_player_rect;
    private int       g_player_speed = 10;


    public TestScreen(OrthographicCamera camera) {
        g_camera = camera;

	int sw = Dungeoneer.INSTANCE.getScreenWidth();
	int sh = Dungeoneer.INSTANCE.getScreenHeight();
        g_camera.position.set(
		new Vector3(
			sw / 2, 
			sh / 2, 
			0)
		);
        
	g_batch = new SpriteBatch();
        g_world = new World(new Vector2(0, 0), true);
	g_renderer = new Box2DDebugRenderer();


	g_player_tex = new Texture(Gdx.files.internal("test.png"));

	g_player_rect = new Rectangle();
	g_player_rect.x = sw / 2 - 12;
	g_player_rect.y = sh / 2 - 12;
	g_player_rect.width = 24;
	g_player_rect.height = 24;
    }



    private void update() {
        Gdx.gl.glClearColor(0,0,0,1);
	Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        g_world.step(1 / 60f, 6, 2);
	g_camera.update();
        g_batch.setProjectionMatrix(g_camera.combined);
	g_renderer.render(g_world, g_camera.combined);
    }

    private void handleInput(){
        if (Gdx.input.isKeyPressed(Input.Keys.ESCAPE)) { // executes the key while it is pressed
	    Gdx.app.log("TestScreen", "Exiting");
            Gdx.app.exit();
        }

        if (Gdx.input.isKeyPressed(Input.Keys.W)) {
	    g_player_rect.y += 1;
	} else if (Gdx.input.isKeyPressed(Input.Keys.S)) {
	    g_player_rect.y -= 1;
	}
        if (Gdx.input.isKeyPressed(Input.Keys.A)) {
	    g_player_rect.x -= 1;
	} else if (Gdx.input.isKeyPressed(Input.Keys.D)) {
	    g_player_rect.x += 1;
	}
    }

    @Override
    public void render(float delta) {
	this.update();
	this.handleInput();

        g_batch.begin();
	g_batch.draw(g_player_tex, g_player_rect.x, g_player_rect.y);
        g_batch.end();

    }

    public World getWorld() {
        return g_world;
    }

    @Override
    public void dispose(){
	g_player_tex.dispose();
    	g_batch.dispose();
    }

}
