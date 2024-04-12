package com.dungeoneer.screen;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.utils.viewport.ScreenViewport;
import com.badlogic.gdx.utils.viewport.Viewport;
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
	    /*
    	Viewport tmp = g_stage.getViewport();
	if (tmp != null){
		tmp.update(w, h, true);
	}
	*/
    }

    public void render (float delta) {
	Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);
	if(g_stage != null){
		System.out.println("Confirm");
		g_stage.act(delta);
		g_stage.draw();
	}
    }

    public void dispose(){
    	   g_stage.dispose();
    }
}
