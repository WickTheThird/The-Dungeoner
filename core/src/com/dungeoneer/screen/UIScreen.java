package com.dungeoneer.screen;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.utils.viewport.ScreenViewport;
import com.badlogic.gdx.scenes.scene2d.Stage;
import com.badlogic.gdx.ScreenAdapter;
import com.badlogic.gdx.graphics.GL20;



public class UIScreen extends ScreenAdapter {
    private Stage g_stage;

    public void create(){
	    g_stage = new Stage( new ScreenViewport() );
	    Gdx.input.setInputProcessor(g_stage);
    }

    public void resize (int w, int h){
    	g_stage.getViewport().update(w, h, true);
    }

    public void render (float delta) {
	Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);
	g_stage.act(delta);
	g_stage.draw();
    }

    public void dispose(){
    	   g_stage.dispose();
    }
}
