package com.mygdx.game.helper;

import com.badlogic.gdx.physics.box2d.*;
import com.badlogic.gdx.graphics.g3d.Model;
import com.badlogic.gdx.graphics.g3d.ModelBuilder;
import com.badlogic.gdx.physics.box2d.Body;
import com.badlogic.gdx.physics.box2d.BodyDef;
import com.badlogic.gdx.physics.box2d.FixtureDef;
import com.badlogic.gdx.physics.box2d.PolygonShape;
import com.badlogic.gdx.physics.box2d.World;

public class BodyHelper {

    //? This is a 2d box creation (might come in handy)
    public static Body createBox(float x, float y, float width, float height, boolean isStatic, float density, World world, ContactType type) {
        BodyDef bodyDef = new BodyDef(); // static body means that the object won't move
        bodyDef.type =  isStatic == false  ? BodyDef.BodyType.DynamicBody : BodyDef.BodyType.StaticBody; // we decide what kind of object we want
        bodyDef.fixedRotation = true;
        bodyDef.position.set(x / Const.PPM, y/ Const.PPM);

        Body body = world.createBody(bodyDef);

        PolygonShape shape = new PolygonShape();
        shape.setAsBox(width / 2 / Const.PPM, height / 2 / Const.PPM);

        FixtureDef fixtureDef = new FixtureDef();
        fixtureDef.shape = shape;
        fixtureDef.density = density;
        body.createFixture(fixtureDef).setUserData(type);

        shape.dispose();
        return body;
    }

    //? This is a 3d box creation (might come in handy)
    public static Body create3dBox(float x, float y, float width, float height, float depth, boolean isStatic, float density, World world, ContactType type) {
        ModelBuilder modelBuilder = new ModelBuilder();
        Model model = modelBuilder.createBox(width, height, depth);

        float[] dimensions = model.calculateBoundingBox(new BoundingBox()).getDimensions().toArray();

        BodyDef bodyDef = new BodyDef(); // static body means that the object won't move
        bodyDef.type =  isStatic == false  ? BodyDef.BodyType.DynamicBody : BodyDef.BodyType.StaticBody; // we decide what kind of object we want
        bodyDef.fixedRotation = true;
        bodyDef.position.set(x / Const.PPM, y/ Const.PPM, z / Const.PPM);

        Body body = world.createBody(bodyDef);

        PolygonShape shape = new PolygonShape();
        shape.setAsBox(dimensions[0] / 2 / Const.PPM, dimensions[1] / 2 / Const.PPM, dimensions[2] / 2 / Const.PPM);

        FixtureDef fixtureDef = new FixtureDef();
        fixtureDef.shape = shape;
        fixtureDef.density = density;
        body.createFixture(fixtureDef).setUserData(type);

        shape.dispose();
        model.dispose();
        return body;
    }
}
