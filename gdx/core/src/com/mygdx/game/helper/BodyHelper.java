package com.mygdx.game.helper;

import com.badlogic.gdx.physics.box2d.*;

public class BodyHelper {

    public static Body createBody(float x, float y, float width, float height, boolean isStatic, float density, World world, ContactType type) {

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

}
