package com.dungeoneer;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Game;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.utils.ScreenUtils;

import com.dungeoneer.screen.GameScreen;

public class Dungeoneer extends Game {

	public static Dungeoneer INSTANCE; // creates one object, and
	// you can exit it from anywhere (note that there would be only one instance of it...)
	private int g_screen_width;
        private int g_screen_height;
	private OrthographicCamera g_camera;


	public Dungeoneer() {
		INSTANCE = this; // physical manifestation of the "this" class...
	}

	public void create() {
		g_screen_width  = Gdx.graphics.getWidth();
		g_screen_height = Gdx.graphics.getHeight();
		g_camera        = new OrthographicCamera();
		g_camera.setToOrtho(false, 
				    g_screen_width, 
				    g_screen_height);
		setScreen(new GameScreen(g_camera));
	}

	public void dispose() {}
	public void pause() {}
	public void resume() {}
	public void resize(int width, int height) {
		g_screen_width = width;
		g_screen_height = height;
	}

	public int getScreenWidth() {
		return g_screen_width;
	}

	public int getScreenHeight() {
		return g_screen_height;
	}
}
