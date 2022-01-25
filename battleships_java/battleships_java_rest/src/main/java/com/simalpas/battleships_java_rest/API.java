/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.simalpas.battleships_java_rest;

import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.ws.rs.Consumes;
import javax.ws.rs.Produces;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PUT;
import javax.enterprise.context.RequestScoped;
import javax.json.bind.Jsonb;
import javax.json.bind.JsonbBuilder;
import javax.ws.rs.FormParam;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

/**
 * REST Web Service
 *
 * @author simal
 */
@Path("api")
@RequestScoped
public class API
{

    @Context
    private UriInfo context;
//    declare a game object
    private BattleshipsMain gameInstance;
    /**
     * Creates a new instance of API
     */
    public API()
    {
    }

//    /**
//     * Retrieves representation of an instance of com.simalpas.battleships_java_rest.API
//     * @return an instance of java.lang.String
//     */
//    @GET
//    @Produces(MediaType.APPLICATION_JSON)
//    public String getJson()
//    {
//        //TODO return proper representation object
//        throw new UnsupportedOperationException();
//    }
//
//    /**
//     * PUT method for updating or creating an instance of API
//     * @param content representation for the resource
//     */
//    @PUT
//    @Consumes(MediaType.APPLICATION_JSON)
//    public void putJson(String content)
//    {
//    }
    
    
    /**
     * Creates instance of BattleshipsMain
     * @Param json with fields {p1auto, p2auto, p1AiLevel, p2AiLevel, boardSize}
     * @return Response
     */
    @PUT
    @Path("/newAutoGame")
    public Response newGame(@FormParam("json") String json)
    {
        Jsonb jsonb = JsonbBuilder.create();
        
        gameInstance = jsonb.fromJson(json, BattleshipsMain.class);
        
        System.out.println("Created a game instance" + gameInstance);
        Response response = Response.ok(gameInstance.toString()).build();
        
        return response;
    }

    /**
     * PUT method for updating or creating an instance of API
     * @param content representation for the resource
     */
    @GET
    @Produces(MediaType.TEXT_HTML)
    public String testingDeployment()
    {
        //TODO
        return "<html><body><h2>Seems to be working</h2></body></html>";
    }
}
